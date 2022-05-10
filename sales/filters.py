from .models import Sale
import django_filters
from django_filters import rest_framework


class SaleFilter(django_filters.FilterSet):
    price__gt = rest_framework.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = rest_framework.NumberFilter(field_name='price', lookup_expr='lte')
    prime_price__gt = rest_framework.NumberFilter(field_name='prime_price', lookup_expr='gte')
    prime_price__lt = rest_framework.NumberFilter(field_name='prime_price', lookup_expr='lte')
    date_gte = rest_framework.DateFilter(field_name='date', label='Дата от', lookup_expr='gte')
    date_lt = rest_framework.DateFilter(field_name='date', label='Дата до', lookup_expr='lte')

    class Meta:
        model = Sale
        fields = ['price', 'prime_price', 'date']
