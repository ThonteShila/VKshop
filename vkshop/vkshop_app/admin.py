from django.contrib import admin
from .models import Category,ProductImage,Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)

