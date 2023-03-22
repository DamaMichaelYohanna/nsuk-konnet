from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    store_ord.order.add(order)
    messages.success(request, "Order has been placed successfully")
    return redirect("/market")


@login_required
def view_order_by_customer(request):
    order = Order.objects.filter(customer=request.user)
    return render(request, 'order_customer.html', {"order": order})


def add_product(request):
    pass


def edit_product(request):
    pass


def delete_product(reqeust):
    pass
