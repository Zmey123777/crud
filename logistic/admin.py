from django.contrib import admin
from logistic.models import Product, Stock, StockProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'description']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    search_fields = ['address']

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'stock', 'product', 'quantity', 'price']
    search_fields = ['stock__address', 'product__title']
