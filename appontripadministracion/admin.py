from django.contrib import admin
from django import forms
from appontripadministracion.models import (
    Pais,
    Region,
    Departamento,
    Municipio,
    DestinoTuristico
)


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_pais", "estado", "fecha_creacion")
    search_fields = ("nombre_pais",)
    list_filter = ("estado",)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_region", "pais", "estado", "fecha_creacion")
    search_fields = ("nombre_region",)
    list_filter = ("pais", "estado")


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_departamento", "region", "estado", "fecha_creacion")
    search_fields = ("nombre_departamento",)
    list_filter = ("region", "estado")


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_municipio", "departamento", "estado", "fecha_creacion")
    search_fields = ("nombre_municipio",)
    list_filter = ("departamento", "estado")

@admin.register(DestinoTuristico)
class DestinoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nombre_destino', 'municipio', 'email_responsable_documentacion', 'estado', 'fecha_creacion')
    search_fields = ('nombre_destino', 'municipio__nombre_municipio')
    list_filter = ('estado', 'municipio')
    ordering = ('nombre_destino',)