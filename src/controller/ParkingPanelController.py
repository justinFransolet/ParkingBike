from src.domains import create_bike, create_customer, create_park, Customer, Bike, Park
from datetime import datetime
import logging
from src.infrastructure import RepositoriesManager

# Configure log
logging.basicConfig(
    filename="ParkingPanel.log",  # Name of the log file
    level=logging.INFO,  # Level of the logs
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format of the logs
    datefmt="%Y-%m-%d %H:%M:%S"  # Format of the date
)

class ParkingPanelController:
    """
    Controller for managing the parking panel operations.

    This class provides methods to add bikes and customers to their respective repositories,
    place bikes in the park, and return bikes to customers. It also handles logging of these operations.
    """

    def __init__(self, repositories: RepositoriesManager):
        """
        Initializes the ParkingPanelController with the given repositories' manager.

        This constructor sets up the repositories manager which will be used to interact with the database for managing bikes, customers, and parks.

        :param repositories: The manager for all repositories to interact with the database.
        """
        self.repositories = repositories

    def add_bike(self,model: str, colour: str, is_electric: bool) -> (int,Bike):
        """
        Adds a bike to the repository.

        This method creates a bike with the given model, colour, and electric status. It then checks if the bike already exists in the repository.
        If the bike exists, a warning is logged. If the bike does not exist, it is added to the repository and an info message is logged.

        :param model: The model of the bike. The model can't be more than 40 characters.
        :param colour: The colour of the bike. The colour can't be more than 30 characters.
        :param is_electric: Indicates if the bike is electric.

        :raises AttributeError: If any attribute doesn't meet the constraints.
        :raises MemoryError: If duplicate bikes found in the database.

        :return: The bike object.
        """
        bike = create_bike(model, colour, is_electric)
        repository = self.repositories.bike_repository
        try:
            db_bike = repository.get_bike(bike)
            logging.warning(f"A bike with this id({db_bike[0]}) already exist.")
        except ValueError:
            repository.add_bike(bike)
            db_bike =  repository.get_bike(bike)
            logging.info(f"A new bike create with this id({db_bike[0]}).")
        return db_bike[0],bike

    def add_customer(self,surname: str, firstname: str)-> (int,Customer):
        """
        Adds a customer to the repository.

        This method creates a customer with the given surname and firstname. It then checks if the customer already exists in the repository.
        If the customer exists, a warning is logged. If the customer does not exist, it is added to the repository and an info message is logged.

        :param surname: The surname of the customer. The surname can't be more than 50 characters.
        :param firstname: The firstname of the customer. The firstname can't be more than 50 characters.

        :raises AttributeError: If any attribute doesn't meet the constraints.
        :raises MemoryError: If duplicate customers found in the database.

        :return: The customer object.
            """
        customer = create_customer(surname, firstname)
        repository = self.repositories.customer_repository
        try:
            db_customer = repository.get_customer(customer)
            logging.warning(f"A customer with this id({db_customer[0]}) already exist.")
        except ValueError:
            repository.add_customer(customer)
            db_customer = repository.get_customer(customer)
            logging.info(f"A new bike create with this id({db_customer[0]}).")
        return db_customer[0],customer

    def place_bike(self,parking_number: int, model: str, colour: str, surname: str, firstname: str, is_electric: bool) -> Park:
        """
        Places a bike in the park.

        This method adds a bike and a customer to their respective repositories, then creates a park entry with the given parking number.
        It logs the creation of the park entry.

        :param parking_number: The parking number for the bike.
        :param model: The model of the bike. The model can't be more than 40 characters.
        :param colour: The colour of the bike. The colour can't be more than 30 characters.
        :param surname: The surname of the customer. The surname can't be more than 50 characters.
        :param firstname: The firstname of the customer. The firstname can't be more than 50 characters.
        :param is_electric: Indicates if the bike is electric.

        :raises AttributeError: If any attribute doesn't meet the constraints.
        :raises MemoryError: If duplicate entries are found in the database.

        :return: The park object.
        """
        bike = self.add_bike(model,colour,is_electric)
        customer = self.add_customer(surname,firstname)
        repository = self.repositories.park_repository
        park = create_park(bike[1], customer[1], datetime.now(), None, parking_number)
        repository.add_park(park,bike[0],customer[0])
        db_park = repository.get_park(park)
        logging.info(f"A new bike create with this id({db_park[0]}).")
        return park

    def return_bike(self,park: Park)-> bool:
        """
        This function is usable to return a bike to a customer.

        :param park: The park object to return to the customer.

        :return: True if the bike was return otherwise the wasn't return to a customer.
        """
        date = datetime.now()
        if park.start_time >= date:
            raise ValueError("The depot date must be earlier than the retake date.")

        repository = self.repositories.park_repository
        repository.update_retake_date(park,date)
        return True

    def get_all_bikes(self)-> list:
        """
        This function is usable to get all the bikes in the parking.

        :return: A list of all the bikes in the parking.
        """
        return self.repositories.bike_repository.get_bike_parking()