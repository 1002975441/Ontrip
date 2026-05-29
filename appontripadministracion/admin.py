from django.contrib import admin
from django import forms

from appontripadministracion.models import *
from .admin_site import admin_site


# =========================================================
# ESTRUCTURA ORGANIZACIONAL
# =========================================================

@admin.register(Pais, site=admin_site)
class PaisAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_pais", "estado", "fecha_creacion")


@admin.register(Region, site=admin_site)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_region", "pais", "estado", "fecha_creacion")


@admin.register(Departamento, site=admin_site)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_departamento", "region", "estado", "fecha_creacion")


@admin.register(Municipio, site=admin_site)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_municipio", "departamento", "estado", "fecha_creacion")


# =========================================================
# INFORMACIÓN TURÍSTICA
# =========================================================

@admin.register(DestinoTuristico, site=admin_site)
class DestinoTuristicoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_destino',
        'municipio',
        'email_responsable_documentacion',
        'estado',
        'fecha_creacion'
    )


@admin.register(Actividadturistica, site=admin_site)
class ActividadTuristicaAdmin(admin.ModelAdmin):
    list_display = (
        'Nombre_actividad_turistica',
        'estado',
        'fecha_creacion'
    )


@admin.register(Turismo, site=admin_site)
class TurismoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Nombre', 'Estado')


@admin.register(destinotipoturismo, site=admin_site)
class DestinotipoturismoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Id_destino', 'Id_turismo')


@admin.register(tipoevento, site=admin_site)
class TipoeventoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Nombre')


@admin.register(eventos, site=admin_site)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('Id', 'municipio', 'Nombre')


@admin.register(eventotipo, site=admin_site)
class EventotipoAdmin(admin.ModelAdmin):
    list_display = ('Id_tipoevento', 'Id_evento')


@admin.register(atractivoturistico, site=admin_site)
class AtractivoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Id_destino', 'Nombre')


# =========================================================
# PAQUETES TURÍSTICOS
# =========================================================

class PaqueteDestinoInline(admin.TabularInline):
    model = PaqueteDestino
    extra = 1


class PaqueteActividadInline(admin.TabularInline):
    model = PaqueteActividad
    extra = 1


@admin.register(PaqueteTuristico, site=admin_site)
class PaqueteTuristicoAdmin(admin.ModelAdmin):

    list_display = (
        'Id',
        'Nombre',
        'Fecha_inicio',
        'Fecha_fin',
        'Valor_base',
        'estado'
    )

    search_fields = ('Nombre',)

    inlines = [
        PaqueteDestinoInline,
        PaqueteActividadInline
    ]


# =========================================================
# CLIENTES Y RESERVAS
# =========================================================

@admin.register(Cliente, site=admin_site)
class ClienteAdmin(admin.ModelAdmin):

    list_display = (
        'Nombre',
        'Correo',
        'Celular',
        'fecha_creacion'
    )

    search_fields = (
        'Nombre',
        'Correo'
    )


@admin.register(Reserva, site=admin_site)
class ReservaAdmin(admin.ModelAdmin):

    list_display = (
        'Id',
        'Id_cliente',
        'Id_paquete',
        'Numero_personas',
        'Valor_unitario',
        'Descuento',
        'Total',
        'Forma_pago',
        'Vendedor',
        'Fecha_reserva'
    )

    search_fields = (
        'Id_cliente__Nombre',
        'Id_paquete__Nombre'
    )


# =========================================================
# GALERÍA Y MULTIMEDIA
# =========================================================

@admin.register(fotografias, site=admin_site)
class GaleriaAdmin(admin.ModelAdmin):

    list_display = (
        'Id',
        'Nombre',
        'Destino',
        'Actividad'
    )


# =========================================================
# ALOJAMIENTOS
# =========================================================

@admin.register(EstablecimientoTuristico, site=admin_site)
class EstablecimientoTuristicoAdmin(admin.ModelAdmin):

    list_display = (
        'Id',
        'Nombre',
        'Id_destino'
    )


@admin.register(TipoAlojamiento, site=admin_site)
class TipoAlojamientoAdmin(admin.ModelAdmin):

    list_display = (
        'Id',
        'Nombre'
    )


@admin.register(Alojamiento, site=admin_site)
class AlojamientoAdmin(admin.ModelAdmin):

    list_display = (
        'Id',
        'Id_destino',
        'Id_establecimiento',
        'Nombre'
    )


# =========================================================
# PRODUCTOS
# =========================================================

@admin.register(tipoproducto, site=admin_site)
class TipoProductoAdmin(admin.ModelAdmin):

    list_display = (
        'Id',
        'Nombre'
    )


@admin.register(productos, site=admin_site)
class ProductosAdmin(admin.ModelAdmin):

    list_display = (
        'Id',
        'Id_tipoproducto',
        'Nombre'
    )