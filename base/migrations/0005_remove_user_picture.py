# Generated by Django 4.0.6 on 2022-10-18 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='picture',
        ),
    ]