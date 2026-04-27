from rest_framework import serializers
from appontripadministracion.models import *

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre_pais', 'estado', 'fecha_creacion']

class RegionSerializer(serializers.ModelSerializer):
    pais_nombre = serializers.CharField(source='pais.nombre_pais', read_only=True)
    class Meta:
        model = Region
        fields = ['id', 'pais', 'pais_nombre', 'nombre_region', 'estado', 'fecha_creacion']

class DepartamentoSerializer(serializers.ModelSerializer):
    region_nombre = serializers.CharField(source='region.nombre_region', read_only=True)
    pais_nombre = serializers.CharField(source='region.pais.nombre_pais', read_only=True)
    class Meta:
        model = Departamento
        fields = ['id', 'region', 'region_nombre', 'pais_nombre', 'nombre_departamento', 'estado', 'fecha_creacion']

class MunicipioSerializer(serializers.ModelSerializer):
    departamento_nombre = serializers.CharField(source='departamento.nombre_departamento', read_only=True)
    region_nombre = serializers.CharField(source='departamento.region.nombre_region', read_only=True)
    pais_nombre = serializers.CharField(source='departamento.region.pais.nombre_pais', read_only=True)
    class Meta:
        model = Municipio
        fields = ['id', 'departamento', 'departamento_nombre', 'region_nombre', 'pais_nombre', 'nombre_municipio', 'estado', 'fecha_creacion']

class DestinoTuristicoSerializer(serializers.ModelSerializer):
    municipio_nombre = serializers.CharField(source='municipio.nombre_municipio', read_only=True)
    departamento_id = serializers.IntegerField(source='municipio.departamento.id', read_only=True)
    departamento_nombre = serializers.CharField(source='municipio.departamento.nombre_departamento', read_only=True)
    region_id = serializers.IntegerField(source='municipio.departamento.region.id', read_only=True)
    region_nombre = serializers.CharField(source='municipio.departamento.region.nombre_region', read_only=True)
    pais_id = serializers.IntegerField(source='municipio.departamento.region.pais.id', read_only=True)
    pais_nombre = serializers.CharField(source='municipio.departamento.region.pais.nombre_pais', read_only=True)

    class Meta:
        model = DestinoTuristico
        fields = [
            'id',
            'pais_id', 'pais_nombre',
            'region_id', 'region_nombre',
            'departamento_id', 'departamento_nombre',
            'municipio', 'municipio_nombre',
            'nombre_destino', 'Detalle_ubicacion',
            'Url_video_promocional', 'Url_video_informativo',
            'descripcion', 'email_responsable_documentacion',
            'estado', 'fecha_creacion'
        ]