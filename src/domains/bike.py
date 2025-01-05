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

    def __str__(self):
        return f'Bike {self.__id}: {self.__model} {self.__colour} {"electric" if self.__is_electric else "not electric"}'