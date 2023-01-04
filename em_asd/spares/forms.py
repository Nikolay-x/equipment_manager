from django import forms

from em_asd.spares.models import Spares


class SparesAddForm(forms.ModelForm):
    class Meta:
        model = Spares
        exclude = ('pump', )
