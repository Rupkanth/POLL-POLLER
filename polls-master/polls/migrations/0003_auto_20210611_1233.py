# Generated by Django 3.0.7 on 2021-06-11 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210610_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votedby',
            name='polledOpt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.PollsOptions'),
        ),
    ]
