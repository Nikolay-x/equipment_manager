from django import forms

from em_asd.core.utils import DateInput
from em_asd.m_activities.models import Activity


class ActivityAddForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ('pump', )
        widgets = {
            'due_date': DateInput(),
        }
