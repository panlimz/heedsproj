# Generated by Django 4.0.1 on 2022-01-07 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whereapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
