# Generated by Django 5.1.7 on 2025-03-11 17:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Cuisine",
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
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("profile_pic", models.ImageField(upload_to="images/")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
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
                ("title", models.CharField(max_length=30)),
                ("description", models.TextField(default="")),
                (
                    "ingredients",
                    models.TextField(
                        default="", help_text="Separate ingredients with commas."
                    ),
                ),
                (
                    "cook_time",
                    models.PositiveIntegerField(help_text="Cooking time in minutes."),
                ),
                ("servings", models.PositiveIntegerField()),
                ("method", models.TextField(default="")),
                ("image", models.ImageField(upload_to="images/")),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("easy", "easy"),
                            ("medium", "medium"),
                            ("hard", "hard"),
                            ("expert", "expert"),
                        ],
                        default="easy",
                        max_length=250,
                    ),
                ),
                ("category", models.ManyToManyField(to="recipes.category")),
                ("cuisine", models.ManyToManyField(to="recipes.cuisine")),
            ],
        ),
    ]
