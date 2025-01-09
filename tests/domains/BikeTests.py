import unittest
from src.domains.BikeModel import *


class BikeTests(unittest.TestCase):
    def test_create_a_object_with_valid_attribute(self):
        model = "Treck"
        colour = "Red"
        is_electric = False
        bike = create_bike(model,colour,is_electric)
        self.assertEqual(bike.model, model)
        self.assertEqual(bike.colour, colour)
        self.assertEqual(bike.is_electric, is_electric)

    def test_create_a_object_with_invalid_model(self):
        model = 14
        colour = "Red"
        is_electric = False
        with self.assertRaises(AttributeError):
            create_bike(model, colour, is_electric)

        model = "A"*41
        with self.assertRaises(AttributeError):
            create_bike(model, colour, is_electric)

    def test_create_a_object_with_invalid_colour(self):
        model = "Treck"
        colour = 632
        is_electric = False
        with self.assertRaises(AttributeError):
            create_bike(model, colour, is_electric)

        colour = "A"*31
        with self.assertRaises(AttributeError):
            create_bike(model, colour, is_electric)

    def test_create_a_object_with_invalid_is_electric(self):
        model = "Treck"
        colour = "Red"
        is_electric = "Yes"
        with self.assertRaises(AttributeError):
            create_bike(model, colour, is_electric)

if __name__ == '__main__':
    unittest.main()
