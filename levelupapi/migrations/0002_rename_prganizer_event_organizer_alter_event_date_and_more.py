# Generated by Django 4.0.4 on 2022-05-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='prganizer',
            new_name='organizer',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
