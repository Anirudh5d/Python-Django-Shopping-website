# Generated by Django 5.0.3 on 2024-04-13 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_digitalappliances_image_groceries_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qauntity',
            new_name='quantity',
        ),
    ]
