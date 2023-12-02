from django import forms
from .models import Audio_store

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio_store
        fields = ['record']