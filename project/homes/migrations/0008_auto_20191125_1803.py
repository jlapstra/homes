# Generated by Django 2.0.8 on 2019-11-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0007_auto_20191125_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='rentzestimate_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='rentzestimate_last_updated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='zestimate_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='zestimate_last_updated',
            field=models.DateField(blank=True, null=True),
        ),
    ]