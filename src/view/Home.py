import os
import PIL.Image
from src.view import ErrorPopUp
from src.view.Tooltip import *
from src.controller import HomeController


class HomeApp:
    """
    This class is the view of the parking whose role is to display the data and interact with it.
    """
    def __init__(self, app: ctk.CTk,controller: HomeController, x: int, y: int) -> None:
        """
        Constructor of the view of the parking.

        :param controller: The controller of the view.
        :param x: The width of the view.
        :param y: The height of the view.
        """
        self.__app = app
        self.__list_widgets = []
        # Set controller
        self.__controller = controller
        # Interface configuration
        try:
            ctk.set_appearance_mode(self.__controller.get_selected_appearance())
            ctk.set_default_color_theme(self.__controller.get_color_theme())
        except Exception as e:
            ErrorPopUp(400,150,"Error", str(e))
        self.__x = x
        self.__y = y
        self.__app.title("Home")
        self.__app.geometry(f"{x}x{y}")
        self.__app.resizable(True, True)
        # Padding
        self.__x_pad = round(2.5 * (x / 100) + 5)
        self.__y_pad = round(1.6 * (y / 100) + 3.2)

        # Header
        header_container = ctk.CTkFrame(self.__app)
        header_container.grid(row=0, column=0, columnspan=3, pady=self.__y_pad, sticky="nsew")
        header_container.columnconfigure(0, weight=1)  # Center column for title
        header_container.columnconfigure(1, weight=0)  # Empty column for spacing
        header_container.columnconfigure(2, weight=1)  # Right column for switches
        self.__list_widgets.append(header_container)

        # Title
        header = ctk.CTkLabel(header_container, text="Mountain Bike Parking", font=("Arial", 24))
        header.grid(row=0, column=0, pady=self.__y_pad, sticky="ew")

        # Parameters (Switches)
        param_container = ctk.CTkFrame(header_container)
        param_container.grid(row=0, column=2, padx=self.__x_pad, sticky="e")
        self.__list_widgets.append(param_container)

        # Theme Switch
        # Conteneur pour le switch et les labels
        switch_container = ctk.CTkFrame(param_container)
        switch_container.grid(row=0, column=0, columnspan=2, pady=self.__y_pad, sticky="ew")

        # Texte à gauche
        left_label = ctk.CTkLabel(switch_container, text="Light")
        left_label.grid(row=0, column=0, padx=5, sticky="w")

        # Switch
        self.__theme = ctk.StringVar(value=self.__controller.get_selected_appearance())
        theme_switch = ctk.CTkSwitch(switch_container, text="Dark", variable=self.__theme, onvalue="dark", offvalue="light")
        theme_switch.grid(row=0, column=1, padx=5, sticky="ew")


        # Language Switch
        try:
            # Conteneur pour le switch et les labels
            lang_container = ctk.CTkFrame(param_container)
            lang_container.grid(row=1, column=0, columnspan=2, pady=self.__y_pad, sticky="ew")

            # Texte à gauche
            left_lang_label = ctk.CTkLabel(lang_container, text="FR")
            left_lang_label.grid(row=0, column=0, padx=5, sticky="w")

            # Switch
            self.__lang = ctk.StringVar(value=self.__controller.get_selected_lang())
            lang_switch = ctk.CTkSwitch(lang_container, text="EN", variable=self.__lang, onvalue="en", offvalue="fr")
            lang_switch.grid(row=0, column=1, padx=5, sticky="ew")
        except Exception as e:
            ErrorPopUp(400,150,"Error", str(e))

        # Buttons
        button_container = ctk.CTkFrame(self.__app)
        button_container.grid(row=1, column=0, columnspan=3, pady=self.__y_pad, sticky="nsew")
        button_container.columnconfigure((0, 1, 2), weight=1)
        self.__list_widgets.append(button_container)

        # Find path of images
        base_path = os.path.dirname(os.path.abspath(__file__))
        images_path = os.path.join(base_path, "images")

        # Load image
        try:
            image_btn1 = PIL.Image.open(os.path.join(images_path, "Visualizer.png"))
            button1_image = ctk.CTkImage(light_image=image_btn1, dark_image=image_btn1,size=(48, 48))

            image_btn2 = PIL.Image.open(os.path.join(images_path, "Parking.png"))
            button2_image = ctk.CTkImage(light_image=image_btn2, dark_image=image_btn2, size=(48, 48))

            image_btn3 = PIL.Image.open(os.path.join(images_path, "Analyzer.png"))
            button3_image = ctk.CTkImage(light_image=image_btn3, dark_image=image_btn3, size=(48, 48))

            # Button Visualizer
            btn1 = ctk.CTkButton(button_container, text="", image=button1_image, compound="left", command=self.open_visualizer)
            btn1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
            # Add tooltip
            Tooltip(btn1, "Data Visualizer")

            # Button Parking panel
            btn2 = ctk.CTkButton(button_container, text="", image=button2_image, compound="left", command=self.open_parking)
            btn2.grid(row=0, column=1, padx=self.__x_pad, sticky="ew")
            # Add tooltip
            Tooltip(btn2, "Parking panel")

            # Button Analyser
            btn3 = ctk.CTkButton(button_container, text="", image=button3_image, compound="left", command=self.open_analyzer)
            btn3.grid(row=0, column=2, padx=self.__x_pad, sticky="ew")
            # Add tooltip
            Tooltip(btn3, "Data Analyser")

        except Exception as e:
            ErrorPopUp(400,150,"Error", str(e))

        # Footer
        footer = ctk.CTkLabel(self.__app, text="Created by Fransolet Justin", font=("Arial", 13))
        footer.grid(row=2, column=0, columnspan=3, pady=self.__y_pad, sticky="nsew")
        self.__list_widgets.append(footer)

    def open_visualizer(self):
        """
        Open the visualizer view.
        """
        try:
            self.destroy()
            self.__controller.open_visualizer(self.__app)
        except Exception as e:
            ErrorPopUp(400,150,"Error", str(e))

    def open_parking(self):
        """
        Open the parking view.
        """
        try:
            self.destroy()
            self.__controller.open_parking(self.__app)
        except Exception as e:
            ErrorPopUp(400,150,"Error", str(e))

    def open_analyzer(self):
        """
        Open the analyzer view.
        """
        try:
            self.destroy()
            self.__controller.open_analyzer(self.__app)
        except Exception as e:
            ErrorPopUp(400,150,"Error", str(e))

    def changes_theme(self):
        """
        Change the theme of the view.
        """
        try:
            self.__controller.changes_theme(self.__theme.get())
        except Exception as e:
            ErrorPopUp(400,150,"Error", str(e))
    def changes_lang(self):
        """
        Change the language of the view.
        """
        try:
            self.__controller.changes_lang(self.__lang.get())
        except Exception as e:
            ErrorPopUp(400,150,"Error", str(e))

    def destroy(self):
        """
        Override the destroy method to ensure all background tasks are stopped.
        """
        for widget in self.__list_widgets:
            widget.destroy()