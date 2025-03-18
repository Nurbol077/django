from django.shortcuts import render
import requests

def product_list(request):
    page = request.GET.get('page', 1)
    data= requests.get(f'https://boykot.kg/api/v1/products/?page={page}').json()
    products = data.get('results', [])
    return render(request, 'product/product_list.html', {'products': products})

