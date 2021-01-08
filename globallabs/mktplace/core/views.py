from .models import Product
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.views.generic.list import ListView

'''
from django.views.generic import TemplateView
from django.views.generic.base import View


class IndexTemplateView(TemplateView):
    template_name = "index.html"

def listar_material(request):

    #evento = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual)
    #dados = {'eventos': evento}
    #return render(request, 'agenda.html', dados)

    material = Material.objects.all()
    return render(request, 'products-form.html', {'materiais': material})

'''


def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request,'products-form.html', {'form': form})


def update_products(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request, 'products-form.html', {'form': form, 'product': product})


def delete_products(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    return render(request, 'prod-delete-confirm.html', {'product': product})


class MaterialListView(ListView):
    template_name = 'test.html'
    model = Product
    context_object_name = 'allproducts'

# Create your views here.
