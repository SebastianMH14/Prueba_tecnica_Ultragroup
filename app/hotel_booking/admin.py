from django.contrib import admin

from .models import Hotel, Room, Passenger, EmerygencyContact, Booking


admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Passenger)
admin.site.register(EmerygencyContact)
admin.site.register(Booking)