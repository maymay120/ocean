# Generated by Django 4.0.3 on 2022-04-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oceanapp', '0014_alter_profile_file_alter_profile_file2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
