# Generated by Django 2.0.7 on 2018-07-16 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='deparment',
            new_name='department',
        ),
    ]
