# Generated by Django 5.1 on 2024-09-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0008_product_delete_coffee_delete_snack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='in_stock',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=True),
        ),
    ]
