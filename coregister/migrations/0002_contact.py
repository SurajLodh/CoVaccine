# Generated by Django 3.2 on 2021-05-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coregister', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unique_id', models.TextField()),
                ('name', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.TextField()),
                ('query', models.TextField()),
            ],
        ),
    ]
