# Generated by Django 5.0.2 on 2024-06-02 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_contact_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutimage',
            options={'ordering': ['sort'], 'verbose_name': 'About Us Image', 'verbose_name_plural': 'About Us Images'},
        ),
        migrations.AddField(
            model_name='aboutimage',
            name='sort',
            field=models.IntegerField(default=0, verbose_name='Sort'),
        ),
    ]