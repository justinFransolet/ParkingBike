import sqlite3
import logging
from datetime import datetime

# Configure log
logging.basicConfig(
    filename="databaseParking.log",  # Name of the log file
    level=logging.INFO,  # Level of the logs
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format of the logs
    datefmt="%Y-%m-%d %H:%M:%S"  # Format of the date
)

def create_database()-> str:
    """
    Create the database with the tables customer, bike and park.

    The customer table contains the current customers of the bike park.
    The bike table contains the bikes of the customers.
    The park table contains the park time.

    :return: The name of the database created. If an error occurs, the name of the database is "error".
    """

    connection = None

    try:
        # Create the database name
        current_date = datetime.now().strftime("%Y%m%d")
        db_name = f"parking_{current_date}.db"
        # Connection to the database if it exists, otherwise it is created
        connection = sqlite3.connect(db_name, autocommit=False)
        cursor = connection.cursor()
        logging.info(f"The database connection to {db_name} is successful.")

        # Create table customer
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lastname TEXT NOT NULL,
            firstname TEXT NOT NULL
        );
        """)

        # Create table bike
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bike (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT NOT NULL,
            colour TEXT NOT NULL,
            is_electric BOOLEAN NOT NULL
        );
        """)

        # Create table park
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS park (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            parking_number INTEGER NOT NULL,
            deposit_time TEXT NOT NULL,
            retake_time TEXT,
            bike_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            FOREIGN KEY (bike_id) REFERENCES bike (id),
            FOREIGN KEY (customer_id) REFERENCES customer (id)
        );
        """)

        # Save the changes
        connection.commit()
        logging.info(f"Database named {db_name} was created successfully.")

    except sqlite3.Error as e:
        logging.error(f"Error during the creation of the database: {e}")
        db_name = "error"
    finally:
        # Close the connection
        if connection:
            connection.close()
            logging.info("The database connection was closed")

    return db_name

if __name__ == "__main__":
    create_database()