# Generated by Django 5.0.2 on 2024-05-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_aboutimage_alter_page_meta_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='text',
            field=models.TextField(blank=True, default='', verbose_name='Text'),
        ),
    ]
