# Generated by Django 4.0.6 on 2022-10-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=80, unique=True),
        ),
    ]