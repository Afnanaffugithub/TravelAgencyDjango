# Generated by Django 4.2.2 on 2023-06-27 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0046_cities'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cities',
            new_name='FlightCities',
        ),
    ]