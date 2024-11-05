# Generated by Django 5.1.1 on 2024-10-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home1', '0003_alter_user_wedsite_managers_user_wedsite_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_wedsite',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='user_wedsite_set', to='auth.group'),
        ),
        migrations.AddField(
            model_name='user_wedsite',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='user_wedsite_permissions', to='auth.permission'),
        ),
    ]
