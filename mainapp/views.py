from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')

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
