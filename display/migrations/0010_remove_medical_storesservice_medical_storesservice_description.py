# Generated by Django 3.2.6 on 2021-08-07 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0009_auto_20210807_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medical_storesservice',
            name='medical_storesservice_description',
        ),
    ]
