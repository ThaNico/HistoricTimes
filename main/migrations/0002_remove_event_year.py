# Generated by Django 4.0.6 on 2022-08-15 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='year',
        ),
    ]
