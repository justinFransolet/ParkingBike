import customtkinter as ctk
from tkinter import ttk
from errorPopUp import ErrorPopUp


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


class ParkingBikeApp(ctk.CTk):
    """
    This class is the view of the parking whose role is to display the data and interact with it.
    """
    def __init__(self,appearance: str, color_theme:str,x: int, y: int)-> None:
        """
        Constructor of the view of the parking.

        :param appearance: The appearance of the interface.
        :param color_theme: The color theme of the interface.
        :param x: The width of the interface.
        :param y: The height of the interface.
        """
        super().__init__()
        # Interface configuration
        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(color_theme)
        self.__x = x
        self.__y = y
        self.title("Parking Bike")
        self.geometry(f"{x}x{y}")
        self.resizable(True, True)
        # Padding
        self.__x_pad = round(2.5 * (x / 100) + 5)
        self.__y_pad = round(1.6 * (y / 100) + 3.2)

        # Header
        header = ctk.CTkLabel(self, text="Parking Bike", font=("Arial", 24))
        header.grid(row=0, column=0, columnspan=2, pady=self.__y_pad, sticky="nsew")


        # Form container
        form_container = ctk.CTkFrame(self)
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
        self.park_button = ctk.CTkButton(self, text="Park", command=self.park_bike)
        self.park_button.grid(row=2, column=0, columnspan=2, pady=self.__y_pad)

        # Parking view
        table_frame = ctk.CTkFrame(self)
        table_frame.grid(row=3, column=0, columnspan=2, padx=self.__x_pad, pady=self.__y_pad, sticky="nsew")

        ctk.CTkLabel(table_frame, text="Parking", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=self.__y_pad)
        self.search_bar = ctk.CTkEntry(table_frame, placeholder_text="Search")
        self.search_bar.grid(row=1, column=0, columnspan=2, padx=10, pady=self.__y_pad)

        self.table = ttk.Treeview(table_frame, columns=("parking", "model", "colour", "electric", "surname", "firstname"), show="headings")
        self.table.grid(row=2, column=0, columnspan=2, pady=self.__y_pad, sticky="nsew")
        self.table.heading("parking", text="Parking number")
        self.table.heading("model", text="Model")
        self.table.heading("colour", text="Colour")
        self.table.heading("electric", text="Electric")
        self.table.heading("surname", text="Surname")
        self.table.heading("firstname", text="Firstname")

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, weight=1)
        table_frame.grid_rowconfigure(2, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

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
                # TODO : Park the bike in the parking and verify the data
            except ValueError as e:
                popup = ErrorPopUp(400,150,"Error", str(e))
                popup.wait_window()
                return
            self.table.insert("", "end", values=(parking_number, model, colour, is_electric, surname, firstname))
            self.clear_entries()
        else:
            popup = ErrorPopUp(400,150,"Error", "All required fields must be filled!")
            popup.wait_window()

    def clear_entries(self):
        """Effacer les champs d'entrée."""
        for entry in [self.parking_number_entry, self.model_entry, self.colour_entry, self.surname_entry, self.firstname_entry]:
            entry.delete(0, "end")

if __name__ == "__main__":
    app = ParkingBikeApp("dark", "dark-blue",800,600)
    app.mainloop()
