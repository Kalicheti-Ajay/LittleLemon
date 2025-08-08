from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuItemSerializer,BookingSerializer

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='Test-User',password='Test@pass')
        self.client.force_authenticate(user=self.user)

        self.Menu1 = Menu.objects.create(Title='Lemon Dessert',Price=10.75,Inventory=15)
        self.Menu2 = Menu.objects.create(Title='Grilled Fish',Price=15.50,Inventory=20)
        self.Menu3 = Menu.objects.create(Title='Cappuccino',Price=15.25,Inventory=25)

    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        
        menu_items = Menu.objects.all()
        serialized_data = MenuItemSerializer(menu_items,many=True)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,serialized_data.data)

class BookingViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='Test-User',password='Test@pass')
        self.client.force_authenticate(user=self.user)

        self.Booking1 = Booking.objects.create(Name='Mark',No_of_guests=2,BookingDate='2025-08-10T00:00:00Z')
        self.Booking2 = Booking.objects.create(Name='Ajay',No_of_guests=4,BookingDate='2025-09-03T00:00:00Z')
        self.Booking3 = Booking.objects.create(Name='Steeve',No_of_guests=2,BookingDate='2025-08-09T00:00:00Z')

    def test_getall(self):
        response = self.client.get('/restaurant/booking/tables/')

        bookings = Booking.objects.all()
        serialized_data = BookingSerializer(bookings,many=True)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,serialized_data.data)

