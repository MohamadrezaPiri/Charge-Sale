from django.contrib import admin
from .models import SaleOrder, Seller, Transaction, CreditOrder


# Register your models here.


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'credit']
    fields = ['name']
    search_fields=['name']
    list_filter=['name']
    list_per_page = 10

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount','status']
    search_fields=['seller']
    list_per_page = 10
    

@admin.register(CreditOrder)
class CreditOrderAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount', 'order_type','status']
    fields = ['seller','order_type','amount']
    search_fields=['seller']
    autocomplete_fields=['seller']
    list_per_page = 10


@admin.register(SaleOrder)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display=['seller','phone','amount']
    autocomplete_fields=['seller']
    list_per_page = 10
