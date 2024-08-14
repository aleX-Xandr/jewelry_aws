# Generated by Django 5.0.2 on 2024-08-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_address_order_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('waiting', 'Waiting'), ('success', 'Success'), ('cancel', 'Cancel')], default='waiting', max_length=10, verbose_name='Status'),
        ),
    ]