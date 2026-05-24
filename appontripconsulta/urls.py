from django.urls import path
from appontripconsulta.views import *
from django.conf import settings


urlpatterns = [
    path('filtros/', FiltrosJerarquicosAPIView.as_view(), name='filtros-jerarquicos'),
    path('destinos/<int:pk>/', DestinoTuristicoDetailView.as_view()),
    path('get/fotografias/', FotografiasDetailView.as_view(), name='galeria'),
    path('get/establecimientosturisticos/', Establecimientos_turisticos_detailview.as_view(), name = 'establecimientos_turisticos'),
]
