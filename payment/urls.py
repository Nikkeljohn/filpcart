from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]
