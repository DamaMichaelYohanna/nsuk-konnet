from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, StoreOrder


def market(request):
    # if
    page = request.GET.get("page", 1)
    search = request.GET.get('search')
    category = request.GET.get("category")
    if search and category:
        products = Product.objects.filter(name__icontains=search)
    elif search:
        products = Product.objects.filter(name__icontains=search)
    elif category:
        products = Product.objects.filter(category__icontains=category)
    else:
        products = Product.objects.all()

    page_obj = Paginator(products, 20)
    try:
        products = page_obj.page(page)
    except PageNotAnInteger:
        products = page_obj.page(1)
    except EmptyPage:
        products = page_obj.page(page_obj.num_pages)
    print(products)
    context = {"products": products}
    return render(request, 'market.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {"product": product})


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


@login_required
def add_product(request):
    if request.method == "POST":
        product = Product.objects.create()
    else:
        pass
    context = {}
    return render(request, "add_product.html", context)


@login_required
def edit_product(request):
    pass


@login_required
def delete_product(reqeust):
    pass
