from src.infrastructure.database.DBConnect import DBConnect


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
        result = self.__db.search_request(request,[])
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
        result = self.__db.search_request(request, [customer_id])
        if result is not None:
            return result[0]
        else:
            raise ValueError("Customer not found")

    def get_customer_by_parameter(self, firstname: str, lastname: str)-> dict:
        """
        This method is used to get the customer by firstname and lastname from the database.

        :param firstname: This is the firstname of the customer.
        :param lastname: This is the lastname of the customer.

        :raises ValueError: If no customers found in the database.

        :return: It returns the customer.
        """
        request = """SELECT * FROM customer WHERE firstname = ? AND lastname = ?"""
        result = self.__db.search_request(request,[firstname,lastname])
        if result is not None:
            return result[0]
        else:
            raise ValueError("Customer not found")

    def add_customer(self, firstname: str, lastname: str)-> None:
        """
        This method is used to create a customer into the database.
        """
        request = """INSERT INTO customer(firstname,lastname) VALUES(?,?)"""
        self.__db.changes_request(request, [firstname, lastname])

    def delete_customer(self, customer_id: int):
        """
        This method is used to delete the customer by id from the database.

        :return: It returns the list of customers.
        """
        request = """DELETE FROM customer WHERE id = ?"""
        return self.__db.changes_request(request,[customer_id])