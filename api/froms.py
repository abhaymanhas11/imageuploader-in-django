from django import forms
from .models import imageuploader


class imageform(forms.ModelForm):
    class Meta:
        model=imageuploader
        fields='__all__'
        labels={'image':''}