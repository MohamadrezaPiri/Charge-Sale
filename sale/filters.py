from django.contrib import admin
from django.db.models import Count

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