# Generated by Django 3.1.4 on 2021-10-01 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20211001_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 10, 1, 18, 30, 42, 715373)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_upto',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 10, 1, 19, 30, 42, 715373)),
        ),
    ]
