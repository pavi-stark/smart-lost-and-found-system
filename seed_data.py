import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lost_and_found.settings')
django.setup()

from django.contrib.auth.models import User
from items.models import Item, LostItem, Skill

def seed():
    print("Seeding database with report data...")

    # 1. Create or update Users
    admin_user, _ = User.objects.get_or_create(
        username="admin",
        defaults={
            "email": "admin@novalisinfotech.com",
            "is_staff": True,
            "is_superuser": True
        }
    )
    admin_user.set_password("adminpassword123")
    admin_user.save()

    pavi_user, _ = User.objects.get_or_create(
        username="pavithran",
        defaults={
            "email": "pavithran@novalisinfotech.com",
            "first_name": "Pavithran",
            "last_name": "V",
            "is_staff": False
        }
    )
    pavi_user.set_password("pavithranpassword123")
    pavi_user.save()

    # Clear existing items to maintain clean seed
    Item.objects.all().delete()
    LostItem.objects.all().delete()
    Skill.objects.all().delete()

    # 2. Main Project Items (Figure 8.1 - Report Page 27)
    items_data = [
        {
            "title": "Black Wallet",
            "category": "Accessories",
            "place": "Central Library",
            "date": date(2026, 8, 11),
            "description": "Black leather wallet containing ID card and two bank cards. Brown stitching on the edge.",
            "status": "lost",
            "owner": pavi_user
        },
        {
            "title": "Blue Water Bottle",
            "category": "Accessories",
            "place": "Canteen",
            "date": date(2026, 8, 12),
            "description": "Stainless steel blue water bottle with a silver cap found on the 2nd row canteen table.",
            "status": "found",
            "owner": admin_user
        },
        {
            "title": "Android Phone",
            "category": "Electronics",
            "place": "Block B, Room 204",
            "date": date(2026, 8, 10),
            "description": "Black Android smartphone with clear bumper case, misplaced during practical lab session.",
            "status": "lost",
            "owner": pavi_user
        },
        {
            "title": "ID Card",
            "category": "Documents",
            "place": "Bus Stand",
            "date": date(2026, 8, 13),
            "description": "College student identity card with lanyard found near college bus bay 3.",
            "status": "found",
            "owner": admin_user
        },
        # Found Black Wallet to activate 92% Smart Match suggestion for "Black Wallet" (Central Library)
        {
            "title": "Black Leather Wallet",
            "category": "Accessories",
            "place": "Central Library",
            "date": date(2026, 8, 11),
            "description": "Found leather wallet handed in at the central library front desk by a student.",
            "status": "found",
            "owner": admin_user
        },
        {
            "title": "Umbrella",
            "category": "Accessories",
            "place": "Main Gate",
            "date": date(2026, 8, 9),
            "description": "Blue foldable umbrella left behind near main security guard desk.",
            "status": "lost",
            "owner": pavi_user
        },
        {
            "title": "College ID Card",
            "category": "Documents",
            "place": "Bus Stand",
            "date": date(2026, 8, 12),
            "description": "Lost college identification card with blue strap.",
            "status": "lost",
            "owner": pavi_user
        },
        {
            "title": "Scientific Calculator",
            "category": "Electronics",
            "place": "Exam Hall 3",
            "date": date(2026, 8, 8),
            "description": "Casio fx-991EX scientific calculator found after semester exam.",
            "status": "claimed",
            "owner": pavi_user
        }
    ]

    for item_data in items_data:
        Item.objects.create(**item_data)
    print(f"Created {len(items_data)} items in Item table.")

    # 3. Practice 3 Items (Report Chapter 7.3, Page 22-23)
    practice_3_data = [
        {"name": "Black Leather Wallet", "place": "Central Library"},
        {"name": "Blue Water Bottle", "place": "Canteen"},
        {"name": "Android Phone", "place": "Block B, Room 204"},
        {"name": "College ID Card", "place": "Bus Stand"},
        {"name": "Umbrella", "place": "Main Gate"},
    ]

    for p3 in practice_3_data:
        LostItem.objects.create(name=p3["name"], place=p3["place"])
    print(f"Created {len(practice_3_data)} items in LostItem table.")

    # 4. Skills (Report Chapter 6.2, Page 15-16)
    skills_data = [
        {"name": "Python", "category": "Programming"},
        {"name": "Django", "category": "Backend Framework"},
        {"name": "HTML5 & CSS3", "category": "Frontend"},
        {"name": "JavaScript", "category": "Frontend"},
        {"name": "MySQL", "category": "Database"},
    ]
    for sk in skills_data:
        Skill.objects.create(name=sk["name"], category=sk["category"])
    print("Seeding completed successfully!")

if __name__ == '__main__':
    seed()
