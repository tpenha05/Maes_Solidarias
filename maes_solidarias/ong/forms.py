from django import forms
from .models import Campanha, Evento

class CampanhaForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = ['nome', 'descricao', 'data_e_horario', 'local', 'publico_destinado']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'data_e_horario', 'local', 'publico_destinado']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5}),
        }
        