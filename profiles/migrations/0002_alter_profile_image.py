# Generated by Django 3.2.25 on 2024-05-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../pixavibe/default_profile_pbhpua.jpg', upload_to='images/'),
        ),
    ]
