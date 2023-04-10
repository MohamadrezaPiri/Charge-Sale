from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction, CreditOrder, Transaction, Seller


@receiver(post_save, sender=CreditOrder)
def update_seller_credit_and_create_transaction_after_credit_order(sender, **kwargs):
    if kwargs['created']:
        seller = Seller.objects.get(pk=kwargs['instance'].seller.id)
        if kwargs['instance'].order_type == 'WIT':
            seller.credit -= kwargs['instance'].amount
            seller.save()
            Transaction.objects.create(seller=kwargs['instance'].seller,amount=kwargs['instance'].amount,type=kwargs['instance'].order_type)
        else:
            seller.credit += kwargs['instance'].amount
            seller.save()
            Transaction.objects.create(seller=kwargs['instance'].seller,amount=kwargs['instance'].amount,type=kwargs['instance'].order_type)

