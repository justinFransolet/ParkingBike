import unittest
import os
import sqlite3
from src.infrastructure.database.DBCreator import create_database
from src.utils.database import DBConnect


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # This method will be run before each test
        self.db_name = create_database()
        self.db = DBConnect(self.db_name)

    def tearDown(self):
        # This method will be run after each test
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_search_request(self):
        # Insert a test record
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customer (lastname, firstname) VALUES (?, ?)", ("Doe", "John"))
        connection.commit()
        connection.close()

        # Test search_request method
        result = self.db.search_request("SELECT * FROM customer WHERE lastname = ?", ("Doe",))
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "Doe")
        print(f"Result : {result}")

    def test_changes_request(self):
        # Test changes_request method
        self.db.changes_request("INSERT INTO customer (lastname, firstname) VALUES (?, ?)", ("Smith", "Jane"))
        result = self.db.search_request("SELECT * FROM customer WHERE lastname= ?", ("Smith",))
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "Smith")
        print(f"Result : {result}")


if __name__ == '__main__':
    unittest.main()
