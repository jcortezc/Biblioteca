from django import forms
from .models import *


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'autor', 'editorial',)
        widgets = {
            'autor': forms.CheckboxSelectMultiple()
        }
