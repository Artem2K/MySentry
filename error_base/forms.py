from django import forms

from .models import ErrorModel


class DateInput(forms.DateInput):
    input_type = 'date'


class AppListForm(forms.Form):
    type_search = forms.CharField(required=False)
    day_search = forms.DateField(required=False, widget=DateInput)

    class Meta:
        model = ErrorModel


class ErrorListForm(forms.Form):
    model = ErrorModel
    type_search = forms.CharField(required=False)


