# Generated by Django 3.0.7 on 2021-06-13 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_commentby_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votedby',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
