from rest_framework import serializers
from appontripadministracion.models import *

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [
            'id', 
            'nombre_pais', 
            'estado',
            ]

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
            'fecha_creacion',
            'Portada',
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
            'tipos_turismo',
        ]

    def get_tipos_turismo(self, obj):

        return [
            item.Id_turismo.Nombre
            for item in obj.destinotipoturismo.all()
        ]
        
    def get_imagenesportada(self, obj):

        imagenes = obj.imagenes.filter(Portada=True)

        return FotografiasSerializer(
            imagenes,
            many=True,
            context=self.context
        ).data
class Atractivos_turisticos_serializers_list(serializers.ModelSerializer):
    
    class Meta:
        model = atractivoturistico
        
        fields = [
            'Id',
            'Nombre',
            'Descripcion',
            'Historia',
            'Categoria'
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
    atractivosturisticos = Atractivos_turisticos_serializers_list(many=True, read_only= True)
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
            'estado',
            'latitud',
            'longitud',
            'imagenes',
            'actividades',
            'tiposturismo',
            'atractivosturisticos'
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
class FotografiasPortadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = fotografias
        fields = [
            'Id',
            'Nombre',
            'Imagen',
            'Autor',
        ]
        
class Destinos_mas_consultados_serializer(serializers.ModelSerializer):

    total_visitas = serializers.IntegerField(read_only=True)

    region = serializers.CharField(source='municipio.departamento.region.nombre_region', read_only=True)
    departamento = serializers.CharField(source='municipio.departamento.nombre_departamento', read_only=True)
    municipio = serializers.CharField(source='municipio.nombre_municipio',read_only=True)
    ubicacion = serializers.SerializerMethodField()
    tipos_turismo = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()
    class Meta:
        model = DestinoTuristico

        fields = [
            'id',
            'nombre_destino',
            'region',
            'departamento',
            'municipio',
            'ubicacion',
            'tipos_turismo',
            'total_visitas',
            'imagen'
        ]

    def get_tipos_turismo(self, obj):

        return [
            item.Id_turismo.Nombre
            for item in obj.destinotipoturismo.all()
        ]

    def get_ubicacion(self, obj):

        municipio = obj.municipio.nombre_municipio
        departamento = obj.municipio.departamento.nombre_departamento

        return f"{municipio}, {departamento}, Colombia"
    
    def get_imagen(self, obj):
        imagen = obj.imagenes.first()  

        if imagen:
            return FotografiasSerializer(imagen).data

        return None