﻿from typing import NamedTuple

class Customer(NamedTuple):
    """
    The class customer is a record. You can use it for represent a record of customer for a database.
    """
    firstname: str
    lastname: str

def create_customer(firstname: str, lastname: str)-> Customer:
    """
    This function check all these attribute of the customer before creating.

    :param firstname: The firstname of the customer. Firstname can't make more of 50 characters
    :param lastname: The lastname of the customer. Lastname can't make more of 50 characters

    :raises AttributeError: If any attribute wasn't in right with the different constraints.

    :return: This function return a customer objet with your attribute.
    """

    # Firstname Check
    if type(firstname) != str.__class__ or len(firstname) > 50:
        raise AttributeError("Firstname can't make more of 50 characters" if len(
            firstname) > 50 else "Firstname of a customer wasn't a string object")
    # Lastname Check
    if type(lastname) != str.__class__ or len(lastname) > 50:
        raise AttributeError("Lastname can't make more of 50 characters" if len(
            lastname) > 50 else "Lastname of a customer wasn't a string object")

    return Customer(firstname,lastname)