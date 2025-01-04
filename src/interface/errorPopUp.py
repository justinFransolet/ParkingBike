import customtkinter as ctk

class ErrorPopUp(ctk.CTkToplevel):
    """
    This class is the view of the error pop-up whose role is to display the error message.
    """
    def __init__(self, x: int, y: int, title: str, message: str)-> None:
        """
        Constructor of the error pop-up.

        :param x: The width of the pop-up.
        :param y: The height of the pop-up.
        :param title: The title of the pop-up. The best practice is to use the error name.
        :param message: The message of the error. The best practice is to use the error description for all user can understand.
        """
        super().__init__()
        self.title("Error")
        self.geometry(f"{x}x{y}")

        # Padding
        x_pad = round(2.5*(x/100)+5)
        y_pad = round(1.6*(y/100)+3.2)

        # Title
        label = ctk.CTkLabel(self, text=title, font=("Arial", 24))
        label.pack(padx=x_pad, pady=y_pad)

        # Description
        text = ctk.CTkTextbox(self, width=round(x/1.5), height=round(y/3))
        text.insert("1.0", message)
        text.configure(state="disabled")
        text.pack(padx=x_pad, pady=y_pad)

        # Close button
        button = ctk.CTkButton(self, text="Close", command=self.destroy)
        button.pack(padx=x_pad, pady=y_pad)