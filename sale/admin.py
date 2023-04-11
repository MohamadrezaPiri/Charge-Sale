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
    list_display = ['seller', 'amount','type','status']
    search_fields=['seller']
    

@admin.register(CreditOrder)
class CreditOrderAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount', 'order_type','status']
    search_fields=['seller']
    autocomplete_fields=['seller']


@admin.register(SaleOrder)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display=['seller','phone','amount']
    autocomplete_fields=['seller']
