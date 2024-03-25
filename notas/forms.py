from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):

    titulo = forms.CharField(label='Mi texto personalizado', widget=forms.TextInput(attrs={'class': 'form-titulo'}))
    descripcion = forms.CharField(label='Mi texto personalizado', widget=forms.Textarea(attrs={'class': 'form-des'}))

    class Meta:
        model = Nota
        fields = ["titulo", "descripcion"]