# Generated by Django 5.0 on 2024-07-30 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCH_Admin', '0006_offer_email_table_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_booking',
            name='available',
            field=models.CharField(choices=[('available', 'Available'), ('not available', 'Not Available')], default='available', max_length=20),
        ),
    ]
