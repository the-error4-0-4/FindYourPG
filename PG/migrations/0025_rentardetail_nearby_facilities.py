# Generated by Django 4.1.5 on 2023-02-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PG', '0024_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentardetail',
            name='nearby_facilities',
            field=models.TextField(default=''),
        ),
    ]
