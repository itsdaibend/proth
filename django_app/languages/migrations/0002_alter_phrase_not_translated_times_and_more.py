# Generated by Django 4.0.4 on 2022-07-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("languages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phrase",
            name="not_translated_times",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="phrase",
            name="translated_times",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
