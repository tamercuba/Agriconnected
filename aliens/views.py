from django.shortcuts import render, redirect, render_to_response
from django.http      import HttpResponse
from .forms           import AlienForm
from .models          import Alien, State

def home(request):
    return render(request, template_name='home.html')

def register(request):
    template_name = 'register.html'
    form = AlienForm(request.POST or None)
    if form.is_valid():
        salvar = form.save(commit=False)
        salvar.save()
        return redirect('aliens:home')
    else:
        context = {
            'form': form
        }
        return render(request, template_name, context)


def aliens_list(request):
    template_name = 'list.html'
    aliens = Alien.objects.all()


    context = {
        'aliens': aliens
    }
    return render(request, template_name, context)

def alien_counter(request):
    template_name = 'counter.html'
    states = State.objects.all().exclude(count=0)
    context = {
        'states': states
    }
    return render(request, template_name, context)
