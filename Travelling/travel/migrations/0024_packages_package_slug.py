# Generated by Django 4.2.2 on 2023-06-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0023_alter_cab_cab_departuredate_alter_cab_cab_pickuptime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='package_slug',
            field=models.SlugField(default='cagh'),
        ),
    ]
