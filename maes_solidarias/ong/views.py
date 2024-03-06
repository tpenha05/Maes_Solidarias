from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CampanhaForm, EventoForm

def index(request):
    return redirect('accounts/login/')

def home(request):
    return render(request, 'base.html')

def add_campanha(request):
    if request.method == 'POST':
        form = CampanhaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = CampanhaForm()
    return render(request, 'ong/add_campanha.html', {'form': form})

def add_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = EventoForm()
    return render(request, 'ong/add_evento.html', {'form': form})







