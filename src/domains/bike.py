class Bike:
    """
    The class bike use to represent a bike entity.
    """
    def __init__(self, id: int, model: str, colour: str, is_electric: bool):
        """
        This constructor initializes the bike entity.

        :param id: The id of the bike.
        :param model: The model of the bike.
        :param colour: The colour of the bike.
        :param is_electric: The is_electric of the bike.
        """
        self.__id = id
        self.__model = model
        self.__colour = colour
        self.__is_electric = is_electric

    def get_id(self)-> int:
        """
        This method returns the id of the bike.

        :return: The id of the bike.
        """
        return self.__id

    def get_model(self)-> str:
        """
        This method returns the model of the bike.

        :return: The model of the bike.
        """
        return self.__model

    def get_colour(self)-> str:
        """
        This method returns the colour of the bike.

        :return: The colour of the bike.
        """
        return self.__colour

    def get_is_electric(self)-> bool:
        """
        This method returns the is_electric of the bike.

        :return: The is_electric of the bike.
        """
        return self.__is_electric

    def __str__(self):
        return f'Bike {self.__id}: {self.__model} {self.__colour} {"electric" if self.__is_electric else "not electric"}'