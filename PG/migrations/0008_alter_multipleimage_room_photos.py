# Generated by Django 4.1.5 on 2023-02-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PG', '0007_alter_multipleimage_room_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimage',
            name='room_photos',
            field=models.ImageField(default='', upload_to='room/photo'),
        ),
    ]