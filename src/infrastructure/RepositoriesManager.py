from typing import NamedTuple

from src.infrastructure.repository import BikeRepository, CustomerRepository, ParkRepository


class RepositoriesManager(NamedTuple):
    """
    The class repositoriesManager is a record. You can use it for store the different repository.
    """
    bike_repository: BikeRepository
    customer_repository: CustomerRepository
    park_repository: ParkRepository