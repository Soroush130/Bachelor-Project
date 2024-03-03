from django.urls import path
from .views import log_in, register, log_out

app_name = 'accounts'

urlpatterns = [
    path('login/', log_in, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_out, name='logout'),
]