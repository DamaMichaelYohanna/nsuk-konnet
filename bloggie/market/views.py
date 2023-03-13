from django.shortcuts import render


def market(request):
    context = {}
    return render(request, 'market.html', context)


def add_product(request):
    pass


def edit_product(request):
    pass


def delete_product(reqeust):
    pass
