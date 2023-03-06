from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.FloatField(blank=False)
    taxes = models.FloatField(blank=False)
    room_number = models.IntegerField(blank=False)
    room_type = models.CharField(max_length=100, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    capacity = models.IntegerField(blank=False, default=1)
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.location:
            self.location = self.hotel.location
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.room_number)


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_people = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return f"{self.hotel} in room {self.room} from {self.check_in} to {self.check_out}"


class Passenger(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=False)
    DOCUMENT_CHOICES = (
        ('CC', 'Cedula de ciudadania'),
        ('CE', 'Cedula de extranjeria'),
        ('TI', 'Tarjeta de identidad'),
        ('PA', 'Pasaporte'),
    )
    document_type = models.CharField(
        max_length=100, choices=DOCUMENT_CHOICES, blank=False)
    document_number = models.CharField(
        unique=False, max_length=100, blank=False)
    phone_number = models.BigIntegerField(blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmerygencyContact(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    phone_number = models.IntegerField(blank=False)

    def __str__(self):
        return self.name
