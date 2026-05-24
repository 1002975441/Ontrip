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

class FotografiasSerializer(serializers.ModelSerializer):

    class Meta:
        model = fotografias
        fields = [
            'Id',
            'Nombre',
            'Destino',
            'Actividad',
            'Imagen',
            'Descripcion',
            'Autor',
            'fecha_creacion'
        ]

class ActividadTuristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividadturistica
        fields = [
            'Id',
            'Nombre_actividad_turistica',
            'Descripcion',
            'Zonas',
            'Duracion',
            'Observacion',
            'Recomendaciones',
            'Nivel',
            'Modalidad',
            'Equipamiento',
            'Enfoque',
            'Precio',
            'estado',
            'fecha_creacion',
        ]

class TurismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turismo
        
        fields = [
            'Id',
            'Nombre',
            'Descripcion',
            'Estado',
        ]
        
class DestinoTipoTurismoSerializer(serializers.ModelSerializer):
    
    turismo = TurismoSerializer(source='Id_turismo', read_only=True)
    class Meta:
        model = destinotipoturismo
        
        fields = [
            'Id',
            'turismo',
            'Id_destino',
            
        ]
        
class DestinoTuristicoSerializerFiltros(serializers.ModelSerializer):

    region = serializers.CharField(source='municipio.departamento.region.nombre_region', read_only=True)
    departamento = serializers.CharField(source='municipio.departamento.nombre_departamento', read_only=True)
    municipio = serializers.CharField(source='municipio.nombre_municipio', read_only=True)
    tipos_turismo = serializers.SerializerMethodField()
    class Meta:
        model = DestinoTuristico

        fields = [
            'id',
            'nombre_destino',
            'region',
            'departamento',
            'municipio',
            'tipos_turismo'
        ]

    def get_tipos_turismo(self, obj):

        return [
            item.Id_turismo.Nombre
            for item in obj.destinotipoturismo.all()
        ]
class DestinoTuristicoSerializer(serializers.ModelSerializer):

    municipio_nombre = serializers.CharField(source='municipio.nombre_municipio', read_only=True)
    departamento_id = serializers.IntegerField(source='municipio.departamento.id', read_only=True)
    departamento_nombre = serializers.CharField(source='municipio.departamento.nombre_departamento', read_only=True)
    region_id = serializers.IntegerField(source='municipio.departamento.region.id', read_only=True)
    region_nombre = serializers.CharField(source='municipio.departamento.region.nombre_region', read_only=True)
    pais_id = serializers.IntegerField(source='municipio.departamento.region.pais.id', read_only=True)
    pais_nombre = serializers.CharField(source='municipio.departamento.region.pais.nombre_pais', read_only=True)
    imagenes = FotografiasSerializer(many=True, read_only=True)
    actividades = ActividadTuristicaSerializer(many=True, read_only=True)
    tiposturismo = TurismoSerializer(many=True, read_only=True)
    destinotipoturismo = DestinoTipoTurismoSerializer(many=True, read_only=True)
    class Meta:
        model = DestinoTuristico

        fields = [
            'id',
            'pais_id',
            'pais_nombre',
            'region_id',
            'region_nombre',
            'departamento_id',
            'departamento_nombre',
            'municipio',
            'municipio_nombre',
            'nombre_destino',
            'Detalle_ubicacion',
            'Vias_acceso',
            'Tipo_acceso',
            'Clima',
            'Recomendaciones',
            'descripcion',
            'Url_video_promocional',
            'Url_video_informativo',
            'email_responsable_documentacion',
            'email_responsable_destino',
            'estado',
            'fecha_creacion',
            'imagenes',
            'actividades',
            'tiposturismo',
            'destinotipoturismo',
        ]
        
class Fotografias_serializer_list(serializers.ModelSerializer):
    
    class Meta:
        model = fotografias
        
        fields = [
            'Id',
            'Nombre',
            'Destino',
            'Actividad',
            'Imagen',
            'Descripcion',
            'Autor',
        ]

class Establecimientos_turisticos_serializers_list(serializers.ModelSerializer):
    
    class Meta:
        model = EstablecimientoTuristico
        
        fields = [
            'Id',
            'Id_destino',
            'Nombre',
            'Descripcion',
            'Detalle_ubicacion',
    
        ]