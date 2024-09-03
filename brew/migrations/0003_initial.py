# Generated by Django 5.1 on 2024-09-02 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brew', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffee_type', models.CharField(max_length=200)),
                ('temperature', models.CharField(max_length=500)),
                ('caffeine_amount', models.CharField(max_length=200)),
                ('price', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snack_name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(max_length=200)),
            ],
        ),
    ]