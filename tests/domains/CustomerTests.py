import unittest
from src.domains.CustomerModel import create_customer

class CustomerTests(unittest.TestCase):
    def test_create_a_object_with_valid_attribute(self):
        firstname = "John"
        lastname = "Doe"
        customer = create_customer(firstname, lastname)
        self.assertEqual(customer.firstname, firstname)
        self.assertEqual(customer.lastname, lastname)

    def test_create_a_object_with_invalid_firstname(self):
        firstname = 123
        lastname = "Doe"
        with self.assertRaises(AttributeError):
            create_customer(firstname, lastname)

        firstname = "A" * 51
        with self.assertRaises(AttributeError):
            create_customer(firstname, lastname)

    def test_create_a_object_with_invalid_lastname(self):
        firstname = "John"
        lastname = 456
        with self.assertRaises(AttributeError):
            create_customer(firstname, lastname)

        lastname = "A" * 51
        with self.assertRaises(AttributeError):
            create_customer(firstname, lastname)

if __name__ == '__main__':
    unittest.main()