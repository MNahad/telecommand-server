# Generated by Django 2.0.7 on 2018-07-31 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configUp', '0002_auto_20180720_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='confirm_uplink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='config',
            name='date_uplink',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0)),
        ),
    ]
