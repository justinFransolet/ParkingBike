import json
import logging
from .error import JSONReaderError

# Configure log
logging.basicConfig(
    filename="JSONReader.log",  # Name of the log file
    level=logging.INFO,  # Level of the logs
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format of the logs
    datefmt="%Y-%m-%d %H:%M:%S"  # Format of the date
)

def read_file(path: str) -> dict:
    """
    Get the content of a JSON file.

    :param path: Path to the JSON file.

    :raise FileNotFoundError: If the file is not found.
    :raise JSONReaderError: If the file is not a valid JSON file.

    :return: The content of the JSON file on a dictionary.
    """
    try:
        with open(path, 'r', encoding='utf-8-sig') as file:
            donnees = json.load(file)
            return donnees
    except FileNotFoundError:
        message = f"File not found at : {path}"
        logging.error(message)
        raise FileNotFoundError(message)
    except json.JSONDecodeError as e:
        message = f"Format JSON file not valide. Detail : {e}"
        logging.critical(message)
        raise JSONReaderError(message)
    except Exception as e:
        message = f"Other error : {e}"
        logging.critical(message)
        raise JSONReaderError(message)