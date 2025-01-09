import unittest
from src.domains.ParkModel import create_park
from src.domains.BikeModel import Bike
from src.domains.CustomerModel import Customer
from datetime import datetime

class ParkTests(unittest.TestCase):
    def test_create_a_object_with_valid_attribute(self):
        # data
        bike = Bike("Model X", "Red", True)
        customer = Customer("John", "Doe")
        start_time = datetime.strptime("2023-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
        end_time2 = None
        ticket = 123

        # object
        park1 = create_park(bike, customer, start_time, end_time, ticket)
        self.assertEqual(park1.bike, bike)
        self.assertEqual(park1.customer, customer)
        self.assertEqual(park1.start_time, start_time)
        self.assertEqual(park1.end_time, end_time)
        self.assertEqual(park1.ticket, ticket)

        park2 = create_park(bike, customer, start_time, end_time2, ticket)
        self.assertEqual(park2.bike, bike)
        self.assertEqual(park2.customer, customer)
        self.assertEqual(park2.start_time, start_time)
        self.assertEqual(park2.end_time, end_time2)
        self.assertEqual(park2.ticket, ticket)

    def test_create_a_object_with_invalid_bike(self):
        customer = Customer("John", "Doe")
        start_time = datetime.strptime("2023-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
        end_time = None
        ticket = 123
        with self.assertRaises(AttributeError):
            create_park("Invalid Bike", customer, start_time, end_time, ticket)

    def test_create_a_object_with_invalid_customer(self):
        bike = Bike("Model X", "Red", True)
        start_time = datetime.strptime("2023-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
        end_time = None
        ticket = 123
        with self.assertRaises(AttributeError):
            create_park(bike, "Invalid Customer", start_time, end_time, ticket)

    def test_create_a_object_with_invalid_start_time(self):
        bike = Bike("Model X", "Red", True)
        customer = Customer("John", "Doe")
        end_time = None
        ticket = 123
        with self.assertRaises(AttributeError):
            create_park(bike, customer, "Invalid Start Time", end_time, ticket)

    def test_create_a_object_with_invalid_end_time(self):
        bike = Bike("Model X", "Red", True)
        customer = Customer("John", "Doe")
        start_time = datetime.strptime("2023-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
        ticket = 123
        with self.assertRaises(AttributeError):
            create_park(bike, customer, start_time, "Invalid End Time", ticket)

    def test_create_a_object_with_invalid_ticket(self):
        bike = Bike("Model X", "Red", True)
        customer = Customer("John", "Doe")
        start_time = datetime.strptime("2023-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
        end_time = None
        with self.assertRaises(AttributeError):
            create_park(bike, customer, start_time, end_time, "Ticket123")

if __name__ == '__main__':
    unittest.main()