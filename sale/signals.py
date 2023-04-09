from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction, CreditOrder, Transaction, Seller


@receiver(post_save, sender=CreditOrder)
def create_transaction_for_credit_order(sender, **kwargs):
    if kwargs['created']:
        seller = Seller.objects.get(pk=kwargs['instance'].seller.id)
        if kwargs['instance'].order_type == 'WIT':
            seller.credit -= kwargs['instance'].amount
            seller.save()
        else:
            seller.credit += kwargs['instance'].amount
            seller.save()
