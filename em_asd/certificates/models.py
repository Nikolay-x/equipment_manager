from django.db import models

from em_asd.pumps.models import Pump


# Create your models here.


class Certificate(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=30,
    )

    issue_date = models.DateField(
        verbose_name='Issuance Date',
    )

    expiry_date = models.DateField(
        verbose_name='Expiry Date',
        null=True,
        blank=True,
    )

    certificate_url = models.URLField(
        verbose_name='Certificate URL',
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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('expiry_date',)
