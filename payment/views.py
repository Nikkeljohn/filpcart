from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def payment(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NOIdDK4TiXrbchbNpDiQL6WKdg54g1VXYnNZT730MGpVWheA3olnYpenmTuQ0F6m53MHq0WVTNeYDRsKXTTq2S6007E57G1rL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)