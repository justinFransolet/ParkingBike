from datetime import datetime
from typing import NamedTuple, Any
from .BikeModel import Bike
from .CustomerModel import Customer

class Park(NamedTuple):
    """
    The class park is a record. You can use it for represent a record of park for a database.
    """
    id: int
    bike: Bike
    customer: Customer
    start_time: datetime
    end_time: Any
    ticket: int

def create_park(id_park: int, bike: Bike, customer: Customer, start_time: datetime, end_time: Any, ticket: int)-> Park:
    """
    This function check all these attribute of the park before creating.

    :param id_park: The id of the park. The id can't be negative.
    :param bike: The bike in the park.
    :param customer: The customer in the park.
    :param start_time: The start time of the park.
    :param end_time: The end time of the park. Or None if not already set.
    :param ticket: The ticket of the park. The ticket can't be negative.

    :raises AttributeError: If any attribute wasn't in right with the different constraints.

    :return: This function return a park objet with your attribute.
    """

    # id Check
    if isinstance(id_park, int):
        if id_park < 0:
            raise AttributeError("Id of a park can't be negative")
    else:
        raise AttributeError("Id of a park wasn't a int object")
    # bike Check
    if not isinstance(bike,Bike):
        raise AttributeError("Bike of a park wasn't a Bike object")
    # customer Check
    if not isinstance(customer,Customer):
        raise AttributeError("Customer of a park wasn't a Customer object")
    # start time Check
    if not isinstance(start_time,datetime):
        raise AttributeError("Start time of a park wasn't a datetime object")
    # end time Check
    if not isinstance(end_time,datetime) and end_time is not None:
        raise AttributeError("End time of a park wasn't a datetime object")
    # ticket Check
    if isinstance(ticket, int):
        if ticket < 1:
            raise AttributeError("Ticket can't be negative")
    else:
        raise AttributeError("Ticket of a park wasn't a int object")

    return Park(id_park,bike,customer,start_time,end_time,ticket)