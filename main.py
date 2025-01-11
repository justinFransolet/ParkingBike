from src.app import ParkingBikeApp
from src.controller import ParkingPanelController
from src.infrastructure import BikeRepository, CustomerRepository, ParkRepository, RepositoriesManager
from src.utils.database import DBConnect

if __name__ == "__main__":
    # Database
    connect = DBConnect("parking_20250105.db")
    # Repository
    bike = BikeRepository(connect)
    customer = CustomerRepository(connect)
    park = ParkRepository(connect)
    repositories = RepositoriesManager(bike, customer, park)
    # Controller
    controller = ParkingPanelController(repositories)
    # App
    app = ParkingBikeApp(controller, "dark", "dark-blue",800,600)
    app.mainloop()