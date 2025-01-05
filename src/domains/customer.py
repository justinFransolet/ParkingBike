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

    def __str__(self):
        return f'Customer {self.__id}: {self.__firstname} {self.__lastname}'