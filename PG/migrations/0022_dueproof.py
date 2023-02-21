# Generated by Django 4.1.5 on 2023-02-21 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PG', '0021_booking_remaining_due'),
    ]

    operations = [
        migrations.CreateModel(
            name='dueProof',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='room/dueproof')),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PG.booking')),
            ],
        ),
    ]