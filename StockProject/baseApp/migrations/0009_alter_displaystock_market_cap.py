# Generated by Django 4.2.5 on 2024-02-02 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0008_alter_stock_bse_code_alter_stock_nse_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displaystock',
            name='market_cap',
            field=models.FloatField(),
        ),
    ]
