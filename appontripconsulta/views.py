from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from appontripadministracion.models import *
from appontripconsulta.serializers import *
from rest_framework.generics import RetrieveAPIView
from rest_framework import generics
from django.db.models import Count


class FiltrosJerarquicosAPIView(APIView):
    """
    Filtros jerárquicos SOLO con elementos que tengan destinos turísticos activos.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request):

        pais_id = request.query_params.get('pais_id')
        region_id = request.query_params.get('region_id')
        departamento_id = request.query_params.get('departamento_id')
        municipio_id = request.query_params.get('municipio_id')
        destino_id = request.query_params.get('destino_id')

        # =========================
        # PAÍSES (solo con destinos activos)
        # =========================
        paises = Pais.objects.filter(
            estado=True,
            region__departamento__municipio__destinoturistico__estado=True
        )

        if region_id:
            paises = paises.filter(region__id=region_id)
        if departamento_id:
            paises = paises.filter(region__departamento__id=departamento_id)
        if municipio_id:
            paises = paises.filter(region__departamento__municipio__id=municipio_id)
        if destino_id:
            paises = paises.filter(region__departamento__municipio__destinoturistico__id=destino_id)

        paises = paises.distinct().order_by('nombre_pais')
        paises_serializados = PaisSerializer(paises, many=True).data

        # =========================
        # REGIONES
        # =========================
        regiones = Region.objects.filter(
            estado=True,
            departamento__municipio__destinoturistico__estado=True
        )

        if pais_id:
            regiones = regiones.filter(pais_id=pais_id)
        if departamento_id:
            regiones = regiones.filter(departamento__id=departamento_id)
        if municipio_id:
            regiones = regiones.filter(departamento__municipio__id=municipio_id)
        if destino_id:
            regiones = regiones.filter(departamento__municipio__destinoturistico__id=destino_id)

        regiones = regiones.distinct().order_by('nombre_region')
        regiones_serializadas = RegionSerializer(regiones, many=True).data

        # =========================
        # DEPARTAMENTOS
        # =========================
        departamentos = Departamento.objects.filter(
            estado=True,
            municipio__destinoturistico__estado=True
        )

        if pais_id:
            departamentos = departamentos.filter(region__pais_id=pais_id)
        if region_id:
            departamentos = departamentos.filter(region_id=region_id)
        if municipio_id:
            departamentos = departamentos.filter(municipio__id=municipio_id)
        if destino_id:
            departamentos = departamentos.filter(municipio__destinoturistico__id=destino_id)

        departamentos = departamentos.distinct().order_by('nombre_departamento')
        departamentos_serializados = DepartamentoSerializer(departamentos, many=True).data

        # =========================
        # MUNICIPIOS
        # =========================
        municipios = Municipio.objects.filter(
            estado=True,
            destinoturistico__estado=True
        )

        if pais_id:
            municipios = municipios.filter(departamento__region__pais_id=pais_id)
        if region_id:
            municipios = municipios.filter(departamento__region_id=region_id)
        if departamento_id:
            municipios = municipios.filter(departamento_id=departamento_id)
        if destino_id:
            municipios = municipios.filter(destinoturistico__id=destino_id)

        municipios = municipios.distinct().order_by('nombre_municipio')
        municipios_serializados = MunicipioSerializer(municipios, many=True).data

        # =========================
        # DESTINOS TURÍSTICOS
        # =========================
        destinos = DestinoTuristico.objects.filter(
            estado=True
        ).select_related(
            'municipio',
            'municipio__departamento',
            'municipio__departamento__region',
            'municipio__departamento__region__pais'
        ).prefetch_related(
            'imagenes',
            'actividades',
            'tiposturismo',
            'destinotipoturismo',
            'destinotipoturismo__Id_turismo'
        )

        if pais_id:
            destinos = destinos.filter(municipio__departamento__region__pais_id=pais_id)
        if region_id:
            destinos = destinos.filter(municipio__departamento__region_id=region_id)
        if departamento_id:
            destinos = destinos.filter(municipio__departamento_id=departamento_id)
        if municipio_id:
            destinos = destinos.filter(municipio_id=municipio_id)
        if destino_id:
            destinos = destinos.filter(id=destino_id)

        destinos = destinos.distinct().order_by('nombre_destino')
        destinos_serializados = DestinoTuristicoSerializerFiltros(destinos, many=True).data

        return Response({
            'paises': paises_serializados,
            'regiones': regiones_serializadas,
            'departamentos': departamentos_serializados,
            'municipios': municipios_serializados,
            'destinos': destinos_serializados
        })

class DestinoTuristicoDetailView(RetrieveAPIView):

    queryset = DestinoTuristico.objects.all()
    serializer_class = DestinoTuristicoSerializer

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()

        # registrar visita
        VisitaDestino.objects.create(
            destino=instance
        )

        serializer = self.get_serializer(instance)

        return Response(serializer.data)

class FotografiasDetailView(generics.ListAPIView):
    queryset = fotografias.objects.all()
    serializer_class = Fotografias_serializer_list

class Establecimientos_turisticos_detailview(generics.ListAPIView):
    queryset = EstablecimientoTuristico.objects.all()
    serializer_class = Establecimientos_turisticos_serializers_list
    
class Fotografias_Portada_View(generics.ListAPIView):
    serializer_class = FotografiasPortadaSerializer

    def get_queryset(self):
        return fotografias.objects.filter(Portada=True)

class Destinos_mas_consultados_view(APIView):

    def get(self, request):

        destinos = DestinoTuristico.objects.annotate(
            total_visitas=Count('visitas')
        ).order_by('-total_visitas')[:10]

        serializer = Destinos_mas_consultados(destinos, many=True)

        return Response(serializer.data)