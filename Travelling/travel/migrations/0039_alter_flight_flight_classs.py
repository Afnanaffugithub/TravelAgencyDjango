# Generated by Django 4.2.2 on 2023-06-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0038_tarinclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_classs',
            field=models.IntegerField(),
        ),
    ]