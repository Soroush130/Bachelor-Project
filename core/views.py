from django.shortcuts import render

from products.models import Products

from products.utility import get_last_products, get_outstanding_products


def home(request):
    products = Products.objects.all()
    # آخرین محصولات
    last_products = get_last_products(products)
    # محصولات برجسته
    outstanding_products = get_outstanding_products(products)

    context = {
        'last_products': last_products,
        'outstanding_products': outstanding_products,
    }
    return render(request, "index.html", context)
