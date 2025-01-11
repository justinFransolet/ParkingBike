from src.domains import Customer
from src.utils.database.DBConnect import DBConnect


class CustomerRepository:
    """
    CustomerRepository class is a repository to interact with the customer data into the database.
    """
    def __init__(self, db: DBConnect):
        """
        Constructor to initialize the CustomerRepository class.
        :param db: This is the object to interact with the database.
        """
        self.__db = db

    def get_all_customers(self)-> list:
        """
        This method is used to get all the customers from the database.

        :raises ValueError: If no customers found in the database.

        :return: It returns the list of customers.
        """
        request = """SELECT * FROM customer"""
        result = self.__db.search_request(request,())
        if result is not None:
            return result
        else:
            raise ValueError("No customers found")

    def get_customer_by_id(self, customer_id: int)-> dict:
        """
        This method is used to get a customer by id from the database.

        :param customer_id: This is the id of the customer.

        :raises ValueError: If no customers found in the database.

        :return: It returns the customer.
        """
        request = """SELECT * FROM customer WHERE id = ?"""
        result = self.__db.search_request(request, (customer_id,))
        if result is not None:
            return result[0]
        else:
            raise ValueError("Customer not found")

    def get_customer(self, customer: Customer)-> dict:
        """
        This method is used to get the customer by firstname and lastname from the database.

        :param customer: This is the customer object.

        :raises ValueError: If no customers found in the database.

        :return: It returns the customer.
        """
        request = """SELECT * FROM customer WHERE firstname = ? AND lastname = ?"""
        result = self.__db.search_request(request,(customer.firstname,customer.lastname))
        if result is not None:
            if len(result) > 1:
                raise MemoryError("Duplicate customers found")
            return result[0]
        else:
            raise ValueError("Customer not found")

    def add_customer(self, customer: Customer)-> None:
        """
        This method is used to create a customer into the database.

        :param customer: This is the customer object.
        """
        request = """INSERT INTO customer(firstname,lastname) VALUES(?,?)"""
        self.__db.changes_request(request, (customer.firstname, customer.lastname))

    def delete_customer(self, customer_id: int)-> None:
        """
        This method is used to delete the customer by id from the database.

        :param customer_id: This is the id of the customer.
        """
        request = """DELETE FROM customer WHERE id = ?"""
        self.__db.changes_request(request,(customer_id,))