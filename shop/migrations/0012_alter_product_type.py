# Generated by Django 4.2.1 on 2023-06-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_city_province_id_remove_city_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Type',
            field=models.CharField(choices=[('درجه یک', 'درجه یک'), ('درجه دو', 'درجه دو'), ('درجه سه', 'درجه سه')], max_length=20),
        ),
    ]