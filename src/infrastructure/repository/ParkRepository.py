from datetime import datetime

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
        request = """SELECT p.parking_number, b.model, b.colour, b.is_electric, c.firstname, c.lastname, p.id FROM park p LEFT JOIN bike b ON p.bike_id = b.id LEFT JOIN customer c ON p.customer_id = c.id"""
        result = self.__db.search_request(request,())
        if result is not None:
            return result
        else:
            raise ValueError("No park found")

    def get_already_parked(self)-> list:
        """
        This method is used to get all the parks not already return to customer.

        :raises ValueError: If no bike found in the database.

        :return: It returns the list of park.
        """
        request = """SELECT p.parking_number, b.model, b.colour, b.is_electric, c.firstname, c.lastname, p.id FROM park p LEFT JOIN bike b ON p.bike_id = b.id LEFT JOIN customer c ON p.customer_id = c.id WHERE p.retake_time IS NULL"""
        result = self.__db.search_request(request,())
        if result is not None:
            return result
        else:
            raise ValueError("No park found")

    def get_park_by_id(self, park_id: int)-> tuple:
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

    def get_park(self, park: Park)-> tuple:
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

    def update_retake_date(self, park: Park,retake_date: datetime)-> None:
        """
        This method is used to change the return date into the database.

        :param park: This is the park object.
        :param retake_date: This is the retake date.
        """
        request = """UPDATE park SET retake_time = ? WHERE parking_number = ? AND retake_time IS NULL AND id = ?"""
        self.__db.changes_request(request, (retake_date, park.ticket, park.id))