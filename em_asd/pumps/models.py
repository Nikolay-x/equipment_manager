from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

# Create your models here.


UserModel = get_user_model()


class Pump(models.Model):
    Positive_displacement = 'Positive-displacement'
    Centrifugal = 'Centrifugal'
    Dosing = 'Dosing'
    Axial_flow = 'Axial-flow'
    Other = 'Other'

    PUMP_TYPES = (
        (Positive_displacement, Positive_displacement),
        (Centrifugal, Centrifugal),
        (Dosing, Dosing),
        (Axial_flow, Axial_flow),
        (Other, Other),
    )

    tag = models.CharField(
        verbose_name='Tag',
        max_length=30,
        unique=True,
    )

    name = models.CharField(
        verbose_name='Name',
        max_length=30,
    )

    type = models.CharField(
        verbose_name='Type',
        max_length=30,
        choices=PUMP_TYPES,
    )

    model = models.CharField(
        verbose_name='Model',
        max_length=30,
    )

    fluid = models.CharField(
        verbose_name='Fluid',
        max_length=30,
    )

    flow_rate = models.FloatField(
        verbose_name='Flow Rate (m3/h)',
        validators=(
            validators.MinValueValidator(0),
        ),
    )

    head = models.FloatField(
        verbose_name='Head (m)',
        validators=(
            validators.MinValueValidator(0),
        ),
    )

    power = models.FloatField(
        verbose_name='Power (kW)',
        validators=(
            validators.MinValueValidator(0),
        ),
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=True,
        blank=True,
    )

    favourites = models.ManyToManyField(
        UserModel,
        related_name='favourite',
        default=None,
        blank=True,
    )

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ('tag',)
