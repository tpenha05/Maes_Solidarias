from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    return redirect('accounts/login/')
