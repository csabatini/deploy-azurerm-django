from django import forms
from .models import JSONFile


class JSONFileForm(forms.Form):
    filetype = forms.ModelChoiceField(queryset=JSONFile.objects.values_list('type', flat=True).distinct())
    file = forms.FileField(
        label='File type:'
    )