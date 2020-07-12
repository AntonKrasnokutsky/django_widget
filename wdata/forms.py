from django import forms
from .models import SelectDateTime


class SelectDateTimeForm(forms.Form):
    date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    time = forms.TimeField(
        input_formats=['%H:%M'],
        widget=forms.TimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        })
    )
