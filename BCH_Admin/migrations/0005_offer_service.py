# Generated by Django 5.0 on 2024-07-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCH_Admin', '0004_remove_coldcoffee_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percent', models.IntegerField()),
                ('descriptions', models.CharField(max_length=200)),
                ('offer_starting_time', models.CharField(max_length=200)),
            ],
        ),
    ]
