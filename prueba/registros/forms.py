from django import forms
from .models import ComentarioContactos

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContactos
        fields = ['usuario','mensaje']