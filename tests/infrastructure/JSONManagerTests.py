import unittest
from src.infrastructure.JSONManager import *

class JSONManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager_valid = JSONManager("test_file/test_valid.json")
        self.manager_missing = JSONManager("test_file/test_missing.json")
        self.manager_rewriting = JSONManager("test_file/test_rewriting.json")
    def test_get_params_when_there_in_the_file(self):
        self.assertEqual(self.manager_valid.get_database_path(), "database.db")
        self.assertEqual(self.manager_valid.get_appearance(), "dark")
        self.assertEqual(self.manager_valid.get_color_theme(), "dark-blue")
        self.assertEqual(self.manager_valid.get_language(), "en")
    def test_get_params_when_there_not_in_the_fill(self):
        with self.assertRaises(ValueError):
            self.manager_missing.get_database_path()
        with self.assertRaises(ValueError):
            self.manager_missing.get_appearance()
        with self.assertRaises(ValueError):
            self.manager_missing.get_color_theme()
        with self.assertRaises(ValueError):
            self.manager_missing.get_language()
    def test_changes_params_when_there_already_not_exist_in_the_file(self):
        # Database path
        path = "database.db"
        self.manager_missing.set_database_path(path)
        self.assertEqual(path,self.manager_missing.get_database_path())

        # Appearance
        appearance = "white"
        self.manager_missing.set_appearance(appearance)
        self.assertEqual(appearance, self.manager_missing.get_appearance())

        # Color theme
        color = "green"
        self.manager_missing.set_color_theme(color)
        self.assertEqual(color, self.manager_missing.get_color_theme())

        # Language
        lang = "fr"
        self.manager_missing.set_language(lang)
        self.assertEqual(lang, self.manager_missing.get_language())

        with open("test_file/test_missing.json", 'w', encoding='utf-8-sig') as file:
            json.dump({}, file, indent=4, ensure_ascii=False)

    def test_changes_params_when_there_already_exist_in_the_file(self):
        # Database path
        old_path = self.manager_rewriting.get_database_path()
        self.manager_rewriting.set_database_path("database2.db")
        self.assertNotEqual(old_path,self.manager_rewriting.get_database_path())
        self.manager_rewriting.set_database_path(old_path)

        # Appearance
        old_appearance = self.manager_rewriting.get_appearance()
        self.manager_rewriting.set_appearance("white")
        self.assertNotEqual(old_appearance, self.manager_rewriting.get_appearance())
        self.manager_rewriting.set_appearance(old_appearance)

        # Color theme
        old_color = self.manager_rewriting.get_color_theme()
        self.manager_rewriting.set_color_theme("green")
        self.assertNotEqual(old_color, self.manager_rewriting.get_color_theme())
        self.manager_rewriting.set_color_theme(old_color)

        # Language
        old_lang = self.manager_rewriting.get_language()
        self.manager_rewriting.set_language("fr")
        self.assertNotEqual(old_lang, self.manager_rewriting.get_language())
        self.manager_rewriting.set_language(old_lang)

if __name__ == '__main__':
    unittest.main()