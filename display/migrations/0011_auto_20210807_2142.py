# Generated by Django 3.2.6 on 2021-08-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0010_remove_medical_storesservice_medical_storesservice_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medical_storesservice',
            old_name='medical_storesservice_name',
            new_name='medical_stores_name',
        ),
        migrations.RenameField(
            model_name='medical_storesservice',
            old_name='medical_storesservice_state',
            new_name='medical_stores_state',
        ),
        migrations.AlterField(
            model_name='medical_storesservice',
            name='medical_storesservice_medicinetype',
            field=models.CharField(default='', max_length=120),
        ),
    ]
