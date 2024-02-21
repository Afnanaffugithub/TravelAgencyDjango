# Generated by Django 4.2.2 on 2023-06-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0025_vehicles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='timings',
            field=models.CharField(choices=[('0', ''), ('1', 'Morning'), ('2', 'Evening'), ('3', 'AfterNoon')], default=0, max_length=50),
        ),
    ]