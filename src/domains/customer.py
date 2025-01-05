class Customer:
    """
    The class customer use to represent a customer entity.
    """
    def __init__(self, id: int, firstname: str, lastname: str):
        """
        This constructor initializes the customer entity.

        :param id: The id of the customer.
        :param firstname: The firstname of the customer.
        :param lastname: The lastname of the customer.
        """
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname

    def get_id(self) -> int:
        """
        This method returns the id of the customer.

        :return: The id of the customer.
        """
        return self.__id

    def get_firstname(self) -> str:
        """
        This method returns the firstname of the customer.

        :return: The firstname of the customer.
        """
        return self.__firstname

    def get_lastname(self) -> str:
        """
        This method returns the lastname of the customer.

        :return: The lastname of the customer.
        """
        return self.__lastname

    def __str__(self):
        return f'Customer {self.__id}: {self.__firstname} {self.__lastname}'