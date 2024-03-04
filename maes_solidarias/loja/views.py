from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    return render(request, '../templates/loja/index.html', {'produtos': produtos})

def add_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the list of products
    else:
        form = ProdutoForm()
    return render(request, '../templates/loja/add.html', {'form': form})
