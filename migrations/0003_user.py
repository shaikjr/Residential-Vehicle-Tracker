# Generated by Django 2.2.17 on 2020-12-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_Name', models.CharField(max_length=50)),
                ('User_Id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('User_Pass', models.CharField(max_length=10)),
            ],
        ),
    ]