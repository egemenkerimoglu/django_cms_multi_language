# Generated by Django 4.1.7 on 2023-03-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="description",
            field=models.CharField(blank=True, max_length=160),
        ),
    ]
