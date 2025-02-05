﻿import json
import logging
from .error import JSONWriterError

# Configure log
logging.basicConfig(
    filename="JSONWriter.log",  # Name of the log file
    level=logging.INFO,  # Level of the logs
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format of the logs
    datefmt="%Y-%m-%d %H:%M:%S"  # Format of the date
)

def write_file(path: str, data: dict) -> None:
    """
    Write data in a JSON file.

    :param path: Path to the JSON file.
    :param data: Data to write in the JSON file.

    :raise FileNotFoundError: If the file is not found.
    :raise JSONWriterError: If the file is not a valid JSON file.

    :return: True if the file has been written successfully, False otherwise.
    """
    if type(data)!=type({}):
        raise JSONWriterError("The data wasn't dictionary")
    try:
        with open(path, 'w', encoding='utf-8-sig') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            logging.info(f"Fichier JSON mis à jour : {path}")
    except FileNotFoundError:
        message = f"File not found at : {path}"
        logging.error(message)
        raise FileNotFoundError(message)
    except json.JSONDecodeError as e:
        message = f"Format JSON file not valide. Detail : {e}"
        logging.critical(message)
        raise JSONWriterError(message)
    except Exception as e:
        message = f"Other error : {e}"
        logging.error(message)
        raise JSONWriterError(message)