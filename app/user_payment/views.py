from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from user_payment.models import Item
import stripe


def get_stripe_session_id(request, item_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    item = Item.objects.get(id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price': settings.PRODUCT_PRICE,
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )

    return JsonResponse({'session_id': session['id']})


def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, 'item_detail.html', context)


def payment_successful(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    return render(request, 'success.html')


def payment_cancelled(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    return render(request, 'user_payment/payment_cancelled.html')
