from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=False)
    location = models.CharField(max_length=100, blank=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.FloatField(blank=False)
    taxes = models.FloatField(blank=False)
    room_number = models.IntegerField(blank=False)
    room_type = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    available = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return f"{self.hotel.name}  Habitación numero {self.room_number}"

class Passenger(User):
    Birthdate = models.DateField(blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    DOCUMENT_CHOICES = (
        ('CC', 'Cedula de ciudadania'),
        ('CE', 'Cedula de extranjeria'),
        ('TI', 'Tarjeta de identidad'),
        ('PA', 'Pasaporte'),
    )
    Document_type = models.CharField(max_length=100, choices=DOCUMENT_CHOICES, blank=False)
    Document_number = models.CharField(unique=False, max_length=100, blank=False)
    Phone_number = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmerygencyContact(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    phone_number = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger} - {self.hotel} - {self.room}"
