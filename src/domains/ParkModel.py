from datetime import datetime
from typing import NamedTuple, Any
from .BikeModel import Bike
from .CustomerModel import Customer

class Park(NamedTuple):
    """
    The class park is a record. You can use it for represent a record of park for a database.
    """
    bike: Bike
    customer: Customer
    start_time: datetime
    end_time: Any
    ticket: int

def create_park(bike: Bike, customer: Customer, start_time: datetime, end_time: Any, ticket: int)-> Park:
    """
    This function check all these attribute of the park before creating.

    :param bike: The bike in the park.
    :param customer: The customer in the park.
    :param start_time: The start time of the park.
    :param end_time: The end time of the park. Or None if not already set.
    :param ticket: The ticket of the park. The ticket can't be negative.

    :raises AttributeError: If any attribute wasn't in right with the different constraints.

    :return: This function return a park objet with your attribute.
    """

    # bike Check
    if type(bike) != Bike.__class__:
        raise AttributeError("Bike of a park wasn't a Bike object")
    # customer Check
    if type(customer) != Customer.__class__:
        raise AttributeError("Customer of a park wasn't a Customer object")
    # start time Check
    if type(start_time) != datetime.__class__:
        raise AttributeError("Start time of a park wasn't a datetime object")
    # end time Check
    if type(end_time) != datetime.__class__ and end_time is not None:
        raise AttributeError("End time of a park wasn't a datetime object")
    # ticket Check
    if type(ticket) != int.__class__ or ticket < 1:
        raise AttributeError("Ticket can't be negative" if ticket < 1 else "Ticket of a park wasn't a integer object")

    return Park(bike,customer,start_time,end_time,ticket)