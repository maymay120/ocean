# Generated by Django 4.0.3 on 2022-04-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oceanapp', '0015_alter_profile_file2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='price',
        ),
        migrations.AddField(
            model_name='history',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]