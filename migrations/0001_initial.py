# Generated by Django 2.2.17 on 2020-12-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('Resident_Name', models.CharField(max_length=50)),
                ('House_Number', models.CharField(max_length=100)),
                ('Resident_Vehicle_Number', models.CharField(max_length=15)),
                ('Resident_Vehicle_Key', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
    ]
