from rest_framework import routers
from .views import HotelViewSet, RoomViewSet, PassengerViewSet, EmerygencyContactViewSet, BookingViewSet

router = routers.SimpleRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'passengers', PassengerViewSet)
router.register(r'emergency_contacts', EmerygencyContactViewSet)
router.register(r'bookings', BookingViewSet)
urlpatterns = router.urls
