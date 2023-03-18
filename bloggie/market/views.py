from django.shortcuts import render
from .models import Product


def market(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'market.html', context)


def add_product(request):
    pass


def edit_product(request):
    pass


def delete_product(reqeust):
    pass
