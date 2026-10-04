# 🚚 Delivery Management System (Python OOP)

A Python project demonstrating core **Object-Oriented Programming (OOP)** concepts, specifically focusing on **Class Inheritance** and the use of **`super()`** to extend functionality.

---

## 🚀 Features

* **Base Delivery Vehicle (`DeliveryVehicle`)**: Defines general delivery attributes (`driver_name`, `max_capacity`) and common methods (`show_info()`).
* **Motorcycle (`Motorcycle`)**: Inherits from `DeliveryVehicle`, adding custom properties for sidecar availability (`has_sidecar`) and a high-speed package delivery method (`deliver_fast()`).
* **Truck (`Truck`)**: Inherits from `DeliveryVehicle`, managing heavy transport specifications (`number_of_trailers`) and a dedicated cargo unloading method (`unload_cargo()`).

---

## 🛠️ OOP Concepts Demonstrated

1. **Inheritance**: Subclasses (`Motorcycle` and `Truck`) inherit shared properties and behaviors from `DeliveryVehicle`.
2. **Super Class Initialization**: Leveraged `super().__init__()` to seamlessly execute parent constructor logic without duplicating code.
3. **Extensibility**: Custom attributes and methods were added to specialized classes to model real-world transport scenarios.

---

## 💻 How to Run

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/eelhangui/delivery-system-oop.git](https://github.com/eelhangui/delivery-system-oop.git)