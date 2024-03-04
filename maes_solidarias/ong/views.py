from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doador

def index(request):
    return redirect('accounts/login/')

@login_required
def profile(request):
    doador = get_object_or_404(Doador, user=request.user)
    
    return render(request, 'profile.html', {'doador': doador})

@login_required
def create_profile(request):
    if request.method == 'POST':







