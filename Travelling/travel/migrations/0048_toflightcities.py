# Generated by Django 4.2.2 on 2023-06-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0047_rename_cities_flightcities'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToFlightCities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City_name', models.CharField(max_length=50)),
            ],
        ),
    ]
