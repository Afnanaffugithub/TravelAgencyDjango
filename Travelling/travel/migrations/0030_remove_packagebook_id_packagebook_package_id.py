# Generated by Django 4.2.2 on 2023-06-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0029_alter_packagebook_package_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagebook',
            name='id',
        ),
        migrations.AddField(
            model_name='packagebook',
            name='package_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]