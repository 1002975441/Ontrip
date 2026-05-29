
from django.contrib.admin import AdminSite


class OnTripAdminSite(AdminSite):

    site_header = "Administración OnTrip"
    site_title = "OnTrip Admin"
    index_title = "Panel administrativo"
    
    

    def get_app_list(self, request):

        app_dict = self._build_app_dict(request)

        modelos = app_dict.get('appontripadministracion', {}).get('models', [])

        estructura = []
        informacion_turistica = []
        eventos = []
        paquetes = []
        reservas = []
        alojamientos = []
        productos = []

        for model in modelos:

            nombre = model['object_name']

            if nombre == 'Pais':
                model['name'] = '1️ Registrar País'
                estructura.append(model)

            elif nombre == 'Region':
                model['name'] = '2️ Registrar Región'
                estructura.append(model)

            elif nombre == 'Departamento':
                model['name'] = '3️ Registrar Departamento'
                estructura.append(model)

            elif nombre == 'Municipio':
                model['name'] = '4️ Registrar Municipio'
                estructura.append(model)

            elif nombre == 'DestinoTuristico':
                model['name'] = '1️ Registrar Destino Turístico'
                informacion_turistica.append(model)

            elif nombre == 'Actividadturistica':
                model['name'] = '2️ Registrar Actividades Turísticas'
                informacion_turistica.append(model)

            elif nombre == 'atractivoturistico':
                model['name'] = '3️ Registrar Atractivos Turísticos'
                informacion_turistica.append(model)

            elif nombre == 'Turismo':
                model['name'] = '4️ Registrar Tipo de Turismo'
                informacion_turistica.append(model)

            elif nombre == 'destinotipoturismo':
                model['name'] = '5️ Relacionar Destino y Turismo'
                informacion_turistica.append(model)

            elif nombre == 'fotografias':
                model['name'] = '6️ Registrar Fotografías'
                informacion_turistica.append(model)

            elif nombre == 'tipoevento':
                model['name'] = '1️ Registrar Tipo de Evento'
                eventos.append(model)

            elif nombre == 'eventos':
                model['name'] = '2️ Registrar Eventos'
                eventos.append(model)

            elif nombre == 'eventotipo':
                model['name'] = '3️ Relacionar Evento y Tipo'
                eventos.append(model)

            elif nombre == 'PaqueteTuristico':
                model['name'] = '1️ Registrar Paquetes Turísticos'
                paquetes.append(model)

            elif nombre == 'PaqueteDestino':
                model['name'] = '2️ Relacionar Paquete y Destino'
                paquetes.append(model)

            elif nombre == 'PaqueteActividad':
                model['name'] = '3️ Relacionar Paquete y Actividad'
                paquetes.append(model)

            elif nombre == 'Cliente':
                model['name'] = '1️ Registrar Clientes'
                reservas.append(model)

            elif nombre == 'Reserva':
                model['name'] = '2️ Registrar Reservas'
                reservas.append(model)

            elif nombre == 'EstablecimientoTuristico':
                model['name'] = '1️ Registrar Establecimientos'
                alojamientos.append(model)

            elif nombre == 'TipoAlojamiento':
                model['name'] = '2️ Registrar Tipos de Alojamiento'
                alojamientos.append(model)

            elif nombre == 'Alojamiento':
                model['name'] = '3️ Registrar Alojamientos'
                alojamientos.append(model)


            elif nombre == 'tipoproducto':
                model['name'] = '1️ Registrar Tipo de Producto'
                productos.append(model)

            elif nombre == 'productos':
                model['name'] = '2️ Registrar Productos'
                productos.append(model)

        return [

            {
                'name': 'Estructura Organizacional',
                'app_label': 'estructura',
                'models': estructura,
            },

            {
                'name': 'Información Turística',
                'app_label': 'turismo',
                'models': informacion_turistica,
            },

            {
                'name': 'Eventos',
                'app_label': 'eventos',
                'models': eventos,
            },

            {
                'name': 'Paquetes Turísticos',
                'app_label': 'paquetes',
                'models': paquetes,
            },

            {
                'name': 'Clientes y Reservas',
                'app_label': 'reservas',
                'models': reservas,
            },

            {
                'name': 'Alojamientos',
                'app_label': 'alojamientos',
                'models': alojamientos,
            },

            {
                'name': 'Productos',
                'app_label': 'productos',
                'models': productos,
            }

        ]


admin_site = OnTripAdminSite(name='ontrip_admin')
