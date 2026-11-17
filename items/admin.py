from django.contrib import admin
from .models import Item, LostItem, Skill

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'place', 'date', 'status', 'owner', 'created_at')
    list_filter = ('status', 'category', 'date')
    search_fields = ('title', 'place', 'description')
    ordering = ('-created_at',)

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'place')
    search_fields = ('name', 'place')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
