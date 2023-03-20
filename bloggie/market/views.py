from django.contrib import  messages
from django.shortcuts import render, redirect
from .models import Product, Order, StoreOrder


def market(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'market.html', context)


def place_order(request, pk):
    """view for placing orders"""
    product = Product.objects.get(pk=pk)
    order = Order.objects.create(product=product, customer=request.user)
    store_ord, _ = StoreOrder.objects.get_or_create(store=product.owner.store)
    print(store_ord.order)
    store_ord.order.add(order)
    messages.success(request,
                     "Your order has been sent to the seller. "
                     "check your orders tab for progress")
    return redirect("/market")


def add_product(request):
    pass


def edit_product(request):
    pass


def delete_product(reqeust):
    pass
