# Generated by Django 4.2.2 on 2023-07-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0056_alter_bus_user_name_alter_cab_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='package_slug',
            field=models.SlugField(),
        ),
    ]