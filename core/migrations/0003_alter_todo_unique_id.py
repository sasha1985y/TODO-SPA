# Generated by Django 5.1 on 2024-08-09 20:10

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todo_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='unique_id',
            field=models.CharField(default=core.models.generate_unique_id, max_length=32, unique=True),
        ),
    ]
