# Generated by Django 4.1.7 on 2023-03-25 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("title_tr", models.CharField(max_length=200, null=True)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("slug_tr", models.SlugField(max_length=200, null=True, unique=True)),
                ("slug_en", models.SlugField(max_length=200, null=True, unique=True)),
                ("is_active", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("description_tr", models.TextField(blank=True, null=True)),
                ("description_en", models.TextField(blank=True, null=True)),
            ],
            options={
                "ordering": ["title"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BlogTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("is_active", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["title"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("title_tr", models.CharField(max_length=200, null=True)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("slug_tr", models.SlugField(max_length=200, null=True, unique=True)),
                ("slug_en", models.SlugField(max_length=200, null=True, unique=True)),
                ("is_active", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "cover_image",
                    models.ImageField(blank=True, null=True, upload_to="post"),
                ),
                ("content", tinymce.models.HTMLField(blank=True, null=True)),
                ("content_tr", tinymce.models.HTMLField(blank=True, null=True)),
                ("content_en", tinymce.models.HTMLField(blank=True, null=True)),
                ("view_count", models.PositiveBigIntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blog.blogcategory",
                    ),
                ),
                ("tag", models.ManyToManyField(to="blog.blogtag")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
