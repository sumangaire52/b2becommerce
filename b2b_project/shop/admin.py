from django.contrib import admin
from .models import Category, SubCategory, SubSubCategory, Product

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
admin.site.register(Product)
