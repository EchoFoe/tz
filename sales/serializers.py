from rest_framework import serializers
from .models import Sale
from django.urls import reverse


class SalesSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%d.%m.%Y')
    url = serializers.HyperlinkedIdentityField(view_name='sales:sale-detail')

    class Meta:
        model = Sale
        fields = ('url', 'pk', 'price', 'prime_price', 'date', 'diff_price')
