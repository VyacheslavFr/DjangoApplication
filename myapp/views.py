from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Products
import json


def created_products_view(request):
    products = Products.objects.all()

    context = {
        'table': products
    }
    return render(request, 'index.html', context)


def imported_products_view(request):
    with open('myapp/fixtures/parser.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)

    for product_quality in data:
        Products.objects.get_or_create(
            product_name=product_quality['Наименование'],
            vendor_code=product_quality['Артикул'],
            category=product_quality['Категория'],
            sub_category=product_quality['Подкатегория'],
            product_type=product_quality['Вид изделия'],
            completeness=product_quality['Комплектность'],
            gender=product_quality['Пол'],
            season=product_quality['Сезон'],
            material=product_quality['Ткань/Материал верха'],
            compound=product_quality['Состав'],
            density=product_quality['Плотность/Толщина материала'],
            color=product_quality['Цвет'],
        )

    return HttpResponse("Done")