from django.shortcuts import render
from products.models import Products
from products.utility import get_images_product

def detail_product(request, id):
    product = Products.objects.get(id=id)
    image_list = get_images_product(product)

    context = {
        'product': product,
        'image_list': image_list,
    }
    return render(request, 'products/detail_product.html', context)