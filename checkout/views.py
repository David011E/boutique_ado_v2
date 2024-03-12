from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JZTOFFrxPi5qjzPLCD0eNawrStnPmthgDSKBss5HzmxohC3zzSNx7V5Am5JpzMVeoe8Ddr3upiOSXL1BcdLyRUK00CV9Yvk6m',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)