# Generated by Django 4.1 on 2023-02-02 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_alter_roomcheckincustomers_unique_together'),
        ('orders', '0005_alter_orders_room_checkin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='room_checkin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.roomcheckins'),
        ),
    ]
