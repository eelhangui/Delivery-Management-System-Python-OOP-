class DeliveryVehicle:
    def __init__(self,driver_name,max_capacity):
        self.driver_name = driver_name
        self.max_capacity = max_capacity
    def show_info(self):
        print(f"Driver Name: {self.driver_name}, Max Capacity: {self.max_capacity} kg")

class Motorcycle(DeliveryVehicle):
    def __init__(self, driver_name, max_capacity, has_sidecar=False):
        super().__init__(driver_name,max_capacity)
        self.has_sidecar = has_sidecar
    def deliver_fast(self):
        print(f"{self.driver_name} is delivering a fast package on motorcycle with sidecar: {self.has_sidecar}")
class Truck(DeliveryVehicle):
    def __init__(self, driver_name, max_capacity, number_of_trailers=1):
        super().__init__(driver_name,max_capacity)
        self.number_of_trailers = number_of_trailers
    def unload_cargo(self):
        print(f"Unloading heavy cargo from {self.number_of_trailers} trailer(s) driven by {self.driver_name}")


# ==========================================
# TEST SUITE: Delivery System Implementation
# ==========================================

if __name__ == "__main__":
    print("--- 1. Testing Base DeliveryVehicle ---")
    base_vehicle = DeliveryVehicle(driver_name="Alex", max_capacity=500)
    base_vehicle.show_info()

    print("\n--- 2. Testing Motorcycle (Child Class) ---")
    moto = Motorcycle(driver_name="Mustapha", max_capacity=120, has_sidecar=True)
    moto.show_info()         # Inherited from DeliveryVehicle
    moto.deliver_fast()      # Unique Motorcycle method

    print("\n--- 3. Testing Truck (Child Class) ---")
    truck = Truck(driver_name="Jade", max_capacity=12000, number_of_trailers=2)
    truck.show_info()        # Inherited from DeliveryVehicle
    truck.unload_cargo()     # Unique Truck method


