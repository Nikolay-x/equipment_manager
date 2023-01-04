from django import forms

from em_asd.certificates.models import Certificate
from em_asd.core.utils import DateInput


class CertificateAddForm(forms.ModelForm):
    class Meta:
        model = Certificate
        exclude = ('pump',)
        widgets = {
            'issue_date': DateInput(),
            'expiry_date': DateInput(),
        }


class CertificateDeleteForm(CertificateAddForm):
    disabled_attr_name = 'disabled'
    readonly_attr_name = 'readonly'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs[self.disabled_attr_name] = self.disabled_attr_name
            field.widget.attrs[self.readonly_attr_name] = self.readonly_attr_name
