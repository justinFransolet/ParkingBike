import unittest
import os
import sqlite3
from datetime import datetime
from src.infrastructure.database.DBCreator import create_database

class TestDBCreator(unittest.TestCase):

    def setUp(self):
        # This method will be run before each test
        self.db_name = create_database()

    def tearDown(self):
        # This method will be run after each test
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_database_creation(self):
        # Test if the database file is created
        self.assertTrue(os.path.exists(self.db_name))

    def test_customer_table_creation(self):
        # Test if the customer table is created
        connection = None
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='customer';")
            self.assertIsNotNone(cursor.fetchone())
        except sqlite3.Error as error:
            print(f"Error during the test: {error}")
        finally:
            if connection:
                connection.close()

    def test_bike_table_creation(self):
        # Test if the bike table is created
        connection = None
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bike';")
            self.assertIsNotNone(cursor.fetchone())
        except sqlite3.Error as error:
            print(f"Error during the test: {error}")
        finally:
            if connection:
                connection.close()

    def test_park_table_creation(self):
        # Test if the park table is created
        connection = None
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='park';")
            self.assertIsNotNone(cursor.fetchone())
        except sqlite3.Error as error:
            print(f"Error during the test: {error}")
        finally:
            if connection:
                connection.close()

    def test_filename_format(self):
        # Test if the database name has the correct format
        current_date = datetime.now().strftime("%Y%m%d")
        expected_name = f"parking_{current_date}.db"
        self.assertEqual(self.db_name, expected_name)

if __name__ == '__main__':
    unittest.main()
