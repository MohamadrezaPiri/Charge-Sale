from django.db import transaction as r
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction, CreditOrder



@receiver(post_save, sender=CreditOrder)
def update_seller_credit_and_create_transaction_after_credit_order(sender, instance, created, **kwargs):
    with r.atomic():
        if created:
            seller = instance.seller
            amount = instance.amount
            order_type = instance.order_type
            
            
            if order_type == 'WIT':
                if seller.credit >= amount:
                    seller.credit -= amount
                    instance.status = 'COM'
                    Transaction.objects.create(seller=seller, amount=-amount,status='COM')
                else:
                    instance.status = 'FAI'
                    Transaction.objects.create(seller=seller, amount=-amount,status='FAI')
            else:
                seller.credit += amount
                Transaction.objects.create(seller=seller, amount=amount,status='COM')
                instance.status = 'COM'
            seller.save()
            instance.save()



