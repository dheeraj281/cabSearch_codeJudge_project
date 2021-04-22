# Generated by Django 2.2.20 on 2021-04-16 16:18

from django.db import migrations, models
import django.db.models.deletion
import restapi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('phone', models.IntegerField(unique=True, validators=[restapi.models.validate_digit_length])),
                ('liscence', models.CharField(max_length=30, unique=True)),
                ('carNumber', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DriverLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.DecimalField(decimal_places=6, max_digits=15)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=15)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Driver')),
            ],
        ),
    ]