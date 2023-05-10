from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models import Count
from django.db.models.query import QuerySet

class CreditFilter(admin.SimpleListFilter):
    title = 'Credit'
    parameter_name = 'credit'

    def lookups(self, request, model_admin):
        return [
            ('=0', 'Without credit'),
            ('0<', 'With credit')

        ]

    def queryset(self, request, queryset):
        if self.value() == '=0':
            return queryset.filter(credit=0)
        elif self.value() == '0<':
            return queryset.filter(credit__gt=0)
        

class TransactionCountFilter(admin.SimpleListFilter):
    title = 'Transaction count'
    parameter_name = 'Transactions'

    def lookups(self, request, model_admin):
        return [
            ('=0', 'Without transaction'),
            ('0<', 'With transaction')

        ]        
    
    def queryset(self, request, queryset):
        annotated_value = queryset.annotate(transactions_count = Count('transaction'))
        if self.value() == '=0':
            return annotated_value.filter(transactions_count = 0)
        elif self.value() == '0<':
            return annotated_value.filter(transactions_count__gt = 0)
        

class TransactionTypeFilter(admin.SimpleListFilter):
    title = 'Type'
    parameter_name = 'amount'

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            ('0<','Deposit'),
            ('<0','Withdraw')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '0<':
            return queryset.filter(amount__gt = 0)
        elif self.value() == '<0':
            return queryset.filter(amount__lt = 0)

