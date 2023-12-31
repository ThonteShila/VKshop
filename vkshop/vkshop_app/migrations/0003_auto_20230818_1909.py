# Generated by Django 3.2 on 2023-08-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkshop_app', '0002_auto_20230815_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_details',
            old_name='image',
            new_name='product_image',
        ),
        migrations.AddField(
            model_name='product_details',
            name='category_slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
