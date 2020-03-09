from django.shortcuts import get_object_or_404
from .models import Order
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
import random
import string 

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        order = get_object_or_404(Order, id=ipn.invoice)

        if order.get_total() == ipn.mc_gross:
            # mark the order as paid
            order_items = order.items.all()
            order_items.update(ordered=True)
            for item in order_items:
                item.save()

            order.ordered = True
            order.save()
            
            