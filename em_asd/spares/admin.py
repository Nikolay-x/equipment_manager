from django.contrib import admin

from em_asd.spares.models import Spares


# Register your models here.


@admin.register(Spares)
class SparesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ref_doc_code', 'location', 'quantity', 'pump')
    list_filter = ('name', 'ref_doc_code',)
    search_fields = ('name', 'ref_doc_code')
