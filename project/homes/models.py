from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, RegexValidator

price_validator = RegexValidator(
        r"^\$(\d*\.?\d{0,2})[KM]$",
        "Your string should be in the format: $###.##M or $###K"
)

bathroom_validator = RegexValidator(
        r"\d*(\.5)?$",
        "You can only have whole and half baths."
)

AREA_UNITS = (
    ('SqFt', 'Square Foot'),
    ('SqM', 'Square Meter'),
)

HOME_TYPES = (
    ('SingleFamily', 'Single Family'),
    ('VacantResidentialLand', 'Vacant Residential Land'),
    ('Miscellaneous', 'Miscellaneous'),
    ('MultiFamily2To4', 'Muliple Family (2 to 4)'),
    ('Condominium', 'Condominium'),
    ('Apartment', 'Apartment'),
    ('Duplex', 'Duplex'),
)


class Home(models.Model):
    """
        A model to display and store information on a specific home type
    """

    zillow_id = models.PositiveIntegerField(unique=True, primary_key=True)

    home_size = models.PositiveIntegerField(blank=True, null=True)
    zestimate_amount = models.PositiveIntegerField(blank=True, null=True)
    rentzestimate_amount = models.PositiveIntegerField(blank=True, null=True)
    last_sold_price = models.PositiveIntegerField(blank=True, null=True)
    rent_price = models.PositiveIntegerField(blank=True, null=True)
    property_size = models.PositiveIntegerField(blank=True, null=True)

    bedrooms = models.PositiveSmallIntegerField(blank=True, null=True)

    rentzestimate_last_updated = models.DateField(blank=True, null=True)
    zestimate_last_updated = models.DateField(blank=True, null=True)
    last_sold_date = models.DateField(blank=True, null=True)

    link = models.URLField(blank=True)

    area_unit = models.CharField(max_length=20, choices=AREA_UNITS, default='')
    home_type = models.CharField(max_length=30, choices=HOME_TYPES, default='')

    price = models.CharField(max_length=20, validators=[price_validator], default='')
    address = models.CharField(max_length=300, default='')
    city = models.CharField(max_length=300, default='')
    state = models.CharField(max_length=2, default='')
    zipcode = models.CharField(max_length=20, default='')

    tax_value = models.DecimalField(
                    max_digits=10,
                    decimal_places=1,
                    validators=[MinValueValidator(Decimal('0.0'))],
                    blank=True,
                    null=True
    )
    bathrooms = models.DecimalField(
                    max_digits=4,
                    decimal_places=1,
                    validators=[
                            MinValueValidator(Decimal('0.5')),
                            bathroom_validator
                        ],
                    null=True
                    )
    tax_year = models.DecimalField(
                    max_digits=4,
                    decimal_places=0,
                    validators=[MinValueValidator(1800)],
                    null=True
                    )
    year_built = models.DecimalField(
                    max_digits=4,
                    decimal_places=0,
                    validators=[MinValueValidator(1800)],
                    null=True
                    )
