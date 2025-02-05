﻿import unittest
from src.domains.BikeModel import *


class BikeTests(unittest.TestCase):
    def test_create_a_object_with_valid_attribute(self):
        id_bike = 1
        model = "Treck"
        colour = "Red"
        is_electric = False
        bike = create_bike(id_bike,model,colour,is_electric)
        self.assertEqual(bike.model, model)
        self.assertEqual(bike.colour, colour)
        self.assertEqual(bike.is_electric, is_electric)
        self.assertEqual(bike.id, id_bike)

    def test_create_a_object_with_invalid_model(self):
        id_bike = 1
        model = 14
        colour = "Red"
        is_electric = False
        with self.assertRaises(AttributeError):
            create_bike(id_bike, model, colour, is_electric)

        model = "A"*41
        with self.assertRaises(AttributeError):
            create_bike(id_bike, model, colour, is_electric)

    def test_create_a_object_with_invalid_colour(self):
        id_bike = 1
        model = "Treck"
        colour = 632
        is_electric = False
        with self.assertRaises(AttributeError):
            create_bike(id_bike, model, colour, is_electric)

        colour = "A"*31
        with self.assertRaises(AttributeError):
            create_bike(id_bike, model, colour, is_electric)

    def test_create_a_object_with_invalid_is_electric(self):
        id_bike = 1
        model = "Treck"
        colour = "Red"
        is_electric = "Yes"
        with self.assertRaises(AttributeError):
            create_bike(id_bike, model, colour, is_electric)

    def test_create_a_object_with_invalid_id(self):
        id_bike = -1
        model = "Treck"
        colour = "Red"
        is_electric = True
        with self.assertRaises(AttributeError):
            create_bike(id_bike, model, colour, is_electric)

if __name__ == '__main__':
    unittest.main()
