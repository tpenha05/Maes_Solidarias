from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return redirect('accounts/login/')

def home(request):
    return render(request, 'base.html')








