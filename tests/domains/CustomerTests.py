import unittest


class CustomerTests(unittest.TestCase):
    def test_create_a_object_with_valid_attribute(self):
        self.assertEqual(True, False)

    def test_create_a_object_with_invalid_firstname(self):
        self.assertEqual(True, False)

    def test_create_a_object_with_invalid_lastname(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
