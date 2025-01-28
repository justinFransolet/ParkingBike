from customtkinter import CTk
from src.infrastructure import JSONManager, BikeRepository, CustomerRepository, ParkRepository, RepositoriesManager
from src.utils.database import DBConnect


class HomeController:
    """
    This class is the controller of the home view.
    """
    def __init__(self,path_params: str, path_db: str)-> None:
        """
        Constructor of the controller of the home view.

        :param path_params: The path of the parameters file.
        :param path_db: The path of the database file.
        """
        self.json_manager = JSONManager(path_params)
        self.db_connect = DBConnect(path_db)

    def open_visualizer(self,app: CTk)-> None:
        """
        Open the visualizer view.

        :param app: The application object.
        """
        # TODO : Implement the visualizer view
        raise NotImplementedError("The visualizer view is not implemented yet.")

    def open_parking(self, app: CTk)-> None:
        """
        Open the parking view.

        :param app: The application object.
        """
        from src.view import ParkingPanel
        from src.controller import ParkingPanelController
        # Repository
        bike = BikeRepository(self.db_connect)
        customer = CustomerRepository(self.db_connect)
        park = ParkRepository(self.db_connect)
        repositories = RepositoriesManager(bike, customer, park)
        # Controller
        controller = ParkingPanelController(repositories)
        # App
        ParkingPanel(app,controller, self.get_selected_appearance(), self.get_color_theme(), 1300, 700)

    def open_analyzer(self, app: CTk)-> None:
        """
        Open the analyzer view.

        :param app: The application object.
        """
        # TODO : Implement the analyzer view
        raise NotImplementedError("The analyzer view is not implemented yet.")

    def changes_theme(self, param: str)-> bool:
        """
        Change the theme of the view.

        :param param: The choose theme.
        :return: True if the theme is changed, False otherwise.
        """
        if param == "dark":
            self.json_manager.set_appearance("dark")
            self.json_manager.set_color_theme("dark-blue")
            return True
        elif param == "light":
            self.json_manager.set_appearance("light")
            self.json_manager.set_color_theme("dark-blue")
            return True
        else:
            return False

    def changes_lang(self, param: str)-> bool:
        """
        Change the language of the view.

        :param param: The choose language.
        :return: True if the language is changed, False otherwise.
        """
        if param == "fr":
            self.json_manager.set_language("fr")
            return True
        elif param == "en":
            self.json_manager.set_language("en")
            return True
        else:
            return False

    def get_selected_lang(self)-> str:
        """
        Get the selected language.

        :return: The selected language.
        """
        try:
            return self.json_manager.get_language()
        except Exception as e:
            raise Exception(str(e))

    def get_selected_appearance(self)-> str:
        """
        Get the selected theme.

        :return: The selected theme.
        """
        try:
            return self.json_manager.get_appearance()
        except Exception as e:
            raise Exception(str(e))

    def get_color_theme(self)-> str:
        """
        Get the color theme.

        :return: The color theme.
        """
        try:
            return self.json_manager.get_color_theme()
        except Exception as e:
            raise Exception(str(e))