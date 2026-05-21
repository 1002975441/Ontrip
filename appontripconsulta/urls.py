from django.urls import path
from appontripconsulta.views import *
from django.conf import settings


urlpatterns = [
    path('filtros/', FiltrosJerarquicosAPIView.as_view(), name='filtros-jerarquicos'),
    path('destinos/<int:pk>/', DestinoTuristicoDetailView.as_view()),
]
