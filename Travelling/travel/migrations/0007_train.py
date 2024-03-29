# Generated by Django 4.2.2 on 2023-06-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_packages'),
    ]

    operations = [
        migrations.CreateModel(
            name='train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_jfrom', models.CharField(max_length=50)),
                ('train_jto', models.CharField(max_length=50)),
                ('train_date', models.DateField(auto_now_add=True)),
                ('train_time', models.TimeField(auto_now_add=True)),
                ('train_reservation', models.CharField(max_length=50)),
                ('train_passengers', models.IntegerField()),
                ('train_tname', models.CharField(max_length=50)),
                ('train_age', models.IntegerField()),
                ('train_mobNo', models.CharField(max_length=10, unique=True)),
                ('train_email', models.EmailField(max_length=254)),
                ('train_identitytype', models.CharField(max_length=50)),
                ('train_identityno', models.CharField(max_length=50)),
            ],
        ),
    ]
