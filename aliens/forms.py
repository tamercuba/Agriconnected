from django       import forms
#from django.forms import extras
from django.conf  import settings
from .models      import Alien, State


YEARS = [x for x in range(1901,2019)]
class AlienForm(forms.ModelForm):
    city  = forms.CharField(label='Cidade', max_length=50)
    state = forms.ModelChoiceField(label='Estado',queryset=State.objects.all(), widget=forms.Select)
    date  = forms.DateField(required=True, widget=forms.SelectDateWidget)


    class Meta:
        model  = Alien
        fields = '__all__'
