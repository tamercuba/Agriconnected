from django                    import forms
from django.conf               import settings
from .models                   import Alien, State


class AlienForm(forms.ModelForm):
    city  = forms.CharField(label='Cidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ModelChoiceField(label='Estado',queryset=State.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model   = Alien
        fields  = ['city', 'state', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'text', 'id': 'datepicker'})
        }
