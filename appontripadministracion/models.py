from django.db import models


class Pais(models.Model):
    nombre_pais = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'pais'

    def __str__(self):
        return self.nombre_pais


class Region(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nombre_region = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'region'

    def __str__(self):
        return self.nombre_region


class Departamento(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre_departamento = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'departamento'

    def __str__(self):
        return self.nombre_departamento


class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre_municipio = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'municipio'

    def __str__(self):
        return self.nombre_municipio

class DestinoTuristico(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True)
    nombre_destino = models.CharField(max_length=800, null=True, blank=True)
    Detalle_ubicacion = models.CharField(max_length=500, null=False, blank=False)
    Url_video_promocional = models.URLField(null=True, blank=True)
    Url_video_informativo = models.URLField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    email_responsable_documentacion = models.EmailField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'destinosturisticos'

    def __str__(self):
        return self.nombre_destino or "Destino sin nombre"

class actividadturistica(models.Model):
    Id = models.AutoField(primary_key=True)
    Id_destino_turistico = models.ForeignKey(DestinoTuristico, on_delete=models.CASCADE)
    Nombre_actividad_turistica = models.CharField(max_length=250)
    Descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'actividadturistica'