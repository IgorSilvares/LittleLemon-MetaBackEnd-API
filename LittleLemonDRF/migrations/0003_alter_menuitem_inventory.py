# Generated by Django 4.2.3 on 2023-07-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0002_menuitem_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='inventory',
            field=models.SmallIntegerField(),
        ),
    ]