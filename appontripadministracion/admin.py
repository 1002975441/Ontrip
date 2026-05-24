from django.contrib import admin
from django import forms
from appontripadministracion.models import *


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_pais", "estado", "fecha_creacion")
    
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_region", "pais", "estado", "fecha_creacion")

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_departamento", "region", "estado", "fecha_creacion")

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_municipio", "departamento", "estado", "fecha_creacion")

@admin.register(DestinoTuristico)
class DestinoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nombre_destino', 'municipio', 'email_responsable_documentacion', 'estado', 'fecha_creacion')

@admin.register(Actividadturistica)
class ActividadTuristicaAdmin(admin.ModelAdmin):
    list_display = ('Nombre_actividad_turistica', 'estado', 'fecha_creacion')


class PaqueteDestinoInline(admin.TabularInline):
    model = PaqueteDestino
    extra = 1


class PaqueteActividadInline(admin.TabularInline):
    model = PaqueteActividad
    extra = 1

@admin.register(PaqueteTuristico)
class PaqueteTuristicoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Nombre', 'Fecha_inicio', 'Fecha_fin', 'Valor_base', 'estado')
    search_fields = ('Nombre',)
    inlines = [
        PaqueteDestinoInline,
        PaqueteActividadInline
    ]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Correo', 'Celular', 'fecha_creacion')
    search_fields = ('Nombre', 'Correo')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Id_cliente', 'Id_paquete', 'Numero_personas', 'Valor_unitario', 'Descuento', 'Total',
        'Forma_pago', 'Vendedor', 'Fecha_reserva')
    search_fields = ('Id_liente__Nombre', 'Id_paquete__Nombre')
    
@admin.register(fotografias)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Nombre', 'Destino', 'Actividad')
    
@admin.register(EstablecimientoTuristico)
class EstablecimientoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Nombre', 'Id_destino')
    
@admin.register(TipoAlojamiento)
class TipoAlojamientoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Nombre')

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Id_destino', 'Id_establecimiento', 'Nombre')
    
@admin.register(Turismo)
class TurismoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Nombre', 'Estado')
    
@admin.register(destinotipoturismo)
class DestinotipoturismoAdmin(admin.ModelAdmin):
      list_display = ('Id', 'Id_destino', 'Id_turismo') 

@admin.register(tipoproducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Nombre')
    
@admin.register(productos)
class PorductosAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Id_tipoproducto', 'Nombre')
    
@admin.register(tipoevento)
class TipoeventoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Nombre')
    
@admin.register(eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('Id', 'municipio', 'Nombre')

@admin.register(eventotipo)
class EventotipoAdmin(admin.ModelAdmin):
    list_display = ('Id_tipoevento', 'Id_evento')