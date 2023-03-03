from rest_framework import viewsets
from rest_framework.response import Response
from .models import Hotel, Room, Passenger, EmerygencyContact, Booking
from .serializers import HotelSerializer, RoomSerializer, PassengerSerializer, EmerygencyContactSerializer, BookingSerializer
from django.core.mail import send_mail


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def list(self, request):
        queryset = Hotel.objects.all()
        serializer = HotelSerializer(queryset, many=True)
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
