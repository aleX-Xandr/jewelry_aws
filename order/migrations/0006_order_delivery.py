# Generated by Django 5.0.2 on 2024-09-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.BooleanField(blank=True, default=False, verbose_name='Delivery'),
        ),
    ]
