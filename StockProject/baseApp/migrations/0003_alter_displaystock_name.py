# Generated by Django 4.2.5 on 2024-01-22 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_displaystock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displaystock',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseApp.stock'),
        ),
    ]