# Generated by Django 4.2.2 on 2023-06-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0051_fromtrcity_totrcity'),
    ]

    operations = [
        migrations.CreateModel(
            name='FromBuscity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ToBuscity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City_name', models.CharField(max_length=50)),
            ],
        ),
    ]
