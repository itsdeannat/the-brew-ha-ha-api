# Generated by Django 5.1 on 2024-09-19 15:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=20)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='in progress', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='Default Description', max_length=200)),
                ('temperature', models.CharField(blank=True, max_length=500, null=True)),
                ('caffeine_amount', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('description', models.CharField(default='Default Description', max_length=200)),
                ('quantity', models.IntegerField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='brew.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brew.product')),
            ],
        ),
    ]
