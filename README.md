# Prueba Técnica - Desarrollador  Backend
## UltraGruop

Sistema de reservas

## Instrucciones

Use [git](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) para clonar este repositorio en su máquina local. 
Primero clona el repositorio y descarga las funcionalidades necesarias:

```bash
git clone https://github.com/SebastianMH14/Prueba_tecnica_Ultragroup
```

Necesitas tener instalado Python

1.  crear un entorno virtual con `python -m venv venv`
2.  activar el entorno virtual con `source venv/bin/activate`
3.  instalar las dependencias con `pip install -r requirements/requirements.txt`
4.  crear la base de datos con `python manage.py makemigrations`
5.  migrar la base de datos con `python manage.py migrate`
7.  correr el servidor con `python manage.py runserver`


## Endpoints

    Hoteles

- Listar todos los Hoteles GET `http://localhost:8000/hotels `

- Buscar un hotel por id GET `http://localhost:8000/hotels/<id> `

- Crear un hotel POST `http://localhost:8000/hotels`

- Actualizar la información de un Hotel PUT `http://localhost:8000/hotels/<id> `

- Eliminar un hotel DELETE `http://localhost:8000/hotels/<id> `

#

    Habitaciones

- Listar todos las habitaciones GET `http://localhost:8000/rooms `

- Buscar una habitación por id GET `http://localhost:8000/rooms/<id> `

- Crear una habitación POST `http://localhost:8000/rooms`

- Actualizar la información de una habitación PUT `http://localhost:8000/rooms/<id> `

- Eliminar un rooms DELETE `http://localhost:8000/rooms/<id> `

#

    Reservas

- Listar todos las reservas GET `http://localhost:8000/bookings/ `

- Buscar una reserva por id GET `http://localhost:8000/bookings/<id> `

- Crear una reserva POST `http://localhost:8000/bookings`

- Actualizar la información de una reserva PUT `http://localhost:8000/bookings/<id> `

- Eliminar una reserva DELETE `http://localhost:8000/bookings/<id> `

#

    Reservas

- Listar todos las reservas GET `http://localhost:8000/bookings/ `

- Buscar una reserva por id GET `http://localhost:8000/bookings/<id> `

- Crear una reserva POST `http://localhost:8000/bookings`

- Actualizar la información de una reserva PUT `http://localhost:8000/bookings/<id> `

- Eliminar una reserva DELETE `http://localhost:8000/bookings/<id> `

#

    Pasajeros

- Listar todos los pasajeros GET `http://localhost:8000/passengers/ `

- Buscar un pasajero por id GET `http://localhost:8000/passengers/<id> `

- Crear un pasajero POST `http://localhost:8000/passengers`

- Actualizar la información de un pasajero PUT `http://localhost:8000/passengers/<id> `

- Eliminar un pasajero DELETE `http://localhost:8000/passengers/<id> `

#

    Contacto de emergencia

- Listar todos los contactos de emergencia GET `http://localhost:8000/emergency_contacts/ `

- Buscar un contacto de emergencia por id GET `http://localhost:8000/emergency_contacts/<id> `

- Crear un contacto de emergencia POST `http://localhost:8000/emergency_contacts`

- Actualizar la información de un contacto de emergencia PUT `http://localhost:8000/emergency_contacts/<id> `

- Eliminar un contacto de emergencia DELETE `http://localhost:8000/emergency_contacts/<id> `

## Flujo de la aplicación
- Crear un hotel, si la ubicacion no existe, se debe crear una nueva ubicación.
- Crear una habitación para el hotel creado.
- Crear una reserva
- Crear uno o más pasajeros para la reserva creada.
- Crear un contacto de emergencia para cada pasajero creado.


### Ejemplos


    Body para la creación de hoteles

```
{
    "name": "",
    "available": false,
    "location": null
}
```

    Body para la creación de habitaciones

```

{
    "price": null,
    "taxes": null,
    "room_number": null,
    "room_type": "",
    "capacity": null,
    "available": false,
    "hotel": null,
    "location": null
}
```

    Body para la creación de reservas

```
{
    "check_in": null,
    "check_out": null,
    "number_of_people": null,
    "hotel": null,
    "room": null
}
```

    Body para la creación de pasajeros

```
{
    "first_name": "",
    "last_name": "",
    "email": "",
    "birth_date": null,
    "gender": null,
    "document_type": null,
    "document_number": "",
    "phone_number": null,
    "booking": null
}
```

    Body para la creación de contactos de emergencia

```
{
    "name": "",
    "phone_number": null,
    "passenger": null
}
```


## Aclaraciones
1 - No cree un modelo para agentes de viajes, ya que esto es casi un sistema de autenticacion, y por practicidad para entender el sistema no lo implemente.
#
2 - Creo que la forma en la que se envia el email no es la que se debería usar en producción, ya que no se envia de forma asincrona, y puede cargar mucho el backend, considero que se debe hacer por medio de un service worker, o un sistema de colas, al ser esto una prueba no lo implemente, aun asi, el email se envia correctamente y al ser un sistema de prueba no hay ningun problema con eso.
#
3 - Use sqlite para la base de datos, ya que es una base de datos que viene por defecto con django, y no es necesario instalar nada para usarla, pero si se desea usar otra base de datos, solo se debe cambiar el archivo settings.py, y cambiar la configuración de la base de datos. Esto con el fin de facilitar la instalación y configuración del proyecto, y que pueda ser probado en cualquier computador.
#
4 - La forma en que se manejan las ubicaciones es demasiado basica, en un caso real se deberían tener 3 tablas en nuesta base de datos, 1 para país, 1 para ciudad, y 1 para ubicación, lo hice por temas de practicidad, y para que el proyecto sea mas facil de entender.

## Desarrollado con:

- [Python](https://www.python.org/) - Lenguaje interpretado de programaciòn Python.
- [Django](https://www.djangoproject.com/) - Framework para aplicaciones web con Python.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Herramienta para construir API con Django.
- [SQLite](https://www.postgresql.org/) - Motor de base de datos SQL.