# Generated by Django 4.0.4 on 2022-05-25 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial_models_todo_and_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', 'LOW'), ('2', 'MEDIUM'), ('3', 'HIGH'), ('4', 'EXTRA HIGH')], default='2', max_length=2),
        ),
    ]
