from django.shortcuts import render
from rest_framework.viewsets import mixins,GenericViewSet
from .models import SaleOrder
from .serializers import SaleOrderSerializer

# Create your views here.

class SaleOrderViewSet(mixins.CreateModelMixin,GenericViewSet):
    
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer
