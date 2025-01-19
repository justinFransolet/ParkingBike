import customtkinter as ctk
from tkinter import ttk
from .ErrorDisplayer import ErrorPopUp
from src.controller import ParkingPanelController


def validate_int(new_value: str)-> bool:
    """
    Validation pour autoriser uniquement les entiers.

    :param new_value: La valeur actuelle de l'entrée.

    :return: True si la valeur est valide (vide ou entier), False sinon.
    """
    if new_value == "" or (new_value.isdigit() or (new_value.startswith("-") and new_value[1:].isdigit())):
        return True
    return False

def is_boolean_choose(data: str)-> None:
    """
    Check if a string is a digit.

    :params data: The string to check.
    """
    if not data in ["True", "False"]:
        raise ValueError("The electric bike must be True or False!")
    return


class ParkingPanel:
    """
    This class is the view of the parking whose role is to display the data and interact with it.
    """
    def __init__(self, app: ctk.CTk, controller: ParkingPanelController, appearance: str, color_theme:str,x: int, y: int)-> None:
        """
        Constructor of the view of the parking.

        :param app: The application object.
        :param controller: The controller of the view.
        :param appearance: The appearance of the view.
        :param color_theme: The color theme of the view.
        :param x: The width of the view.
        :param y: The height of the view.
        """

        self.__app = app
        # Set controller
        self.controller = controller
        # Interface configuration
        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(color_theme)
        self.__x = x
        self.__y = y
        self.__app.title("Parking Bike")
        self.__app.geometry(f"{x}x{y}")
        self.__app.resizable(True, True)
        # Padding
        self.__x_pad = round(2.5 * (x / 100) + 5)
        self.__y_pad = round(1.6 * (y / 100) + 3.2)

        # Header
        header = ctk.CTkLabel(self.__app, text="Parking Bike", font=("Arial", 24))
        header.grid(row=0, column=0, columnspan=2, pady=self.__y_pad, sticky="nsew")


        # Form container
        form_container = ctk.CTkFrame(self.__app)
        form_container.grid(row=1, column=0, columnspan=2, padx=self.__x_pad, pady=self.__y_pad, sticky="nsew")

        # Form for owner information
        owner_frame = ctk.CTkFrame(form_container)
        owner_frame.grid(row=0, column=0, padx=self.__x_pad, pady=self.__y_pad, sticky="nsew")
        # Add the different entries
        ctk.CTkLabel(owner_frame, text="Enter the details of the person", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=self.__y_pad)
        self.surname_entry = self.create_entry(owner_frame, "Surname:", 1)
        self.firstname_entry = self.create_entry(owner_frame, "Firstname:", 2)

        # Form for bike information

        bike_frame = ctk.CTkFrame(form_container)
        bike_frame.grid(row=0, column=1, padx=self.__x_pad, pady=self.__y_pad, sticky="nsew")
        # Add the different entries
        ctk.CTkLabel(bike_frame, text="Enter the details of the bike", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=self.__y_pad)
        self.model_entry = self.create_entry(bike_frame, "Model:",1)
        self.colour_entry = self.create_entry(bike_frame, "Colour:",2)
        ctk.CTkLabel(bike_frame, text="Electric bike:").grid(row=3, column=0, sticky="w", padx=self.__x_pad, pady=self.__y_pad)
        self.is_electric_var = ctk.StringVar(value="True")
        is_electric = ctk.CTkSwitch(bike_frame, text="", variable=self.is_electric_var, onvalue="True", offvalue="False")
        is_electric.grid(row=3, column=1, sticky="ew", padx=self.__x_pad, pady=self.__y_pad)
        self.parking_number_entry = self.create_entry(bike_frame, "Parking number:",4)
        self.parking_number_entry.configure(validate="key", validatecommand=(self.parking_number_entry.register(validate_int), "%P"))

        # Add the park button
        self.park_button = ctk.CTkButton(self.__app, text="Park", command=self.park_bike)
        self.park_button.grid(row=2, column=0, columnspan=2, pady=self.__y_pad)

        # Parking view
        table_frame = ctk.CTkFrame(self.__app)
        table_frame.grid(row=3, column=0, columnspan=2, padx=self.__x_pad, pady=self.__y_pad, sticky="nsew")

        ctk.CTkLabel(table_frame, text="Parking", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=self.__y_pad)
        # Add the search bar
        self.search_bar = ctk.CTkEntry(table_frame, placeholder_text="Search")
        self.search_bar.grid(row=1, column=0, columnspan=2, padx=10, pady=self.__y_pad)

        self.table = ttk.Treeview(table_frame, columns=("parking", "model", "colour", "electric", "surname", "firstname", "button"), show="headings")
        self.table.grid(row=2, column=0, columnspan=2, pady=self.__y_pad, sticky="nsew")
        self.table.heading("parking", text="Parking number")
        self.table.heading("model", text="Model")
        self.table.heading("colour", text="Colour")
        self.table.heading("electric", text="Electric")
        self.table.heading("surname", text="Surname")
        self.table.heading("firstname", text="Firstname")
        self.table.heading("button", text="Return")

        # Ensure the table_frame and table expand to fill the available space
        self.__app.grid_rowconfigure(3, weight=1)
        self.__app.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(2, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Footer
        footer = ctk.CTkLabel(self.__app, text="Created by Fransolet Justin", font=("Arial", 11))
        footer.grid(row=4, column=0, columnspan=2, pady=self.__y_pad, sticky="nsew")

    def create_entry(self, parent: ctk.CTkFrame, label_text: str,row: int)-> ctk.CTkEntry:
        """
        Create an entry with a label.

        :param parent: The parent of the entry.
        :param label_text: The text of the label.
        :param row: The row of the entry.

        :return: The entry created.
        """
        ctk.CTkLabel(parent, text=label_text).grid(row=row, column=0, sticky="w", padx=self.__x_pad, pady=self.__y_pad)
        entry = ctk.CTkEntry(parent)
        entry.grid(row=row, column=1, sticky="ew", padx=self.__x_pad, pady=self.__y_pad)
        return entry

    def park_bike(self)-> None:
        """
        Park a bike in the parking.
        """
        parking_number = self.parking_number_entry.get()
        model = self.model_entry.get()
        colour = self.colour_entry.get()
        surname = self.surname_entry.get()
        firstname = self.firstname_entry.get()
        is_electric = self.is_electric_var.get()

        if parking_number and model and colour and surname and firstname and is_electric:
            try:
                is_boolean_choose(is_electric)
                self.controller.place_bike(int(parking_number), model, colour, surname, firstname, True if is_electric=="True" else False)
                self.table.insert("", "end", values=(parking_number, model, colour, is_electric, surname, firstname))
                self.clear_entries()
            except Exception as e:
                ErrorPopUp(400,150,"Error", str(e))
                return
        else:
            ErrorPopUp(400,150,"Error", "All required fields must be filled!")

    def clear_entries(self):
        """
        Clear all the entries.
        """
        for entry in [self.parking_number_entry, self.model_entry, self.colour_entry, self.surname_entry, self.firstname_entry]:
            entry.delete(0, "end")
        self.is_electric_var.set("True")