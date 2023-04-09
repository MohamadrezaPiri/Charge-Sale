from django.contrib import admin
from .models import SaleOrder, Seller, Transaction, CreditOrder


# Register your models here.

# admin.site.register(Seller)
admin.site.register(SaleOrder)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'credit']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount','type']


@admin.register(CreditOrder)
class CreditOrderAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount', 'order_type']
