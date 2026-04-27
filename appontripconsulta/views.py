from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from appontripadministracion.models import *
from appontripconsulta.serializers import *

class FiltrosJerarquicosAPIView(APIView):
    """
    Endpoint de filtros jerárquicos para la app de turismo.
    Query params soportados:
        - pais_id
        - region_id
        - departamento_id
        - municipio_id
        - destino_id
    """
    renderer_classes = [JSONRenderer]  # Fuerza JSON, evita errores de template en navegador

    def get(self, request):
        # -------------------------------
        # Captura de query params

        pais_id = request.query_params.get('pais_id')
        region_id = request.query_params.get('region_id')
        departamento_id = request.query_params.get('departamento_id')
        municipio_id = request.query_params.get('municipio_id')
        destino_id = request.query_params.get('destino_id')

        # -------------------------------
        # Países
        # -------------------------------
        paises = Pais.objects.filter(estado=True)
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

        # -------------------------------
        # Regiones
        # -------------------------------
        regiones = Region.objects.filter(estado=True)
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

        # -------------------------------
        # Departamentos
        # -------------------------------
        departamentos = Departamento.objects.filter(estado=True)
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

        # -------------------------------
        # Municipios
        # -------------------------------
        municipios = Municipio.objects.filter(estado=True)
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

        # -------------------------------
        # Destinos turísticos
        # -------------------------------
        destinos = DestinoTuristico.objects.filter(estado=True).select_related(
            'municipio',
            'municipio__departamento',
            'municipio__departamento__region',
            'municipio__departamento__region__pais'
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
        destinos_serializados = DestinoTuristicoSerializer(destinos, many=True).data

        # -------------------------------
        # Respuesta final
        # -------------------------------
        return Response({
            'paises': paises_serializados,
            'regiones': regiones_serializadas,
            'departamentos': departamentos_serializados,
            'municipios': municipios_serializados,
            'destinos': destinos_serializados
        })