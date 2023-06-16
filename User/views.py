from django.shortcuts import render
from Products.models import *
# Create your views here.

def home(request):
    products = Products.objects.all()
    for product in products:
        unique_colors = product.variants.values_list('color__color_code', flat=True).distinct()
        product.unique_colors = unique_colors
        print(unique_colors)
    context = {
        'products': products
    }
    return render(request,'home.html',context)