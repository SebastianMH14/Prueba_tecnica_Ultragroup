from rest_framework import serializers
from hotel_booking.models import Hotel, Room, Passenger, EmerygencyContact, Booking


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.available = validated_data.get(
            'available', instance.available)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.hotel = validated_data.get('hotel', instance.hotel)
        instance.price = validated_data.get('price', instance.price)
        instance.taxes = validated_data.get('taxes', instance.taxes)
        instance.room_number = validated_data.get(
            'room_number', instance.room_number)
        instance.room_type = validated_data.get(
            'room_type', instance.room_type)
        instance.location = validated_data.get('location', instance.location)
        instance.available = validated_data.get(
            'available', instance.available)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

    def create(self, validated_data):
        return Passenger.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.birth_date = validated_data.get(
            'Birthdate', instance.Birthdate)
        instance.gender = validated_data.get('Gender', instance.Gender)
        instance.document_type = validated_data.get(
            'Document_type', instance.Document_type)
        instance.document_number = validated_data.get(
            'Document_number', instance.Document_number)
        instance.phone_number = validated_data.get(
            'Phone_number', instance.Phone_number)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


class EmerygencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmerygencyContact
        fields = '__all__'

    def create(self, validated_data):
        return EmerygencyContact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.passenger = validated_data.get(
            'passenger', instance.passenger)
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        Room.objects.filter(
            id=validated_data['room'].id).update(available=False)
        return Booking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.room = validated_data.get('room', instance.room)
        instance.passenger = validated_data.get(
            'passenger', instance.passenger)
        instance.check_in = validated_data.get('check_in', instance.check_in)
        instance.check_out = validated_data.get(
            'check_out', instance.check_out)
        instance.save()
        return instance

    def delete(self, instance):
        Room.objects.filter(id=instance.room.id).update(available=True)
        instance.delete()
        return instance
