from django.shortcuts import render, redirect, render_to_response
from django.http      import HttpResponse
from .forms           import AlienForm

def home(request):
    template_name = 'home.html'
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
