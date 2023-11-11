from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from myapp.models import Products
import json
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages


def created_products_view(request):
    products = Products.objects.all()

    context = {
        'table': products
    }
    return render(request, 'index.html', context)


def imported_products_view(request):
    with open('\Project\Parser\parser.json', 'r', encoding='UTF-8') as f:
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


def product_view_detailed(request, id):
    product = get_object_or_404(Products, id=id)
    context = {'product': product}
    return render(request, 'detailed_product.html', context)


# class RegisterFormView(FormView):
#     form_class = UserCreationForm
#     success_url = 'myapp/login/'
#
#     template_name = 'register.html'
#
#     def form_valid(self, form):
#         form.save()
#         return super(RegisterFormView, self).form_valid(form)
#
#     def form_invalid(self, form):
#
#         return super(RegisterFormView, self).form_invalid(form)

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('')
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'register.html', context)
#
#
# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have been logged out.')
#     return redirect('myapp/')


# def login_view(request):
#


@login_required
def profile_view(request):
    return render(request, 'profile.html')
