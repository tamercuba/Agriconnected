from django.shortcuts import render
from django.http      import HttpResponse
from .forms           import AlienForm

def home(request):
    template_name = 'home.html'
    if request.method == 'POST':
        form = AlienForm(request.POST)
        if form.is_valid():
            form.save()

    form    = AlienForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
