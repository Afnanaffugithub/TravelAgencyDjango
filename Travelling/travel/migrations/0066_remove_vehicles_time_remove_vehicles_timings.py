# Generated by Django 4.2.2 on 2023-07-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0065_delete_withflt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicles',
            name='time',
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='timings',
        ),
    ]
