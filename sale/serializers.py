from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import SaleOrder,Transaction


class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = ['seller', 'phone', 'amount']

    def save(self):
        with transaction.atomic():
            seller = self.validated_data['seller']
            phone = self.validated_data['phone']
            amount = self.validated_data['amount']

            if amount > seller.credit:
                raise ValidationError('Not enough credit')
            SaleOrder.objects.create(seller=seller, phone=phone, amount=amount)
        
            # Update seller's credit after selling the charge
            seller.credit -= amount
            seller.save()

            # Add the order to Transactions list by creating a transaction
            Transaction.objects.create(seller=seller, amount=-amount, status='COM')
