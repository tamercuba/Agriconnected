from django       import forms
#from django.forms import extras
from django.conf  import settings
from .models      import Alien, State



class AlienForm(forms.ModelForm):

    class Meta:
        model   = Alien
        fields  = ['city', 'state', 'date']
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})} 
