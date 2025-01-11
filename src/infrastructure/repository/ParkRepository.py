from src.domains import Park
from src.utils.database.DBConnect import DBConnect


class ParkRepository:
    """
    This class is used to interact with the database to manage the park.
    """
    def __init__(self, db: DBConnect):
        """
        This is the constructor of the class.
        :param db: This is the object to interact with the database.
        """
        self.__db = db

    def get_all_park(self)-> list:
        """
        This method is used to get all the parks from the database.

        :raises ValueError: If no bike found in the database.

        :return: It returns the list of park.
        """
        request = """SELECT * FROM park"""
        result = self.__db.search_request(request,())
        if result is not None:
            return result
        else:
            raise ValueError("No park found")

    def get_park_by_id(self, park_id: int)-> dict:
        """
        This method is used to get a park by id from the database.

        :param park_id: This is the id of the parks.

        :raises ValueError: If no park found in the database.

        :return: It returns the park.
        """
        request = """SELECT * FROM park WHERE id = ?"""
        result = self.__db.search_request(request, (park_id,))
        if result is not None:
            if len(result) > 1:
                raise MemoryError("Duplicate park ticket found")
            return result[0]
        else:
            raise ValueError("Park ticket not found")

    def get_park(self, park: Park)-> dict:
        """
        This method is used to get the park by parking number, deposit_time, retake_time, bike_id and customer_id from the database.

        :param park: This is the park object.

        :raises ValueError: If no park found in the database.

        :return: It returns the park.
        """
        request = """SELECT * FROM park WHERE parking_number = ?"""
        result = self.__db.search_request(request,(park.ticket,))
        if result is not None:

            return result[0]
        else:
            raise ValueError("Park not found")

    def add_park(self, park: Park,bike_id: int, customer_id: int)-> None:
        """
        This method is used to create a park into the database.

        :param park: This is the park object.
        :param bike_id: This is the bike id.
        :param customer_id: This is the customer id.
        """
        request = """INSERT INTO park(parking_number,deposit_time,retake_time,bike_id,customer_id) VALUES(?,?,?,?,?)"""
        self.__db.changes_request(request, (park.ticket, park.start_time, park.end_time, bike_id, customer_id))

    def delete_bike(self, ticket: int)-> None:
        """
        This method is used to delete the park by the ticket from the database.

        :param ticket: This is the value of the ticket.
        """
        request = """DELETE FROM park WHERE id = ?"""
        self.__db.changes_request(request,(ticket,))