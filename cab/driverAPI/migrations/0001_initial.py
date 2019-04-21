# Generated by Django 2.2 on 2019-04-21 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('number', models.IntegerField(unique=True)),
                ('license', models.CharField(max_length=80, unique=True)),
                ('car_no', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DriverLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='DriverRidesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_address', models.TextField()),
                ('destination_address', models.TextField()),
                ('booked_time', models.DateTimeField(auto_now_add=True)),
                ('car_no', models.CharField(max_length=80, unique=True)),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driverAPI.Driver')),
            ],
        ),
    ]