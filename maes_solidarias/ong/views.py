from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doador

def index(request):
    return render(request, 'base.html')

@login_required
def profile(request):
    doador = get_object_or_404(Doador, user=request.user)
    
    return render(request, 'profile.html', {'doador': doador})

@login_required
def create_profile(request):
    if request.method == 'POST':

        nome_completo = request.POST.get('Nome_completo')
        cpf = request.POST.get('cpf')
        genero = request.POST.get('genero')
        whatsapp = request.POST.get('whatsapp')
        foto_perfil = request.FILES.get('foto_perfil')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        forma_de_doacao =  request.POST.get('forma_de_doacao')
        periodicidade_doacao =  request.POST.get('periodicidade_doacao')
        valor_doacao =  request.POST.get('valor_doacao')

        doador = Doador(user= request.user, nome_completo=nome_completo, cpf=cpf, genero=genero, whatsapp=whatsapp, data_nascimento=data_nascimento, email=email, forma_de_doacao=forma_de_doacao,periodicidade_doacao=periodicidade_doacao,valor_doacao=valor_doacao)

        doador.save()

        return render(request, 'create_profile.html', {'doador': doador})



