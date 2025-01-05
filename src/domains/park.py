from datetime import datetime

from src import Bike, Customer


class Park:
    """
    The class park use to represent a park entity.
    """
    def __init__(self, id: int, bike: Bike, customer: Customer, start_time: datetime, end_time: datetime, ticket: int):
        """
        This constructor initializes the park entity.

        :param id: The id of the park.
        :param bike: The bike in the park.
        :param customer: The customer in the park.
        :param start_time: The start time of the park.
        :param end_time: The end time of the park.
        :param ticket: The ticket of the park.
        """
        self.__id = id
        self.__bike = bike
        self.__customer = customer
        self.__start_time = start_time
        self.__end_time = end_time
        self.__ticket = ticket

    def __str__(self):
        return f'Park {self.__id}: {self.__bike}: {self.__customer}: {self.__start_time}: {self.__end_time}: Ticket: {self.__ticket}'