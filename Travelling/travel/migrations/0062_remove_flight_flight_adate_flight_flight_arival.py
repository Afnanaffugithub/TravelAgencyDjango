# Generated by Django 4.2.2 on 2023-07-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0061_airlines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='flight_adate',
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_arival',
            field=models.CharField(default='No selected', max_length=50),
        ),
    ]
