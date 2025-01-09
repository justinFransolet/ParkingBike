import unittest
from src.utils.JSONTools.JSONReader import read_file
from src.utils.JSONTools.error import JSONReaderError

class TestJSONReader(unittest.TestCase):

    def setUp(self):
        # This method will be run before each test
        self.valid_json_path = "tests_file/test_valid.json"
        self.invalid_json_path = "tests_file/test_invalid.json"
        self.nonexistent_json_path = "tests_file/nonexistent.json"

    def test_read_valid_file(self):
        # Test reading a valid JSON file
        result = read_file(self.valid_json_path)
        self.assertEqual(result.get("db_path"), "database.db")
        self.assertEqual(result.get("lang"), "en")
        self.assertEqual(result.get("style").get("appearance"), "dark")
        self.assertEqual(result.get("style").get("color_theme"), "dark-blue")

    def test_read_invalid_file(self):
        # Test reading an invalid JSON file
        with self.assertRaises(JSONReaderError):
            read_file(self.invalid_json_path)

    def test_read_nonexistent_file(self):
        # Test reading a nonexistent JSON file
        with self.assertRaises(FileNotFoundError):
            read_file(self.nonexistent_json_path)

if __name__ == '__main__':
    unittest.main()