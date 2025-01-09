from typing import NamedTuple

class Bike(NamedTuple):
    """
    The class bike is a record. You can use it for represent a record of bike for a database.
    """
    model: str
    colour: str
    is_electric: bool

def create_bike(model: str, colour: str, is_electric: bool) -> Bike:
    """
    This function check all these attribute of the bike before creating.

    :param model: The model of the bike. The model can't make more of 40 characters
    :param colour: The colour of the bike. The colour can't make more of 30 characters
    :param is_electric: The is_electric of the bike.

    :raises AttributeError: If any attribute wasn't in right with the different constraints.

    :return: This function return a bike objet with your attribute.
    """

    # Model Check
    if isinstance(model, str) :
        if len(model) > 40:
            raise AttributeError("The model can't make more of 40 characters")
    else:
        raise AttributeError("Model of a bike wasn't a string object")
    # Colour Check
    if isinstance(colour, str) :
        if len(colour) > 30:
            raise AttributeError("The colour can't make more of 30 characters")
    else:
        raise AttributeError("Colour of a bike wasn't a string object")
    # is_electric Check
    if not isinstance(is_electric,bool):
        raise AttributeError("The attribute for electrical bike wasn't a boolean object")

    return Bike(model,colour, is_electric)