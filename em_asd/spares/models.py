from django.db import models

from em_asd.pumps.models import Pump


# Create your models here.


class Spares(models.Model):
    SHELF0101 = 'Shelf 01-01'
    SHELF0102 = 'Shelf 01-02'
    SHELF0103 = 'Shelf 01-03'
    SHELF0201 = 'Shelf 02-01'
    SHELF0202 = 'Shelf 02-02'
    SHELF0203 = 'Shelf 02-03'

    LOCATIONS = (
        (SHELF0101, SHELF0101),
        (SHELF0102, SHELF0102),
        (SHELF0103, SHELF0103),
        (SHELF0201, SHELF0201),
        (SHELF0202, SHELF0202),
        (SHELF0203, SHELF0203),
    )

    name = models.CharField(
        verbose_name='Name',
        max_length=30,
    )

    ref_doc_code = models.CharField(
        verbose_name='Ref Document Code',
        max_length=30,
    )

    location = models.CharField(
        verbose_name='Location',
        max_length=30,
        choices=LOCATIONS,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Quantity',
    )

    pump = models.ForeignKey(
        Pump,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    @property
    def pump_tag(self):
        return self.pump.tag

    class Meta:
        ordering = ('ref_doc_code',)
        verbose_name_plural = 'Spares'
