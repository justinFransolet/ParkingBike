from typing import Any, NamedTuple, Callable

import customtkinter as ctk

class Method(NamedTuple):
    """
    This class represents a method with a name of a button, a method and a colour of a button.

    :param name_button: The name of the method.
    :param method: The method to call.
    :param colour_button: The colour of the button.
    """
    name_button: str
    method: Callable[..., Any]
    colour_button: str

class DataTable(ctk.CTkFrame):
    """
    This class is at use to display some data like a table but with more options.

    You can add and delete the row in the table.
    You can add some actions, link to the row.
    """

    def __init__(self, master: Any, columns: [str] = list, methods=None, **kwargs):
        """
        Initialize the DataTable.

        :param master: The parent of the DataTable.
        :param columns: The columns of the DataTable.
        :param methods: The methods to apply at the action buttons.
        :param kwargs: The options of the DataTable.
        """
        super().__init__(master, **kwargs)

        # Save the method
        if methods is None:
            methods = []
        self.__methods = methods

        # Create the different columns
        self.__columns_name = columns
        self.__create_frames__()

    def __create_frames__(self) -> None:
        """
        Create the different columns of the DataTable.
        """
        self.__columns = []
        for column in self.__columns_name:
            column_frame = ctk.CTkFrame(self)
            column_frame.pack(side="left", fill="both", expand=True)
            ctk.CTkLabel(column_frame, text=column).pack(side="top", fill="both", expand=True)
            self.__columns.append(column_frame)
        action_frame = ctk.CTkFrame(self)
        action_frame.pack(side="left", fill="both", expand=True)
        ctk.CTkLabel(action_frame, text="Actions").pack(side="top", fill="both", expand=True)
        self.__columns.append(action_frame)

    def clear_rows(self) -> None:
        """
        Clear the DataTable.
        """
        for frame in self.__columns:
            frame.destroy()
        self.__create_frames__()

    def add_row(self, row: tuple, arguments: Any | None = None)-> None:
        """
        Add a row in the DataTable.

        :param row: The row to add in the DataTable.
        :param arguments: The arguments of the methods.
        """
        for index, column in enumerate(self.__columns[:-1]):
            ctk.CTkLabel(column, text=row[index]).pack(side="left", fill="both", expand=True)
        if self.__methods.__len__() == 0:
            ctk.CTkLabel(self.__columns[-1], text="No action").pack(side="left", fill="both", expand=True)
            return
        for method in self.__methods:
            if arguments is None:
                ctk.CTkButton(self.__columns[-1], text=method.name_button, command=method.method, fg_color=method.colour_button).pack(side="left", fill="both", expand=True)
            else:
                ctk.CTkButton(self.__columns[-1], text=method.name_button, command=lambda : method.method(arguments), fg_color=method.colour_button).pack(side="left", fill="both", expand=True)