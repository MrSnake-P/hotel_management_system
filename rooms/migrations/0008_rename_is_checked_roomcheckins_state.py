# Generated by Django 4.1 on 2023-02-02 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_alter_roomcheckincustomers_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomcheckins',
            old_name='is_checked',
            new_name='state',
        ),
    ]
