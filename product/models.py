from django.db import models

# ---------------- CATEGORY MODEL ----------------------
class Category(models.Model):
    category_name = models.CharField('Category Name', max_length=100, db_index=True)
    category_description = models.CharField('Category Description', max_length=200, null=True, blank=True)
    is_active = models.BooleanField('Active', default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Product Category'
        verbose_name_plural = 'Print Categories'

    def __str__(self):
        return self.category_name

# --------------- SUPPLIER ----------------------------
class Supplier(models.Model):
    supplier_name = models.CharField('Supplier Name',max_length=100, db_index=True)
    supplier_code = models.CharField('Supplier Code', max_length=10)
    is_active = models.BooleanField('Active', default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('supplier_name',)
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.supplier_name


# -------------- PRODUCT -------------------------------
class Product(models.Model):
    cat_no = models.CharField('Cat #', max_length=20, db_index=True)
    product_name = models.CharField('Product Name', max_length=200)
    web_address = models.URLField('Web Address', max_length=200, null=True, blank=True)
    warrenty_period = models.PositiveIntegerField('Warrenty Period')
    category_id = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier, related_name='products', on_delete=models.CASCADE)
    is_active = models.BooleanField('Active', default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('product_name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__ (Self):
        return self.product_name
