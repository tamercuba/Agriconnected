from django       import forms
#from django.forms import extras
from django.conf  import settings
from .models      import Alien, State



class AlienForm(forms.ModelForm):
    city  = forms.CharField(label='Cidade')
    state = forms.ModelChoiceField(label='Estado',queryset=State.objects.all())
    date  = forms.DateInput(attrs={'class':'datepicker'})

    class Meta:
        model  = Alien

        fields = '__all__'
