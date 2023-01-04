from django.db import models

from em_asd.pumps.models import Pump


# Create your models here.


class Manual(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=30,
    )

    manual_url = models.URLField(
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

    class Meta:
        ordering = ('pump',)
