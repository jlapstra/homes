# Generated by Django 2.0.8 on 2019-11-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0004_auto_20191125_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='last_sold_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]