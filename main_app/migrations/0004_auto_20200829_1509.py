# Generated by Django 3.1 on 2020-08-29 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_pot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pot',
            old_name='locaation',
            new_name='location',
        ),
    ]