from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'mainapp/index.html')


def products(request, page=1, category_id=None):
    context = {
        'title': 'GeekShop - Категории',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
        #context.update({'products': products})

    else:
        products = Product.objects.all().order_by('price')
        #context.update({'products': products})
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)


def test_context(request):
    context = {
        'title': 'добро пожаловать',
        'username': 'Alex Alex',
        'products': [
            {'name': 'Черная худи', 'price': '2 990 руб.'},
            {'name': 'Джинсы', 'price': '5 900 руб.'},
        ],
        'promotion': True,
        'promotion_products': [
            {'name': 'Туфли', 'price': '10 000 руб.'},
        ],
    }
    return render(request, 'mainapp/context.html', context)
