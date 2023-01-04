from django.db import models

from em_asd.pumps.models import Pump


# Create your models here.


class Activity(models.Model):
    Open = 'Open'
    Close = 'Close'

    STATUSES = (
        (Open, Open),
        (Close, Close),
    )

    description = models.TextField(
        verbose_name='Description',
    )

    due_date = models.DateField(
        verbose_name='Due Date',
    )

    status = models.CharField(
        verbose_name='Status',
        max_length=30,
        choices=STATUSES,
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
        ordering = ('due_date',)
        verbose_name_plural = 'Activities'
