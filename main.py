from src.app import  HomeApp
from src.controller import HomeController

if __name__ == "__main__":
    controller = HomeController("setting.json", "parking_20250105.db")
    app = HomeApp(controller, 520, 240)
    app.mainloop()