# Generated by Django 4.2 on 2023-06-07 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagebook',
            name='package_guestmember',
        ),
    ]
