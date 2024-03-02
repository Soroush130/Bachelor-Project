from django.urls import path
from products.views import detail_product

app_name = 'products'

urlpatterns = [
    path('detail/<int:id>/', detail_product, name='detail'),
]