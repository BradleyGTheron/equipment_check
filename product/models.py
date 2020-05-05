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
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.category_name

# --------------- SUPPLIER ----------------------------
class Supplier(models.Model):
    supplier_name = models.CharField('Supplier Name',max_length=100, db_index=True)
    supplier_code = models.CharField('Supplier Code', max_length=10)
    web_address = models.URLField('Web Address', max_length=200, blank=True)
    is_active = models.BooleanField('Active', default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('supplier_name',)
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.supplier_name

# --------------- SUPPLIER_CATEGORY ---------------------
class Supplier_Category(models.Model):
    category_id = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier, verbose_name='Supplier',on_delete=models.CASCADE)
    description = models.CharField('Description', max_length=50,
                                    help_text='Description that will be displayed in the category list of the Product')
    is_active = models.BooleanField('Active', default=True)

    class Meta:
        ordering = ('category_id',)
        verbose_name = 'Categories By Supplier'
        verbose_name_plural = 'Product Categories By Suppliers'

    def __str__(self):
        return '{} - {}'.format(self.supplier_id.supplier_name, self.category_id.category_name)




# -------------- PRODUCT -------------------------------
class Product(models.Model):
    cat_no = models.CharField('Cat #', max_length=20, db_index=True)
    product_name = models.CharField('Product Name', max_length=200)
    web_address = models.URLField('Web Address', max_length=200, null=True, blank=True)
    warrenty_period = models.PositiveIntegerField('Warrenty Period', help_text='The warrenty period in years.')
    supplier_id = models.ForeignKey(Supplier, verbose_name='Supplier', related_name='products', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Supplier_Category,verbose_name='Category',
                                    limit_choices_to={'is_active': True }, related_name='products',on_delete=models.CASCADE,)
    is_active = models.BooleanField('Active', default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('product_name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__ (self):
        return self.product_name
