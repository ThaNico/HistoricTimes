# Generated by Django 4.0.6 on 2022-08-13 08:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1500)])),
                ('label', models.CharField(max_length=128)),
                ('source', models.URLField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'On hold'), (1, 'Valid')], default=0)),
            ],
        ),
    ]
