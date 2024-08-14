from django import forms
from .models import Item

class AdItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['Item_name', 'Item_descr', 'price', 'it_image']