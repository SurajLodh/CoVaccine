# Generated by Django 3.2 on 2021-05-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coregister', '0005_auto_20210504_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
