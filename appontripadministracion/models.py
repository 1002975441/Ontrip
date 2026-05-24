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
    Id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=False, blank=False)
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
    Vias_acceso = models.CharField(max_length=800, null=True, blank=True)
    Tipo_acceso = models.CharField(max_length=800, null=True, blank=True)
    Clima = models.TextField(null=True, blank=True)
    Recomendaciones = models.TextField(null=True, blank=True)
    Detalle_ubicacion = models.CharField(max_length=500, null=False, blank=False)
    Url_video_promocional = models.URLField(null=True, blank=True)
    Url_video_informativo = models.URLField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    email_responsable_documentacion = models.EmailField(null=True, blank=True)
    email_responsable_destino = models.EmailField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tiposturismo = models.ManyToManyField("Turismo", through='destinotipoturismo', related_name='destinos')

    class Meta:
        db_table = 'destinosturisticos'

    def __str__(self):
        return self.nombre_destino or "Destino sin nombre"

class Actividadturistica(models.Model):
    Id = models.AutoField(primary_key=True)
    Id_destino_turistico = models.ForeignKey(DestinoTuristico, on_delete=models.CASCADE, related_name='actividades')
    Nombre_actividad_turistica = models.CharField(max_length=250)
    Descripcion = models.TextField(null=True, blank=True)
    Zonas = models.CharField(max_length=250, null=True, blank=True)
    Duracion = models.CharField(max_length=250, null=True, blank=True)
    Observacion = models.TextField(null=True, blank=True)
    Recomendaciones = models.TextField(null=True, blank=True)
    Nivel = models.CharField(max_length=250, null=True, blank=True)
    Modalidad = models.CharField(max_length=250, null=True, blank=True)
    Equipamiento = models.TextField(null=True, blank=True)
    Enfoque = models.CharField(max_length=250, null=True, blank=True)
    Precio = models.CharField(max_length=250, null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'actividadturistica'
    
    def __str__(self):
        return self.Nombre_actividad_turistica
    
class fotografias(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250)
    Destino = models.ForeignKey(DestinoTuristico, on_delete=models.CASCADE, null=True, blank=True, related_name='imagenes')
    Actividad = models.ForeignKey(Actividadturistica, on_delete=models.CASCADE, null=True, blank=True, related_name='imagenes')
    Imagen = models.ImageField(upload_to='galeria/')
    Descripcion = models.CharField(max_length=250, null=True, blank=True)
    Autor = models.CharField(max_length=250, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Descripcion or "Imagen"

    class Meta:
        db_table = 'fotografias'
        
class PaqueteTuristico(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250)
    Descripcion = models.TextField(null=True, blank=True)
    Fecha_inicio = models.DateField()
    Fecha_fin = models.DateField()
    Valor_base = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'paquetesturisticos'

    def __str__(self):
        return self.Nombre

class PaqueteDestino(models.Model):
    Id_paquete = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE)
    Id_destino = models.ForeignKey(DestinoTuristico, on_delete=models.CASCADE)

    class Meta:
        db_table = 'paquete_destino'

class PaqueteActividad(models.Model):
    Id_paquete = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE)
    Id_actividad = models.ForeignKey(Actividadturistica, on_delete=models.CASCADE)

    class Meta:
        db_table = 'paquete_actividad'

class Cliente(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250)
    Correo = models.EmailField()
    Celular = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=250)
    Id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return self.Nombre

class Reserva(models.Model):
    Id = models.AutoField(primary_key=True)
    Id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Id_paquete = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE)
    Numero_personas = models.IntegerField(default=1)
    Valor_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    Descuento = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    Total = models.DecimalField(max_digits=12, decimal_places=2)
    Forma_pago = models.CharField(max_length=100)
    Vendedor = models.CharField(max_length=250)
    Fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reservas'
        
class EstablecimientoTuristico(models.Model):
    Id = models.AutoField(primary_key=True)
    Id_destino = models.ForeignKey(DestinoTuristico, on_delete=models.CASCADE, related_name='establecimientos')
    Nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    Descripcion = models.TextField(null=True, blank=True)
    Detalle_ubicacion = models.CharField(max_length=800, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'establecimientosturisticos'
        
    def __str__(self):
        return self.Nombre

class TipoAlojamiento(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250, null=False, blank=False, unique=True)
    class Meta:
        db_table = 'tipoalojamiento'
    
    def __str__(self):
        return self.Nombre
    
class Alojamiento(models.Model):
    Id = models.AutoField(primary_key=True)
    Id_establecimiento = models.ForeignKey(EstablecimientoTuristico, on_delete=models.CASCADE, related_name='alojamientos', null= True, blank=True)
    Id_destino = models.ForeignKey(DestinoTuristico, on_delete=models.CASCADE, null=True, blank=True)
    Id_tipoalojamiento = models.ForeignKey(TipoAlojamiento, on_delete=models.CASCADE, null=True, blank=True)
    Nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    Descripcion = models.TextField(null=True, blank=True)
    Detalle_ubicacion = models.CharField(max_length=800, null=False, blank=False)
    Checkin = models.TimeField(null=True, blank=True)
    Checkout = models.TimeField(null=True, blank=True)
    Numero_personas = models.IntegerField(null=True, blank=True)
    Precio = models.CharField(max_length=250, null=True, blank=True)
    
    class Meta:
        db_table = 'alojamiento'

class Turismo(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    Descripcion = models.TextField(null=True, blank=True)
    Estado = models.BooleanField(null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta: 
        db_table = 'turismo'
    
    def __str__(self):
        return self.Nombre
        
class destinotipoturismo(models.Model):
    Id = models.AutoField(primary_key=True)
    Id_turismo = models.ForeignKey(Turismo, on_delete=models.CASCADE, null=False, blank=False)
    Id_destino = models.ForeignKey(DestinoTuristico, on_delete=models.CASCADE, null=False, blank=False,
                                   related_name='destinotipoturismo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'destinotipoturismo'

class tipoproducto (models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250, null=False, blank=False)
    Descripcion = models.TextField(null=False, blank=False)

    def __str__ (self):
        return self.Nombre
    class Meta:
        db_table = 'tipoproducto'
        
class productos (models.Model):
    Id = models.AutoField(primary_key=True)
    Id_tipoproducto = models.ForeignKey(tipoproducto, on_delete=models.CASCADE, null=False, blank=False)
    Nombre = models.CharField(max_length=250, null=False, blank=False)
    Descripcion = models.TextField(null=True, blank=True)
    Envios_nacionales = models.BooleanField(null=True, blank=True)
    Envios_internacionales = models.BooleanField(null=True, blank=True)
    
    def __str__ (self):
        return self.Nombre

    class Meta: 
        db_table = 'productos'
        
class nosotros(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre_sistema = models.CharField(max_length=250, null=False, blank=False)
    Slogan = models.CharField(max_length=250, null=False, blank=False)
    Descripcion = models.TextField(null=False, blank=False)
    Objetivo = models.TextField(null=False, blank=False)
    Mision = models.TextField(null=False, blank=False)
    Vision = models.TextField(null=False, blank=False)
    Historia = models.TextField(null=False, blank=False)
    Email_contacto = models.EmailField(null=False, blank=False)
    Telefono_contacto = models.CharField(max_length=13, null=False, blank=False)
    Facebook = models.URLField(null=True, blank=True)
    Intagram = models.URLField(null=True, blank=True)
    Estado = models.BooleanField(null=False, blank=False)
    Fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'nosotros'
        
class equipotrabajo(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250, null=False, blank=False)
    Formacion_academica = models.CharField(max_length=250, null=False, blank=False)
    Cargo = models.CharField(max_length=250, null=False, blank=False)
    Descripcion = models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'equipotrabajo'
class tipoevento(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250, null= False, blank=False)

    class Meta:
        db_table = 'tipoevento'
class eventos(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=250, null=False, blank=False)
    Descripcion = models.TextField(null=False, blank=False)
    Fecha_evento = models.TextField(null=False, blank=False)
    Fecha_inicio = models.DateTimeField(null=False, blank=False)
    Fecha_fin = models.DateTimeField(null=False, blank=False)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=False, blank=False)
    Detalle_ubicacion = models.CharField(max_length=250, null=False, blank=False)
    Imagen_portada = models.ImageField(upload_to='eventos/', blank=False, null=False)
    
    class Meta:
        db_table = 'eventos'
class eventotipo (models.Model):
    Id_tipoevento = models.ForeignKey(tipoevento, on_delete=models.CASCADE)
    Id_evento = models.ForeignKey(eventos, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('Id_tipoevento', 'Id_evento')
        
    class Meta:
        db_table = 'eventotipo'