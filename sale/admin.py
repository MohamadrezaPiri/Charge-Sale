from django.contrib import admin
from .models import SaleOrder, Seller, Transaction, CreditOrder


# Register your models here.


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'credit']
    search_fields=['name']
    list_filter=['name']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount','type']
    search_fields=['seller']
    list_filter=['seller']

@admin.register(CreditOrder)
class CreditOrderAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount', 'order_type']
    search_fields=['seller']
    list_filter=['seller']


@admin.register(SaleOrder)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display=['seller','phone','amount']