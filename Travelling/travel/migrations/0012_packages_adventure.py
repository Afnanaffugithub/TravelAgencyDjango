# Generated by Django 4.2.2 on 2023-06-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0011_hotel_rename_flight_email_flight_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='adventure',
            field=models.BooleanField(default=False),
        ),
    ]
