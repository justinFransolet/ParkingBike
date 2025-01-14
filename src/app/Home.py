import customtkinter as ctk
import PIL.Image

from src.app import Tooltip
from src.controller import HomeController


class HomeApp(ctk.CTk):
    """
    This class is the view of the parking whose role is to display the data and interact with it.
    """
    def __init__(self, controller: HomeController, appearance: str, color_theme: str, x: int, y: int) -> None:
        """
        Constructor of the view of the parking.

        :param controller: The controller of the app.
        :param appearance: The appearance of the app.
        :param color_theme: The color theme of the app.
        :param x: The width of the app.
        :param y: The height of the app.
        """
        # Initialize the parent class
        super().__init__()
        # Set controller
        self.controller = controller
        # Interface configuration
        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(color_theme)
        self.__x = x
        self.__y = y
        self.title("Home")
        self.geometry(f"{x}x{y}")
        self.resizable(True, True)
        # Padding
        self.__x_pad = round(2.5 * (x / 100) + 5)
        self.__y_pad = round(1.6 * (y / 100) + 3.2)

        # Header
        header_container = ctk.CTkFrame(self)
        header_container.grid(row=0, column=0, columnspan=3, pady=self.__y_pad, sticky="nsew")
        header_container.columnconfigure(0, weight=1)  # Center column for title
        header_container.columnconfigure(1, weight=0)  # Empty column for spacing
        header_container.columnconfigure(2, weight=1)  # Right column for switches

        # Title
        header = ctk.CTkLabel(header_container, text="VTT", font=("Arial", 24))
        header.grid(row=0, column=0, pady=self.__y_pad, sticky="ew")

        # Parameters (Switches)
        param_container = ctk.CTkFrame(header_container)
        param_container.grid(row=0, column=2, padx=self.__x_pad, sticky="e")

        # Theme Switch
        # Conteneur pour le switch et les labels
        switch_container = ctk.CTkFrame(param_container)
        switch_container.grid(row=0, column=0, columnspan=2, pady=self.__y_pad, sticky="ew")

        # Texte à gauche
        left_label = ctk.CTkLabel(switch_container, text="Light")
        left_label.grid(row=0, column=0, padx=5, sticky="w")

        # Switch
        self.theme = ctk.StringVar(value="Dark")
        theme_switch = ctk.CTkSwitch(switch_container, text="Dark", variable=self.theme, onvalue="Dark", offvalue="Light")
        theme_switch.grid(row=0, column=1, padx=5, sticky="ew")

        # Language Switch
        # Conteneur pour le switch et les labels
        lang_container = ctk.CTkFrame(param_container)
        lang_container.grid(row=1, column=0, columnspan=2, pady=self.__y_pad, sticky="ew")

        # Texte à gauche
        left_lang_label = ctk.CTkLabel(lang_container, text="FR")
        left_lang_label.grid(row=0, column=0, padx=5, sticky="w")

        # Switch
        self.lang = ctk.StringVar(value="EN")
        lang_switch = ctk.CTkSwitch(lang_container, text="EN", variable=self.lang, onvalue="EN", offvalue="FR")
        lang_switch.grid(row=0, column=1, padx=5, sticky="ew")

        # Buttons
        button_container = ctk.CTkFrame(self)
        button_container.grid(row=1, column=0, columnspan=3, pady=self.__y_pad, sticky="nsew")
        button_container.columnconfigure((0, 1, 2), weight=1)  # Equal spacing for buttons

        # Load image
        image_btn1  = PIL.Image.open("images/Visualizer.png")
        button1_image = ctk.CTkImage(light_image=image_btn1, dark_image=image_btn1,size=(48, 48))

        image_btn2 = PIL.Image.open("images/Parking.png")
        button2_image = ctk.CTkImage(light_image=image_btn2, dark_image=image_btn2, size=(48, 48))

        image_btn3 = PIL.Image.open("images/Analyzer.png")
        button3_image = ctk.CTkImage(light_image=image_btn3, dark_image=image_btn3, size=(48, 48))

        # Button Visualizer
        btn1 = ctk.CTkButton(button_container, text="", image=button1_image, compound="left")
        btn1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        # Add tooltip
        Tooltip(btn1, "Data Visualizer")

        # Button Parking panel
        btn2 = ctk.CTkButton(button_container, text="", image=button2_image, compound="left")
        btn2.grid(row=0, column=1, padx=self.__x_pad, sticky="ew")
        # Add tooltip
        Tooltip(btn2, "Parking panel")

        # Button Analyser
        btn3 = ctk.CTkButton(button_container, text="", image=button3_image, compound="left")
        btn3.grid(row=0, column=2, padx=self.__x_pad, sticky="ew")
        # Add tooltip
        Tooltip(btn3, "Data Analyser")

        # Footer
        footer = ctk.CTkLabel(self, text="Created by Fransolet Justin", font=("Arial", 13))
        footer.grid(row=2, column=0, columnspan=3, pady=self.__y_pad, sticky="nsew")

if __name__ == "__main__":
    controller = HomeController()
    app = HomeApp(controller, "dark", "dark-blue", 520, 240)
    app.mainloop()