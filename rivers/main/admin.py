from django.contrib import admin

from .models import Item, ItemImage

@admin.register(ItemImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'alt_text')

admin.site.register(Item)