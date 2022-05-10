from django.urls import path, include
from rest_framework import routers

from .views import home, objects, object_detail, SaveEntities, GetEntities, GetResults

router = routers.SimpleRouter()
router.register(r'api/sales', SaveEntities, basename='sale')

app_name = 'sale'

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls,)),
    path('objects_list/', objects, name='objects_list'),
    path('object/<int:id>/', object_detail, name='object_detail'),
    path('api/sales/', SaveEntities.as_view({'get': 'list'}), name='api_sales'),
    path('api/objects/', GetEntities.as_view(), name='api_objects'),
    path('api/results/', GetResults.as_view(), name='api_results'),
]
urlpatterns += router.urls
