# Generated by Django 4.2.2 on 2023-06-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0044_busclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='bus_class',
            field=models.CharField(max_length=50),
        ),
    ]
