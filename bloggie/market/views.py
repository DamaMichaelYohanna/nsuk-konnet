from django.shortcuts import render


def market(request):
    context = {}
    return render(request, 'market.html', context)