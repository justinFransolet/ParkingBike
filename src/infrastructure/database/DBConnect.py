import sqlite3
import logging

# Configure log
logging.basicConfig(
    filename="databaseParking.log",  # Name of the log file
    level=logging.INFO,  # Level of the logs
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format of the logs
    datefmt="%Y-%m-%d %H:%M:%S"  # Format of the date
)

class DBConnect:
    """
    Class to join the database with a single connection point.
    """
    def __init__(self,name: str):
        """
        Constructor of the class.

        :param name: Name of the database.
        """
        self.name = name

    def request_executor(self,request: str)-> bool:
        """
        Method to execute a request in the database.

        :param request: Request to execute in the database.

        :return: True if the request was executed successfully, False otherwise.
        """

        connection = None
        success = False

        try:
            # Connect to the database
            connection = sqlite3.connect(self.name)
            cursor = connection.cursor()
            # Execute the request
            cursor.execute(request)
            connection.commit()
            # Change the success flag
            success = True
        except sqlite3.Error as error:
            logging.error(f"Error disconnecting from the database: {error}")
        finally:
            # Close the connection
            if connection:
                connection.close()
                logging.info("The connection to the database was closed successfully.")
        return success