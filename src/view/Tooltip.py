from tkinter import Event
import customtkinter as ctk

class Tooltip:
    """
    This class is used to create a tooltip for a widget.

    A tooltip is a small pop-up window that appears when a user places the mouse pointer over an element such as a button or label.
    """
    def __init__(self, widget, text):
        """
        Create a new tooltip for the given widget.

        :param widget: The widget to which the tooltip will be attached.
        :param text: The text to display in the tooltip.
        """
        self.widget = widget
        self.text = text
        self.tooltip = None

        # Bind events to the widget
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event: Event)-> None:
        """
        Display the tooltip.

        :param event: The event that triggered the display of the tooltip.
        """
        if self.tooltip is None:
            # Create the tooltip window
            self.tooltip = ctk.CTkToplevel()
            self.tooltip.wm_overrideredirect(True)  # Remove the window decorations
            self.tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")

            # Add a label to the tooltip
            label = ctk.CTkLabel(self.tooltip, text=self.text, fg_color="gray75", corner_radius=5, text_color="black")
            label.pack(padx=5, pady=5)

    def hide_tooltip(self, event: Event)-> None:
        """
        Hide the tooltip.

        :param event: The event that triggered the hiding of the tooltip.(It is not used in this method)
        """
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None