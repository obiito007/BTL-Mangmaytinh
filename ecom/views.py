# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Type, Product
from .forms import TimkiemForm,dangnhapForm
from django.views.generic import ListView,DetailView

# Create your views here.
def index(request):
    type_objs = Type.objects.filter(active__exact=True)
    paginate_by = 1
    context = {
        'type_objs': type_objs,
        'paginate_by': paginate_by,
    }
    return render(request, "ecom/type.html", context)
    
def product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'ecom/product.html', {'product': product})
    
def register(request):
    form = dangnhapForm()
    if request.method == 'POST':
        form = dangnhapForm(request.POST)
        if form.is_valid():
            form=form.save()
            return HttpResponseRedirect('/')
    return render(request,'ecom/register.html',{'form':form})

def index1(request):
    return render(request,'ecom/index.html')