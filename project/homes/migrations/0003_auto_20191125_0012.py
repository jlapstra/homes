# Generated by Django 2.0.8 on 2019-11-25 00:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0002_home_zestimate_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='address',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='home',
            name='area_unit',
            field=models.CharField(choices=[('SqFt', 'Square Foot'), ('SqM', 'Square Meter')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='bedrooms',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='city',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='home',
            name='home_type',
            field=models.CharField(choices=[('SingleFamily', 'Single Family'), ('VacantResidentialLand', 'Vacant Residential Land'), ('Miscellaneous', 'Miscellaneous'), ('MultiFamily2To4', 'Muliple Family (2 to 4)'), ('Condominium', 'Condominium'), ('Apartment', 'Apartment'), ('Duplex', 'Duplex')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='home',
            name='price',
            field=models.CharField(default='', max_length=20, validators=[django.core.validators.RegexValidator('^\\$(\\d*\\.?\\d{0,2})[KM]$', 'Your string should be in the format: $###.##M or $###K')]),
        ),
        migrations.AlterField(
            model_name='home',
            name='state',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='home',
            name='zipcode',
            field=models.CharField(default='', max_length=20),
        ),
    ]