# Generated by Django 4.2.5 on 2024-01-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0006_remove_displaystock_pre_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displaystock',
            name='current_price',
            field=models.FloatField(),
        ),
    ]
