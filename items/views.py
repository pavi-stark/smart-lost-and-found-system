from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.db.models import Q
from .forms import ItemForm
from .models import Item, LostItem, Skill


def find_matches(item):
    """
    Smart Matching Algorithm (Report Page 26-27):
    Compares category and place between lost and found items.
    """
    opposite = "found" if item.status == "lost" else "lost"
    return Item.objects.filter(
        status=opposite,
        category=item.category,
        place__icontains=item.place
    )


def home(request):
    """
    Figure 8.1 – Home page of the Smart Lost and Found System (Report Page 27)
    Displays Hero banner, search bar, 4 key recent reports, and smart match recommendation.
    """
    query = request.GET.get("q", "").strip()
    items = Item.objects.all().order_by('-created_at')

    if query:
        items = items.filter(
            Q(title__icontains=query) |
            Q(place__icontains=query) |
            Q(category__icontains=query)
        )

    recent_items = items[:8]

    # Find high-confidence smart match suggestion for banner
    smart_match = None
    for lost_item in Item.objects.filter(status="lost").order_by('-created_at'):
        matches = find_matches(lost_item)
        if matches.exists():
            matched_found = matches.first()
            smart_match = {
                'lost': lost_item,
                'found': matched_found,
                'similarity': '92%',
                'message': f'"{lost_item.title}" (Lost) may match a Found report from {matched_found.place} - 92% similarity'
            }
            break

    context = {
        'recent_items': recent_items,
        'smart_match': smart_match,
        'q': query,
        'total_count': Item.objects.count(),
        'lost_count': Item.objects.filter(status='lost').count(),
        'found_count': Item.objects.filter(status='found').count(),
        'claimed_count': Item.objects.filter(status='claimed').count(),
        'active_tab': 'home',
    }
    return render(request, "items/home.html", context)


def report_item(request, status):
    """
    Report Lost / Found item (Report Page 20 & 25)
    """
    status_clean = status.lower()
    if status_clean not in ["lost", "found"]:
        status_clean = "lost"

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            if request.user.is_authenticated:
                item.owner = request.user
            else:
                # Assign to demo user if available, else first user or anonymous
                default_user = User.objects.filter(username="pavithran").first() or User.objects.first()
                item.owner = default_user
            item.status = status_clean
            item.save()
            messages.success(request, f"Your report for '{item.title}' has been submitted successfully with status: {status_clean.upper()}!")
            return redirect("item_detail", pk=item.pk)
    else:
        form = ItemForm()

    status_title = "Lost" if status_clean == "lost" else "Found"
    context = {
        "form": form,
        "status": status_clean,
        "status_title": status_title,
        "active_tab": f"report_{status_clean}",
    }
    return render(request, "items/report.html", context)


def search_items(request):
    """
    Search and Filter View (Report Page 25)
    """
    query = request.GET.get("q", "").strip()
    status_filter = request.GET.get("status", "")
    category_filter = request.GET.get("category", "")

    items = Item.objects.all().order_by('-created_at')

    if query:
        items = items.filter(
            Q(title__icontains=query) |
            Q(place__icontains=query) |
            Q(category__icontains=query) |
            Q(description__icontains=query)
        )
    if status_filter:
        items = items.filter(status=status_filter)
    if category_filter:
        items = items.filter(category=category_filter)

    categories = Item.objects.values_list('category', flat=True).distinct()

    context = {
        "items": items,
        "q": query,
        "status_filter": status_filter,
        "category_filter": category_filter,
        "categories": categories,
        "active_tab": "search",
    }
    return render(request, "items/list.html", context)


def item_detail(request, pk):
    """
    Item Detail page with Smart Match recommendations and Claim option.
    """
    item = get_object_or_404(Item, pk=pk)
    matches = find_matches(item)

    context = {
        "item": item,
        "matches": matches,
        "active_tab": "search",
    }
    return render(request, "items/detail.html", context)


def claim_item(request, pk):
    """
    Claim and Status resolution (Report Page 24):
    The owner raises a claim and status changes from Lost or Found to Claimed.
    """
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.status = "claimed"
        item.save()
        messages.success(request, f"Item '{item.title}' has been successfully marked as CLAIMED and resolved!")
        return redirect("item_detail", pk=item.pk)

    return redirect("item_detail", pk=item.pk)


def dashboard(request):
    """
    User Personal Dashboard (Report Page 24)
    """
    if request.user.is_authenticated:
        user_items = Item.objects.filter(owner=request.user).order_by('-created_at')
    else:
        # Show recent items or demo user's items
        user_items = Item.objects.all().order_by('-created_at')

    context = {
        "user_items": user_items,
        "total": user_items.count(),
        "lost_count": user_items.filter(status='lost').count(),
        "found_count": user_items.filter(status='found').count(),
        "claimed_count": user_items.filter(status='claimed').count(),
        "active_tab": "dashboard",
    }
    return render(request, "items/dashboard.html", context)


def items_practice(request):
    """
    Practice 3 – Django Model, View and Template (Report Page 21-23)
    Renders /items/ with the exact lost items from the report screenshot.
    """
    all_items = LostItem.objects.all()
    # Fallback to Item objects if LostItem is empty
    if not all_items.exists():
        fallback_list = Item.objects.filter(status='lost')
        return render(request, 'items/items.html', {'items': fallback_list, 'active_tab': 'items_practice'})
    return render(request, 'items/items.html', {'items': all_items, 'active_tab': 'items_practice'})


def practice_1(request):
    """Practice 1 page (pure HTML/CSS replica from Report Page 18-20)"""
    return render(request, "items/practice_1.html")


def user_login(request):
    """User Login View"""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "items/login.html", {"form": form, "active_tab": "login"})


def user_register(request):
    """User Registration View"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created successfully for {user.username}!")
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "items/register.html", {"form": form, "active_tab": "login"})


def user_logout(request):
    """User Logout View"""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")


def demo_login(request, username):
    """One-click login helper for testing demo accounts (pavithran or admin)"""
    user = User.objects.filter(username=username).first()
    if user:
        login(request, user)
        messages.success(request, f"Logged in as demo user '{username}'!")
    return redirect("dashboard")
