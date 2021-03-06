# Generated by Django 2.2.5 on 2020-05-04 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_supplier_web_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Supplier', verbose_name='Supplier'),
        ),
        migrations.CreateModel(
            name='Supplier_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Category')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name': 'Categories By Supplier',
                'verbose_name_plural': 'Categories By Suppliers',
                'ordering': ('category_id',),
            },
        ),
    ]
