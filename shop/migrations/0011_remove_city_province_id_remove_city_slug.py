# Generated by Django 4.2.1 on 2023-06-27 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_city_province_id_city_slug_alter_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='province_id',
        ),
        migrations.RemoveField(
            model_name='city',
            name='slug',
        ),
    ]
