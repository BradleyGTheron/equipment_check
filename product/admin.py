from django.contrib import admin
from .models import Category, Supplier, Product, Supplier_Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'is_active',]
    ordering = ['category_name']
    list_editable = ['is_active',]

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['supplier_name','web_address','is_active',]
    ordering = ['supplier_name',]

class Supplier_CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id','supplier_id','is_active']
    list_filter = ['category_id', 'supplier_id',]
    list_editable = ['is_active',]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','cat_no','supplier_id','is_active',]
    list_filter = ['supplier_id','is_active',]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Supplier_Category, Supplier_CategoryAdmin)
admin.site.register(Product, ProductAdmin)
