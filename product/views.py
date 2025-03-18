from django.shortcuts import render
import requests

def product_list(request):
    products = requests.get('https://boykot.kg/api/v1/products/').json()
    return render(request, 'product/product_list.html', {'products': products})

