from django.contrib import admin

from em_asd.pumps.models import Pump


# Register your models here.


@admin.register(Pump)
class PumpAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name', 'type', 'model', 'fluid', 'flow_rate', 'head', 'power', 'image_url')
    list_filter = ('tag',)
    search_fields = ('tag', 'fluid')
