import pytest
from rest_framework import status
from model_bakery import baker
from sale.models import *



# Tests
@pytest.mark.django_db
class TestCreditOrder:
    def test_credit_order_is_created(self):
        seller1= baker.make(Seller,credit=0)
        seller2= baker.make(Seller,credit=0)

        amount=500
        order_type='DEP'
        initial_balance1 = seller1.credit
        initial_balance2 = seller2.credit

        num_orders = 10
        credit_orders=[]
        for i in range(num_orders):
            credit_order = CreditOrder.objects.create(seller=seller1 if i % 2 == 0 else seller2,
                                                      amount=amount,
                                                      order_type=order_type,
                                                      status='COM'
            )
            credit_orders.append(credit_order)

        for credit_order in credit_orders:
            assert credit_order.amount == amount
            assert credit_order.order_type == order_type
            assert credit_order.status == 'COM'

        
        seller1.refresh_from_db
        seller2.refresh_from_db
        assert seller1.credit == initial_balance1 + num_orders // 2 * amount
        assert seller2.credit == initial_balance2 + num_orders // 2 * amount