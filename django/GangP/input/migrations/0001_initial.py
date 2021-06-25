# Generated by Django 3.2.4 on 2021-06-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChoosenSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.CharField(default=None, max_length=100)),
                ('vga', models.CharField(default=None, max_length=100)),
                ('ram', models.IntegerField(default=None)),
                ('hdd', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('version', models.IntegerField(default=0)),
                ('cpu', models.CharField(max_length=100)),
                ('vga', models.CharField(max_length=100)),
                ('ram', models.IntegerField()),
                ('hdd', models.IntegerField()),
            ],
        ),
    ]