# Generated by Django 5.0.2 on 2024-07-23 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderbracelet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='order.order'),
        ),
        migrations.DeleteModel(
            name='OrderBracelet',
        ),
    ]
