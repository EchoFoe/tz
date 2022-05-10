from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.views import View
# from django.core.serializers import serialize

from .filters import SaleFilter
from .models import Sale
from .serializers import SalesSerializer


def home(request):
    return render(request, 'home/home.html')


def objects(request):

    objects_list = Sale.objects.all()

    context = {
        'objects_list': objects_list
    }

    return render(request, 'objects/objects_list.html', context)


def object_detail(request, id):
    obj = get_object_or_404(Sale, id=id)

    context = {
        'obj': obj
    }

    return render(request, 'objects/object_detail.html', context)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'


class SaveEntities(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['price', 'date']
    filter_class = SaleFilter
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    search_fields = ['price', 'date']
    lookup_field = 'pk'


class GetEntities(View):

    @staticmethod
    def get(request):
        entity_objects = Sale.objects.values()
        field_objects = Sale.objects.all()

        objects_serialized_data = []
        for obj in entity_objects:
            objects_serialized_data.append(obj)

        fields_serialized_data = []
        for obj in field_objects:
            fields_serialized_data.append({
                'price': obj.price,
                'prime_price': obj.prime_price,
            })

        data_serialized = {
            'entity': objects_serialized_data,
            'fields': fields_serialized_data,
        }

        data = [data_serialized]

        return JsonResponse(data, safe=False, status=201)


class GetResults(View):

    @staticmethod
    def get(request):
        objects = Sale.objects.all()

        results_serialized_data = []
        for obj in objects:
            results_serialized_data.append({
                str('Result') + str([obj.date.__format__('%d.%m.%Y')]): obj.price - obj.prime_price,
            })

        data = results_serialized_data
        return JsonResponse(data, safe=False)
