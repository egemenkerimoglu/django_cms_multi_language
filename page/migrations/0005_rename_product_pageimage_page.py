# Generated by Django 4.1.7 on 2023-03-28 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0004_pageimage_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pageimage",
            old_name="product",
            new_name="page",
        ),
    ]
