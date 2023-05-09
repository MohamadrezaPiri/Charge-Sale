from django.contrib import admin
from django.urls import reverse
from django.utils.html import urlencode, format_html
from django.db.models import Count
from .models import SaleOrder, Seller, Transaction, CreditOrder


# Register your models here.


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'credit','transactions']
    fields = ['name']
    search_fields=['name']
    list_filter=['name']
    list_per_page = 10

    def transactions(self, seller):
        url = (
            reverse('admin:sale_seller_changelist')
            + '?'
            + urlencode({
                'seller__id': str(seller.id)
            }))
        return format_html('<a href="{}">{}</a>', url, seller.transactions)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            transactions=Count('transaction')
        )



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
