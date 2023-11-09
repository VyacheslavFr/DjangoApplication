from django.shortcuts import render
from myapp.models import Products
import json


def index_view(request):
    with open('myapp/fixtures/parser.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
    products = Products.objects.all()

    context = {
        'header': 'Привет, мир!',
        'table': products,
        'data': data
    }
    return render(request, 'index.html', context)
