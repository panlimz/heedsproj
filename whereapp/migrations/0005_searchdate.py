# Generated by Django 4.0.1 on 2022-01-08 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whereapp', '0004_remove_search_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Searchdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchdate', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
