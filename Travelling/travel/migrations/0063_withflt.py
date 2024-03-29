# Generated by Django 4.2.2 on 2023-07-31 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0062_remove_flight_flight_adate_flight_flight_arival'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withflt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_image', models.ImageField(upload_to='images')),
                ('airline', models.CharField(max_length=50)),
                ('fromtoto', models.CharField(choices=[('0', ''), ('1', 'Morning'), ('2', 'Evening'), ('3', 'Night')], default=0, max_length=50)),
                ('Baggage', models.CharField(max_length=50)),
                ('Baggagechek', models.CharField(max_length=50)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.packages')),
            ],
        ),
    ]
