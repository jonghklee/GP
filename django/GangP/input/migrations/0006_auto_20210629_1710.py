# Generated by Django 3.2.4 on 2021-06-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0005_auto_20210627_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='othermatters',
            name='laptopweight2',
        ),
        migrations.AlterField(
            model_name='othermatters',
            name='laptopweight1',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
