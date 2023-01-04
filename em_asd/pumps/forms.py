from django import forms

from em_asd.pumps.models import Pump


class PumpAddForm(forms.ModelForm):
    class Meta:
        model = Pump
        exclude = ('favourites',)


class PumpDeleteForm(PumpAddForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
