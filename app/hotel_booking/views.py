from rest_framework import viewsets
from rest_framework.response import Response
from .models import Hotel, Room, Passenger, EmerygencyContact, Booking, Location
from .serializers import HotelSerializer, RoomSerializer, PassengerSerializer, EmerygencyContactSerializer, BookingSerializer, LocationSerializer
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk):
        location = Location.objects.get(pk=pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        location = Location.objects.get(pk=pk)
        location.delete()
        return Response("Location deleted successfully")

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def list(self, request):
        hotel_queryset = Hotel.objects.all()
        booking_queryset = Booking.objects.all()
        room_queryset = Room.objects.all()
        if 'location' in request.query_params:
            hotel_queryset = hotel_queryset.filter(
                location=request.query_params['location'])
        if 'check_in' in request.query_params:
            check_in_queryset = booking_queryset.filter(
                check_in__lte=request.query_params['check_in'])
            if not check_in_queryset:
                return Response("No hotels available in this date")
        if 'check_out' in request.query_params:
            check_out_queryset = booking_queryset.filter(
                check_out__lte=request.query_params['check_out'])
            if not check_out_queryset:
                return Response("No hotels available in this date")
        if 'capacity' in request.query_params:
            room_queryset = room_queryset.filter(
                capacity=request.query_params['capacity'])
            if not room_queryset:
                return Response("No hotels available with this capacity")
        hotel_queryset = hotel_queryset.filter(available=True)
        serializer = HotelSerializer(hotel_queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        hotel.delete()
        return Response("Hotel deleted successfully")


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.delete()
        return Response("Room deleted successfully")


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

    def list(self, request):
        queryset = Passenger.objects.all()
        serializer = PassengerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk):
        passenger = Passenger.objects.get(pk=pk)
        serializer = PassengerSerializer(passenger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        passenger = Passenger.objects.get(pk=pk)
        passenger.delete()
        return Response("Passenger deleted successfully")


class EmerygencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmerygencyContact.objects.all()
    serializer_class = EmerygencyContactSerializer

    def list(self, request):
        queryset = EmerygencyContact.objects.all()
        serializer = EmerygencyContactSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmerygencyContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk):
        emerygency_contact = EmerygencyContact.objects.get(pk=pk)
        serializer = EmerygencyContactSerializer(
            emerygency_contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        emerygency_contact = EmerygencyContact.objects.get(pk=pk)
        emerygency_contact.delete()
        return Response("Emerygency Contact deleted successfully")


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            passenger = Passenger.objects.get(pk=request.data['passenger'])
            hotel = Hotel.objects.get(pk=request.data['hotel'])
            room = Room.objects.get(pk=request.data['room'])

            booking = Booking.objects.filter(
                room=room, check_in__lte=request.data['check_in'], check_out__gte=request.data['check_out'])
            if booking.exists():
                return Response("The room is not available on these dates")
            serializer.save()
            try:
                send_mail(
                    'Booking Confirmation',
                    f'Your booking has been confirmed! in hotel {hotel.name} in room {room}',
                    'sebasmh2002@hotmail.com',
                    [passenger.email])
            except:
                return Response("Booking created successfully, but email not sent")
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response("Booking deleted successfully")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = ['Medellín', 'Bogota']

        return context

