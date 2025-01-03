import customtkinter as ctk
from tkinter import ttk

# Configuration de la bibliothèque CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ParkingBikeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Parking Bike")
        self.geometry("800x600")

        # En-tête
        self.header = ctk.CTkLabel(self, text="Parking Bike", font=("Arial", 24))
        self.header.pack(pady=10)

        # Formulaire
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=20, fill="x", padx=20)

        # Formulaire personne
        self.person_frame = ctk.CTkFrame(self.form_frame)
        self.person_frame.pack(side="left", padx=20)

        ctk.CTkLabel(self.person_frame, text="Enter the details of the person", font=("Arial", 16)).pack(pady=10)
        self.surname_entry = self.create_entry(self.person_frame, "Surname:")
        self.firstname_entry = self.create_entry(self.person_frame, "Firstname:")
        self.phone_entry = self.create_entry(self.person_frame, "Phone number:")

        # Formulaire vélo
        self.bike_frame = ctk.CTkFrame(self.form_frame)
        self.bike_frame.pack(side="right", padx=20)

        ctk.CTkLabel(self.bike_frame, text="Enter the details of the bike", font=("Arial", 16)).pack(pady=10)
        self.model_entry = self.create_entry(self.bike_frame, "Model:")
        self.colour_entry = self.create_entry(self.bike_frame, "Colour:")
        self.parking_number_entry = self.create_entry(self.bike_frame, "Parking number:")

        # Bouton "Park"
        self.park_button = ctk.CTkButton(self, text="Park", command=self.park_bike)
        self.park_button.pack(pady=10)

        # Table de stationnement
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(pady=20, fill="both", expand=True, padx=20)

        ctk.CTkLabel(self.table_frame, text="Parking", font=("Arial", 16)).pack(pady=10)
        self.search_bar = ctk.CTkEntry(self.table_frame, placeholder_text="Search")
        self.search_bar.pack(pady=10, fill="x", padx=20)

        self.table = ttk.Treeview(self.table_frame, columns=("parking", "model", "colour", "surname", "firstname", "phone"), show="headings")
        self.table.pack(fill="both", expand=True, padx=20, pady=10)
        self.table.heading("parking", text="Parking number")
        self.table.heading("model", text="Model")
        self.table.heading("colour", text="Colour")
        self.table.heading("surname", text="Surname")
        self.table.heading("firstname", text="Firstname")
        self.table.heading("phone", text="Phone number")

    def create_entry(self, parent, label_text):
        """Créer une entrée avec un label."""
        ctk.CTkLabel(parent, text=label_text).pack(pady=5, anchor="w")
        entry = ctk.CTkEntry(parent)
        entry.pack(pady=5, fill="x")
        return entry

    def park_bike(self):
        """Ajouter une ligne à la table."""
        parking_number = self.parking_number_entry.get()
        model = self.model_entry.get()
        colour = self.colour_entry.get()
        surname = self.surname_entry.get()
        firstname = self.firstname_entry.get()
        phone = self.phone_entry.get()

        if parking_number and model and colour and surname and firstname:
            self.table.insert("", "end", values=(parking_number, model, colour, surname, firstname, phone))
            self.clear_entries()
        else:
            ctk.CTkMessagebox.show_error(title="Error", message="All required fields must be filled!")

    def clear_entries(self):
        """Effacer les champs d'entrée."""
        for entry in [self.parking_number_entry, self.model_entry, self.colour_entry, self.surname_entry, self.firstname_entry, self.phone_entry]:
            entry.delete(0, "end")

if __name__ == "__main__":
    app = ParkingBikeApp()
    app.mainloop()
