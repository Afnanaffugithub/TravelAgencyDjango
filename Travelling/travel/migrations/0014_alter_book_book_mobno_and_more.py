# Generated by Django 4.2.2 on 2023-06-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_alter_book_book_name_alter_packagebook_package_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_mobNo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='packagebook',
            name='package_mobNo',
            field=models.CharField(max_length=10),
        ),
    ]
