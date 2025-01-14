from src.app import ParkingBikeApp
from src.controller import ParkingPanelController
from src.infrastructure import JSONManager, BikeRepository, CustomerRepository, ParkRepository, RepositoriesManager
from src.utils.database import DBConnect


class HomeController:
    """
    This class is the controller of the home app.
    """
    def __init__(self,path_params: str, path_db: str)-> None:
        """
        Constructor of the controller of the home app.

        :param path_params: The path of the parameters file.
        :param path_db: The path of the database file.
        """
        self.json_manager = JSONManager(path_params)
        self.db_connect = DBConnect(path_db)

    def open_visualizer(self)-> None:
        """
        Open the visualizer app.
        """
        # TODO : Implement the visualizer app
        pass

    def open_parking(self)-> None:
        """
        Open the parking app.
        """
        # Repository
        bike = BikeRepository(self.db_connect)
        customer = CustomerRepository(self.db_connect)
        park = ParkRepository(self.db_connect)
        repositories = RepositoriesManager(bike, customer, park)
        # Controller
        controller = ParkingPanelController(repositories)
        # App
        ParkingBikeApp(controller, self.get_selected_appearance(), self.get_color_theme(), 800, 600).mainloop()

    def open_analyzer(self)-> None:
        """
        Open the analyzer app.
        """
        # TODO : Implement the analyzer app
        pass

    def changes_theme(self, param: str)-> bool:
        """
        Change the theme of the app.

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
        Change the language of the app.

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