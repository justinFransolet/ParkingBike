from src.utils.JSONTools import *

class JSONManager:
    """
    JSONManager class is responsible for managing JSON files.
    """

    def __init__(self, path: str):
        """
        Constructor for JSONManager class.

        :param path: the path of the JSON file.
        """
        self.__path = path
        self.__data = read_file(path)

    def get_database_path(self) -> str:
        """
        Get the database path.

        :raise ValueError: if the database path is not found in the JSON file.

        :return: the database path.
        """
        try:
            return self.__data["db_path"]
        except KeyError:
            raise ValueError("Database path is not found in the JSON file.")

    def get_appearance(self) -> str:
        """
        Get the name of the appearance.

        :raise ValueError: if the name of the appearance is not found in the JSON file.

        :return: the name of the appearance.
        """
        try:
            return self.__data["style"]["appearance"]
        except KeyError:
            raise ValueError("The name of the appearance is not found in the JSON file.")

    def get_color_theme(self) -> str:
        """
        Get the color theme.

        :raise ValueError: if the color theme is not found in the JSON file.

        :return: the color theme.
        """
        try:
            return self.__data["style"]["color_theme"]
        except KeyError:
            raise ValueError("Color theme is not found in the JSON file.")

    def get_language(self) -> str:
        """
        Get the language.

        :raise ValueError: if the language is not found in the JSON file.

        :return: the language.
        """
        try:
            return self.__data["lang"]
        except KeyError:
            raise ValueError("Language is not found in the JSON file.")

    def set_database_path(self, path: str) -> None:
        """
        Set the database path.

        :param path: the new database path.
        """
        self.__data["db_path"] = path
        write_file(self.__path, self.__data)

    def set_appearance(self, appearance: str) -> None:
        """
        Set the appearance.

        :param appearance: the new appearance.
        """
        try:
            self.__data["style"]["appearance"] = appearance
        except KeyError:
            self.__data["style"] = {}
            self.__data["style"]["appearance"] = appearance
        write_file(self.__path, self.__data)

    def set_color_theme(self, color: str) -> None:
        """
        Set the color theme.

        :param color: the new color theme.
        """
        try:
            self.__data["style"]["color_theme"] = color
        except KeyError:
            self.__data["style"] = {}
            self.__data["style"]["color_theme"] = color
        write_file(self.__path, self.__data)

    def set_language(self, language: str) -> None:
        """
        Set the language.

        :param language: the new langue.
        """
        self.__data["lang"] = language
        write_file(self.__path, self.__data)