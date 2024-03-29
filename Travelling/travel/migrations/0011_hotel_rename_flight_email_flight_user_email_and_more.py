# Generated by Django 4.2.2 on 2023-06-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_fname', models.CharField(max_length=50)),
                ('hotel_lname', models.CharField(max_length=50)),
                ('hotel_mobNo', models.CharField(max_length=10, unique=True)),
                ('hotel_email', models.EmailField(max_length=254)),
                ('hotel_numberpdeople', models.IntegerField(default=1)),
                ('hotel_identitytype', models.CharField(max_length=50)),
                ('hotel_identityno', models.CharField(max_length=50)),
                ('hotel_state', models.CharField(max_length=50)),
                ('hotel_city', models.CharField(max_length=50)),
                ('hotel_roomtype', models.CharField(max_length=50)),
                ('hotel_hoteltype', models.CharField(max_length=50)),
                ('hotel_checkin', models.DateTimeField(auto_now_add=True)),
                ('hotel_checkout', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='flight_email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='flight_fname',
            new_name='user_fname',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='flight_identityno',
            new_name='user_identityno',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='flight_identitytype',
            new_name='user_identitytype',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='flight_mobNo',
            new_name='user_mobNo',
        ),
        migrations.RenameField(
            model_name='train',
            old_name='train_age',
            new_name='user_age',
        ),
        migrations.RenameField(
            model_name='train',
            old_name='train_email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='train',
            old_name='train_identityno',
            new_name='user_identityno',
        ),
        migrations.RenameField(
            model_name='train',
            old_name='train_identitytype',
            new_name='user_identitytype',
        ),
        migrations.RenameField(
            model_name='train',
            old_name='train_mobNo',
            new_name='user_mobNo',
        ),
        migrations.RemoveField(
            model_name='train',
            name='train_tname',
        ),
        migrations.AddField(
            model_name='bus',
            name='user_age',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bus',
            name='user_email',
            field=models.EmailField(default='afnan@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='bus',
            name='user_identityno',
            field=models.CharField(default='afnan', max_length=50),
        ),
        migrations.AddField(
            model_name='bus',
            name='user_identitytype',
            field=models.CharField(default='afnan', max_length=50),
        ),
        migrations.AddField(
            model_name='bus',
            name='user_mobNo',
            field=models.CharField(default='afnan', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='bus',
            name='user_name',
            field=models.CharField(default='afnan', max_length=50),
        ),
        migrations.AddField(
            model_name='train',
            name='user_name',
            field=models.CharField(default='affu', max_length=50),
        ),
    ]
