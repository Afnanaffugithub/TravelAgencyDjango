# Generated by Django 4.2.2 on 2023-07-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0059_toflightcities_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='tobuscity',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='totrcity',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
