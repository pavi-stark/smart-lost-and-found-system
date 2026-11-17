from django.db import models
from django.contrib.auth.models import User

# Main Project Model – Smart Lost and Found System (Report Page 25)
class Item(models.Model):
    STATUS_CHOICES = [
        ("lost", "Lost"),
        ("found", "Found"),
        ("claimed", "Claimed"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="items")
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="items/", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"

    @property
    def name(self):
        return self.title

    @property
    def initials(self):
        """Returns 2-letter uppercase initials for the card header badge (e.g., BW, BB, AP, IC)."""
        words = self.title.strip().split()
        if len(words) >= 2:
            return f"{words[0][0]}{words[1][0]}".upper()
        elif words and len(words[0]) >= 2:
            return words[0][:2].upper()
        elif words:
            return (words[0][0] + "X").upper()
        return "LF"

    @property
    def card_color(self):
        """Returns color palette matching Figure 8.1 screenshot."""
        title_lower = self.title.lower()
        if "wallet" in title_lower:
            return "#4f46e5"  # Vibrant Indigo (BW)
        elif "water" in title_lower or "bottle" in title_lower:
            return "#06b6d4"  # Vibrant Cyan / Teal (BB)
        elif "phone" in title_lower or "android" in title_lower or "mobile" in title_lower:
            return "#ec4899"  # Vibrant Rose / Pink (AP)
        elif "card" in title_lower or "id" in title_lower:
            return "#f59e0b"  # Warm Amber / Orange (IC)
        elif "umbrella" in title_lower:
            return "#10b981"  # Emerald Green (UM)
        elif self.category == "Electronics":
            return "#8b5cf6"  # Purple
        elif self.category == "Documents":
            return "#f59e0b"  # Amber
        return "#4f46e5"


# Practice 3 Model (Report Chapter 7.3, Page 21)
class LostItem(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


# Practice 1 & 2 Demo Skill Model (Report Chapter 6.2, Page 15)
class Skill(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name
