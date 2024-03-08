from decimal import Decimal
from django.conf import settings

def bag_contexts(request):

    bag_items = []
    total = 0
    product_count = 0

    # Free delivery if met total percentage
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total # How much need to spend to get free delivery
    else:
        delivery = 0 
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total
    }

    return context