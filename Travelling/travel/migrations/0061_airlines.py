# Generated by Django 4.2.2 on 2023-07-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0060_tobuscity_price_totrcity_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=50)),
            ],
        ),
    ]
