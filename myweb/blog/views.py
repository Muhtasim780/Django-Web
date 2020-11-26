from django.shortcuts import render
from .models import Product


def home(request):
    Products = Product.objects.all()
    context = {
        'Products': Product.objects.all()
    }
    return render(request, 'blog/home.html', context, {'title': 'Home'})


def new(request):
    return render(request, 'blog/new.html', {'title': 'About'})