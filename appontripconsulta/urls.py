from django.urls import path
from appontripconsulta.views import FiltrosJerarquicosAPIView

urlpatterns = [
    path('filtros/', FiltrosJerarquicosAPIView.as_view(), name='filtros-jerarquicos'),
]