# Generated by Django 5.1 on 2025-01-11 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='00000', max_length=5),
        ),
    ]
