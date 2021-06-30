# Generated by Django 3.2.4 on 2021-06-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0004_softwarespec_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='othermatters',
            name='laptopweight1',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='othermatters',
            name='laptopweight2',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='othermatters',
            name='manufacturer',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='othermatters',
            name='operating',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='othermatters',
            name='screensize',
            field=models.CharField(default=None, max_length=100),
        ),
    ]