import unittest
import os
import json
from src.utils.JSONTools.JSONWriter import write_file
from src.utils.JSONTools.error import JSONWriterError

class TestJSONWriter(unittest.TestCase):

    def setUp(self):
        # This method will be run before each test
        self.json_path = "tests_file/test_rewriting.json"
    def tearDown(self):
        data = {
          "db_path": "database.db",
          "style": {
            "appearance": "dark",
            "color_theme": "dark-blue"
          }
        }

        with open(self.json_path, 'w', encoding='utf-8-sig') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def test_write_valid_file(self):
        # Test writing a valid JSON file
        data = {
          "db_path": "database.db",
          "style": {
            "appearance": "dark",
            "color_theme": "dark-blue"
          },
          "lang": "en"
        }
        write_file(self.json_path, data)
        self.assertTrue(os.path.exists(self.json_path))
        with open(self.json_path, 'r', encoding='utf-8-sig') as file:
            content = json.load(file)
            self.assertEqual(content, data)

    def test_write_invalid_path(self):
        # Test writing to an invalid path
        data = {}
        with self.assertRaises(FileNotFoundError):
            write_file("/invalid_path/test_output.json", data)

    def test_write_invalid_data(self):
        # Test writing invalid data
        with self.assertRaises(JSONWriterError):
            write_file(self.json_path, "\"lang\": \"en\"")

if __name__ == '__main__':
    unittest.main()