from django.contrib import admin
from .models import Category
from .models import Product
#add modelds
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name","description","icon")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display = ['id', 'name', 'price', 'color', 'brand', 'image', 'storge']
