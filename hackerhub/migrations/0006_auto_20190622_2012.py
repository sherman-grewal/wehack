# Generated by Django 2.2.1 on 2019-06-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerhub', '0005_hackathon_eventid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='participants',
            field=models.ManyToManyField(blank=True, to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, to='accounts.Profile'),
        ),
    ]
