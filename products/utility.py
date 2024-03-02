from django.db.models import QuerySet
from products.models import Gallery


def get_last_products(products: QuerySet) -> QuerySet:
    return products.order_by('-created')


def get_outstanding_products(products: QuerySet) -> QuerySet:
    products_list = {}
    for product in products:
        image_list = get_images_product(product)
        products_list[product] = image_list
    return products_list


def get_images_product(product: QuerySet) -> QuerySet:
    return Gallery.objects.filter(product_id=product.id).order_by('-id')[:4]
