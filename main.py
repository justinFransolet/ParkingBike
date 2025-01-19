from src.view import  HomeApp
from src.controller import HomeController
from customtkinter import CTk
import logging

# Configure log
logging.basicConfig(
    filename="main.log",  # Name of the log file
    level=logging.INFO,  # Level of the logs
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format of the logs
    datefmt="%Y-%m-%d %H:%M:%S"  # Format of the date
)

if __name__ == "__main__":
    controller = HomeController("setting.json", "parking_20250105.db")
    app = CTk()
    HomeApp(app,controller, 520, 240)
    app.mainloop()