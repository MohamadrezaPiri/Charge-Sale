from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SaleOrder
from .serializers import SaleOrderSerializer

# Create your views here.


class SaleOrderViewSet(ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer
