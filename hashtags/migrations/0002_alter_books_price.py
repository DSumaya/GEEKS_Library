# Generated by Django 5.1.4 on 2025-01-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
