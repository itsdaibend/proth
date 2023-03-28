# Generated by Django 4.0.4 on 2022-07-07 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="label",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="todo.todolabel",
            ),
        ),
    ]
