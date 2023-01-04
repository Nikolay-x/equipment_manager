from django import forms

from em_asd.core.utils import DateInput
from em_asd.manuals.models import Manual


class ManualAddForm(forms.ModelForm):
    class Meta:
        model = Manual
        exclude = ('pump', )
        widgets = {
            'issue_date': DateInput(),
            'expiry_date': DateInput(),
        }


class ManualDeleteForm(ManualAddForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
