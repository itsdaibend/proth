# Generated by Django 4.0.4 on 2022-06-10 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoLabel",
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
            name="Todo",
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
                ("title", models.CharField(max_length=150)),
                ("memo", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("expired_at", models.DateTimeField(blank=True, null=True)),
                ("is_completed", models.BooleanField(default=False)),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("1", "LOW"),
                            ("2", "MEDIUM"),
                            ("3", "HIGH"),
                            ("4", "EXTRA HIGH"),
                        ],
                        default="2",
                        max_length=2,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "TODO"),
                            ("2", "IN PROGRESS"),
                            ("3", "ON HOLD"),
                            ("4", "COMPLETE"),
                        ],
                        default="1",
                        max_length=2,
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(
                        default=10,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todo.todolabel",
                    ),
                ),
            ],
        ),
    ]
