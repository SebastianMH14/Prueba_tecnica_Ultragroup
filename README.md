# Prueba Técnica - Desarrollador  Backend
## UltraGruop

Sistema de reservas

## Instrucciones

## para correr el proyecto en local

Use [git](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) para clonar este repositorio en su máquina local. 
Primero clona el repositorio y descarga las funcionalidades necesarias:

```bash
git clone https://github.com/SebastianMH14/Prueba_tecnica_Ultragroup
```

```bash
git checkout develop
```

Necesitas tener instalado Python

1.  Crear un entorno virtual con `python -m venv venv`
2.  activar el entorno virtual con `source venv/bin/activate`
3.  instalar las dependencias con `pip install -r requirements/requirements.txt`
4.  crear la base de datos con `python manage.py makemigrations`
5.  migrar la base de datos con `python manage.py migrate`
7.  correr el servidor con `python manage.py runserver`


## Endpoints


#

    Ubicaciones

- Listar todos las ubicaciones GET `https://pruebatecnicaultragroup-production.up.railway.app/locations `

- Buscar una ubicación  por id GET `https://pruebatecnicaultragroup-production.up.railway.app/locations/<id> `

- Crear una ubicación POST `https://pruebatecnicaultragroup-production.up.railway.app/locations/`

- Actualizar la información de una ubicación PUT `https://pruebatecnicaultragroup-production.up.railway.app/locations/<id> `

- Eliminar una ubicación DELETE `https://pruebatecnicaultragroup-production.up.railway.app/locations/<id> `

    Hoteles

- Listar todos los Hoteles GET `https://pruebatecnicaultragroup-production.up.railway.app/hotels `

- Buscar un hotel por id GET `https://pruebatecnicaultragroup-production.up.railway.app/hotels/<id> `

- Crear un hotel POST `https://pruebatecnicaultragroup-production.up.railway.app/hotels`

- Actualizar la información de un Hotel PUT `https://pruebatecnicaultragroup-production.up.railway.app/hotels/<id> `

- Eliminar un hotel DELETE `https://pruebatecnicaultragroup-production.up.railway.app/hotels/<id> `

#

    Habitaciones

- Listar todos las habitaciones GET `https://pruebatecnicaultragroup-production.up.railway.app/rooms `

- Buscar una habitación por id GET `https://pruebatecnicaultragroup-production.up.railway.app/rooms/<id> `

- Crear una habitación POST `https://pruebatecnicaultragroup-production.up.railway.app/rooms`

- Actualizar la información de una habitación PUT `https://pruebatecnicaultragroup-production.up.railway.app/rooms/<id> `

- Eliminar una habitación DELETE `https://pruebatecnicaultragroup-production.up.railway.app/rooms/<id> `

#

    Reservas

- Listar todos las reservas GET `https://pruebatecnicaultragroup-production.up.railway.app/bookings/ `

- Buscar una reserva por id GET `https://pruebatecnicaultragroup-production.up.railway.app/bookings/<id> `

- Crear una reserva POST `https://pruebatecnicaultragroup-production.up.railway.app/bookings`

- Actualizar la información de una reserva PUT `https://pruebatecnicaultragroup-production.up.railway.app/bookings/<id> `

- Eliminar una reserva DELETE `https://pruebatecnicaultragroup-production.up.railway.app/bookings/<id> `

#

    Reservas

- Listar todos las reservas GET `https://pruebatecnicaultragroup-production.up.railway.app/bookings/ `

- Buscar una reserva por id GET `https://pruebatecnicaultragroup-production.up.railway.app/bookings/<id> `

- Crear una reserva POST `https://pruebatecnicaultragroup-production.up.railway.app/bookings`

- Actualizar la información de una reserva PUT `https://pruebatecnicaultragroup-production.up.railway.app/bookings/<id> `

- Eliminar una reserva DELETE `https://pruebatecnicaultragroup-production.up.railway.app/bookings/<id> `

#

    Pasajeros

- Listar todos los pasajeros GET `https://pruebatecnicaultragroup-production.up.railway.app/passengers/ `

- Buscar un pasajero por id GET `https://pruebatecnicaultragroup-production.up.railway.app/passengers/<id> `

- Crear un pasajero POST `https://pruebatecnicaultragroup-production.up.railway.app/passengers`

- Actualizar la información de un pasajero PUT `https://pruebatecnicaultragroup-production.up.railway.app/passengers/<id> `

- Eliminar un pasajero DELETE `https://pruebatecnicaultragroup-production.up.railway.app/passengers/<id> `

#

    Contacto de emergencia

- Listar todos los contactos de emergencia GET `https://pruebatecnicaultragroup-production.up.railway.app/emergency_contacts/ `

- Buscar un contacto de emergencia por id GET `https://pruebatecnicaultragroup-production.up.railway.app/emergency_contacts/<id> `

- Crear un contacto de emergencia POST `https://pruebatecnicaultragroup-production.up.railway.app/emergency_contacts`

- Actualizar la información de un contacto de emergencia PUT `https://pruebatecnicaultragroup-production.up.railway.app/emergency_contacts/<id> `

- Eliminar un contacto de emergencia DELETE `https://pruebatecnicaultragroup-production.up.railway.app/emergency_contacts/<id> `

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
1 - No cree un modelo para agentes de viajes, ya que esto es un sistema de autenticacion, y por practicidad para entender el sistema no lo implemente.
#
2 - Creo que la forma en la que se envia el email no es la que se debería usar en producción, ya que no se envia de forma asincrona, y puede cargar mucho el backend, considero que se debe hacer por medio de un service worker, o un sistema de colas, al ser esto una prueba no lo implemente, aun asi, el email se envia correctamente y al ser un sistema de prueba no hay ningun problema con eso.
#
3 - En producción use la base de datos PostgreSQL, pero localmente use SQLite, ya que es mas facil de instalar y configurar, y no es necesario tener un servidor de base de datos instalado.
## Desarrollado con:

- [Python](https://www.python.org/) - Lenguaje interpretado de programaciòn Python.
- [Django](https://www.djangoproject.com/) - Framework para aplicaciones web con Python.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Herramienta para construir API con Django.
- [SQLite](https://www.postgresql.org/) - Motor de base de datos SQL.