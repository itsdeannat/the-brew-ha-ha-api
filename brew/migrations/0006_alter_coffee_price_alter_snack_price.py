# Generated by Django 5.1 on 2024-09-02 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0005_alter_coffee_caffeine_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='snack',
            name='price',
            field=models.FloatField(),
        ),
    ]