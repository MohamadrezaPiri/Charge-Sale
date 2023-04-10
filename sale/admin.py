from django.contrib import admin
from .models import SaleOrder, Seller, Transaction, CreditOrder


# Register your models here.


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'credit']
    search_fields=['name']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount','type']


@admin.register(CreditOrder)
class CreditOrderAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount', 'order_type']


@admin.register(SaleOrder)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display=['seller','phone','amount']