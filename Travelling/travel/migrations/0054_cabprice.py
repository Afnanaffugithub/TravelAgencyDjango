# Generated by Django 4.2.2 on 2023-06-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0053_fromcabcity_tocabcity_cab_cars_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CabPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_Price', models.CharField(max_length=50)),
            ],
        ),
    ]
