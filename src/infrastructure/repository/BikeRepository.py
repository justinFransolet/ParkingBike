from src.utils.database.DBConnect import DBConnect


class BikeRepository:
    """
    This class is used to interact with the database to get the bikes.
    """
    def __init__(self, db: DBConnect):
        """
        This is the constructor of the class.
        :param db: This is the object to interact with the database.
        """
        self.__db = db

    def get_all_bike(self)-> list:
        """
        This method is used to get all the bikes from the database.

        :raises ValueError: If no bike found in the database.

        :return: It returns the list of bikes.
        """
        request = """SELECT * FROM bike"""
        result = self.__db.search_request(request,())
        if result is not None:
            return result
        else:
            raise ValueError("No bike found")

    def get_bike_by_id(self, bike_id: int)-> dict:
        """
        This method is used to get a bike by id from the database.

        :param bike_id: This is the id of the bike.

        :raises ValueError: If no bike found in the database.

        :return: It returns the bike.
        """
        request = """SELECT * FROM bike WHERE id = ?"""
        result = self.__db.search_request(request, (bike_id,))
        if result is not None:
            return result[0]
        else:
            raise ValueError("Bike not found")

    def get_bike_by_parameter(self, model: str, colour: str, is_electric: bool)-> dict:
        """
        This method is used to get the bike by model, colour and is_electric from the database.

        :param model: This is the model of the bike.
        :param colour: This is the colour of the bike.
        :param is_electric: This is the is_electric of the bike.

        :raises ValueError: If no bike found in the database.

        :return: It returns the bike.
        """
        request = """SELECT * FROM bike WHERE model = ? AND colour = ? AND is_electric = ?"""
        result = self.__db.search_request(request,(model,colour,is_electric))
        if result is not None:
            return result[0]
        else:
            raise ValueError("Bike not found")

    def add_bike(self, model: str, colour: str, is_electric: bool)-> None:
        """
        This method is used to create a bike into the database.

        :param model: This is the model of the bike.
        :param colour: This is the colour of the bike.
        :param is_electric: This is the is_electric of the bike.
        """
        request = """INSERT INTO bike(model,colour,is_electric) VALUES(?,?,?)"""
        self.__db.changes_request(request, (model, colour, is_electric))

    def delete_bike(self, bike_id: int)-> None:
        """
        This method is used to delete the bike by id from the database.

        :param bike_id: This is the id of the bike.
        """
        request = """DELETE FROM bike WHERE id = ?"""
        self.__db.changes_request(request,(bike_id,))