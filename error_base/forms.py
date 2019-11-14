from django import forms

from .models import ErrorModel


class AppListForm(forms.Form):
    model = ErrorModel
    type_search = forms.CharField(required=False)
    day_search = forms.DateField(required=False)


class ErrorListForm(forms.Form):
    model = ErrorModel
    type_search = forms.CharField(required=False)


