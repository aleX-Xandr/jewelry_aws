# Generated by Django 5.0.2 on 2024-07-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_productimage_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_constructor',
        ),
        migrations.AddField(
            model_name='category',
            name='is_bracelet',
            field=models.BooleanField(default=False, verbose_name='Bracelet?'),
        ),
        migrations.AddField(
            model_name='category',
            name='is_coulomb',
            field=models.BooleanField(default=False, verbose_name='Coulomb?'),
        ),
    ]
