# Generated by Django 2.2 on 2019-04-21 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driverAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TravelHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_address', models.TextField()),
                ('destination_address', models.TextField()),
                ('booked_time', models.DateTimeField(auto_now_add=True)),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driverAPI.Driver')),
                ('passenger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passengerAPI.Passenger')),
            ],
        ),
    ]
