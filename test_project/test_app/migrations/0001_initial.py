# Generated by Django 4.2.2 on 2023-06-11 15:00

import dj3nk.nk_model
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(default=dj3nk.nk_model.gnk, primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
