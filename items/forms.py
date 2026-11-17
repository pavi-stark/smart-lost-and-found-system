from django import forms
from .models import Item

CATEGORY_CHOICES = [
    ('Accessories', 'Accessories'),
    ('Electronics', 'Electronics'),
    ('Documents', 'Documents'),
    ('Clothing', 'Clothing'),
    ('Keys', 'Keys'),
    ('Other', 'Other'),
]

class ItemForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={
            'id': 'category',
            'name': 'category',
            'class': 'form-input'
        })
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'id': 'date',
            'name': 'date',
            'class': 'form-input'
        })
    )

    class Meta:
        model = Item
        fields = ['title', 'category', 'place', 'date', 'description', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'item',
                'name': 'item',
                'placeholder': 'e.g., Black leather wallet',
                'class': 'form-input',
                'required': True
            }),
            'place': forms.TextInput(attrs={
                'id': 'place',
                'name': 'place',
                'placeholder': 'e.g., Central library, 2nd floor',
                'class': 'form-input',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'id': 'description',
                'name': 'description',
                'rows': 4,
                'placeholder': 'Distinctive marks, contents, brown stitching on the edge...',
                'class': 'form-input'
            }),
            'photo': forms.FileInput(attrs={
                'id': 'photo',
                'class': 'file-input'
            }),
        }
        labels = {
            'title': 'Item name',
            'category': 'Category',
            'place': 'Place where lost',
            'date': 'Date',
            'description': 'Description',
            'photo': 'Photo (optional)',
        }
