# Generated by Django 5.0 on 2024-07-30 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BCH_Admin', '0007_table_booking_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table_booking',
            old_name='available',
            new_name='check_table',
        ),
    ]
