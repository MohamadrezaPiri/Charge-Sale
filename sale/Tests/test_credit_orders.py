import pytest
from model_bakery import baker
from sale.models import *



# Tests
@pytest.mark.django_db
class TestCreditOrder:
    def test_if_credit_order_is_created(self):
        seller= baker.make(Seller,credit=0)

        amount=500
        order_type='DEP'
        initial_balance1 = seller.credit

        credit_order = CreditOrder.objects.create(seller=seller,
                                                  amount=amount,
                                                  order_type=order_type,
                                                  status='COM'
        )

        assert credit_order.amount == amount
        assert credit_order.order_type == order_type
        assert credit_order.status == 'COM'
            
        seller.refresh_from_db
        assert seller.credit == initial_balance1 + amount