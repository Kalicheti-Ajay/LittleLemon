from django.test import TestCase
from restaurant.models import Menu,Booking

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="Ice Creame",Price=15.75,Inventory=10)
        self.assertEqual(str(item),'Ice Creame : 15.75')
        
class BookingTest(TestCase):
    def test_get_booking(self):
        booking_details = Booking.objects.create(Name='Mark',No_of_guests=4,BookingDate='2025-8-10T00:00:00Z')
        self.assertEqual(str(booking_details),'Mark : 4')