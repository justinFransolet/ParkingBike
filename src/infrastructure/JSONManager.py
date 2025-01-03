from .JSONTools.JSONReader import *
from .JSONTools.JSONWriter import *

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
        data = self.__data["database"]
        if data is None:
            raise ValueError("Database path is not found in the JSON file.")
        return data

    def set_database_path(self, path: str) -> None:
        """
        Set the database path.

        :param path: the new database path.
        """
        self.__data["database"] = path
        write_file(self.__path, self.__data)