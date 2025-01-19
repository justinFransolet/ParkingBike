from src.view import  HomeApp
from src.controller import HomeController
from customtkinter import CTk

if __name__ == "__main__":
    controller = HomeController("setting.json", "parking_20250105.db")
    app = CTk()
    HomeApp(app,controller, 520, 240)
    app.mainloop()