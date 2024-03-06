from django.shortcuts import render, redirect
from .forms import DonationForm

def donation_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            # Processamento após o formulário ser válido
            form.save()
            return redirect('algum_lugar')  # Redireciona após processar o formulário
    else:
        form = DonationForm()

    context = {'form': form}  # Certifique-se de que isso é um dicionário
    return render(request, '../templates/donations/donate.html', context)
