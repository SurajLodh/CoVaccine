# Generated by Django 3.2 on 2021-05-04 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coregister', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Unique_id',
            new_name='uni',
        ),
    ]