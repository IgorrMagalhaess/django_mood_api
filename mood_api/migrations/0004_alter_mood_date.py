# Generated by Django 5.0.6 on 2024-05-23 20:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_api', '0003_alter_mood_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
