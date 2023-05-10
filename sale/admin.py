from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import urlencode, format_html
from django.db.models import Count
from .models import SaleOrder, Seller, Transaction, CreditOrder
from .filters import CreditFilter, TransactionCountFilter, TransactionTypeFilter

# Register your models here.


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'credit','transactions']
    list_filter=['name',CreditFilter, TransactionCountFilter]
    list_per_page = 10
    fields = ['name']
    search_fields=['name']
    actions = ['clear_transactions']

    @admin.display(ordering='transactions')
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
    
    @admin.action(description="Clear Transactions")
    def clear_transactions(self, request, queryset):
        total_transactions_count = sum(seller.transaction_set.count() for seller in queryset)

        for seller in queryset:
            seller.transaction_set.all().delete()

        self.message_user(
            request,
            f'{total_transactions_count} were successfully removed',
            messages.SUCCESS
        )    


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['seller', 'amount','status']
    list_filter = ['status','seller',TransactionTypeFilter]
    list_per_page = 10
    search_fields=['seller']
    

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
