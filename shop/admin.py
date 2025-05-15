from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'image']
    fieldsets = [
        (None, {'fields': ('name', 'slug', 'description', 'image')})
    ]

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = [
        'name',
        'price',
        'available',
        'is_hot',
        'created',
        'updated',
    ]
    list_filter = ['available', 'is_hot', 'created', 'updated']
    list_editable = ['price', 'available', 'is_hot']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
