# Generated by Django 5.1 on 2024-09-02 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='snack',
            name='price',
            field=models.IntegerField(),
        ),
    ]
