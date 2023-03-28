# Generated by Django 4.0.4 on 2022-07-07 21:34

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
            name="LanguagesLabel",
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
                ("label", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "Label",
                "verbose_name_plural": "Labels",
            },
        ),
        migrations.CreateModel(
            name="Phrase",
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
                (
                    "source_lang",
                    models.CharField(
                        choices=[
                            ("1", "English"),
                            ("2", "Ukrainian"),
                            ("3", "Russian"),
                            ("4", "German"),
                            ("5", "Polish"),
                            ("6", "Italian"),
                            ("7", "French"),
                            ("8", "Spanish"),
                            ("9", "Turkish"),
                        ],
                        default="1",
                        max_length=2,
                    ),
                ),
                (
                    "target_lang",
                    models.CharField(
                        choices=[
                            ("1", "English"),
                            ("2", "Ukrainian"),
                            ("3", "Russian"),
                            ("4", "German"),
                            ("5", "Polish"),
                            ("6", "Italian"),
                            ("7", "French"),
                            ("8", "Spanish"),
                            ("9", "Turkish"),
                        ],
                        default="3",
                        max_length=2,
                    ),
                ),
                ("source_text", models.CharField(max_length=200)),
                ("target_text", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("comment", models.CharField(blank=True, max_length=200)),
                ("translated_times", models.PositiveIntegerField()),
                ("not_translated_times", models.PositiveIntegerField()),
                (
                    "label",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="languages.languageslabel",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
