# Generated by Django 5.1.1 on 2024-10-16 11:17

import home1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user_wedsite',
            managers=[
                ('objects', home1.models.User_wedsiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='user_wedsite',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user_wedsite',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
