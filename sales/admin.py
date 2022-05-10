from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('price', 'prime_price'), 'date']
    list_display = ['date', 'price', 'prime_price', 'diff_price']
    list_display_links = ['date']
    search_fields = ['price']
    list_editable = ['price', 'prime_price']
    date_hierarchy = 'date'
    list_filter = ['date']
