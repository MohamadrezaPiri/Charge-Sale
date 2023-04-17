import pytest
from rest_framework import status
from model_bakery import baker
from sale.models import *


# Fixtures
@pytest.fixture
def create_sale_order(api_client):
    def do_create_sale_order(sale_order):
        return api_client.post('/sell/',sale_order)
    return do_create_sale_order


@pytest.mark.django_db
class TestCreateSaleOrder:
    def test_if_sale_order_is_created_returns_201(self, create_sale_order):
        seller = baker.make(Seller, credit=30000)

        data = {
            'seller': seller.id,
            'phone': '09029813840',
            'amount': 5
        }
            
        initial_credit = seller.credit
                
        response = create_sale_order(data)
        assert response.status_code == status.HTTP_201_CREATED

        seller.refresh_from_db()
            
        assert seller.credit == (initial_credit - data['amount'])


    @pytest.mark.parametrize("i", range(10))
    @pytest.mark.xfail(reason="Possible thread safety issue")
    def test_if_credit_is_not_enough_returns_400(self, create_sale_order, i):
        pytest.xfail("Possible thread safety issue")

        with self.lock:
            seller=baker.make(Seller, credit=2000)
            data = {
                    'seller': seller.id,
                    'phone': '09029813840',
                    'amount': 3000
                }
            response = create_sale_order(data)
            assert response.status_code == status.HTTP_400_BAD_REQUEST