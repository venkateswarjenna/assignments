from abc import ABC, abstractmethod
from datetime import date, timedelta


class Person(ABC):
    """Abstraction: Base class Person cannot be instantiated directly."""
    def __init__(self, name, phone):
        self.name = name
        self._phone = phone   

    @abstractmethod
    def display_info(self):
        pass


class Customer(Person):
    _id_counter = 1000

    def __init__(self, name, phone, license_no):
        super().__init__(name, phone)
        Customer._id_counter += 1
        self.customer_id = Customer._id_counter
        self.__license_no = license_no  
   
    def get_license_no(self):
        return self.__license_no

    def display_info(self):
        return f"Customer[{self.customer_id}] {self.name}"


class Staff(Person):
    def __init__(self, name, phone, role):
        super().__init__(name, phone)
        self.role = role

    def display_info(self):
        return f"Staff {self.role}: {self.name}"


# --------- Vehicles ---------
class Vehicle(ABC):
    """Abstraction: Abstract Vehicle class."""
    def __init__(self, plate_no, make, model, rate_per_day, seats):
        self.plate_no = plate_no
        self.make = make
        self.model = model
        self._rate_per_day = rate_per_day   # Encapsulation
        self.seats = seats
        self.available = True

    @abstractmethod
    def rental_rate(self):
        """Polymorphism: implemented differently by subclasses"""
        pass

    def info(self):
        return f"{self.__class__.__name__} {self.make} {self.model} ({self.plate_no}) | ₹{self.rental_rate()}/day | seats={self.seats}"


class EconomyCar(Vehicle):
    def rental_rate(self):   
        return self._rate_per_day


class SUV(Vehicle):
    def rental_rate(self):   
        return self._rate_per_day * 1.20


class Truck(Vehicle):
    def __init__(self, plate_no, make, model, rate_per_day, seats, payload_ton=1.0):
        super().__init__(plate_no, make, model, rate_per_day, seats)
        self.payload_ton = payload_ton

    def rental_rate(self):   
        return self._rate_per_day * 1.40


# --------- Rental ---------
class Rental:
    def __init__(self, rental_id, customer, vehicle, start_date, days):
        self.rental_id = rental_id
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.days = days
        self.status = "ACTIVE"

    def due_date(self):
        return self.start_date + timedelta(days=self.days)


# --------- Agency ---------
class CarRentalAgency:
    def __init__(self, name):
        self.name = name
        self.customers = {}
        self.vehicles = {}
        self.rentals = {}
        self._rental_seq = 0

    def register_customer(self, name, phone, license_no):
        c = Customer(name, phone, license_no)
        self.customers[c.customer_id] = c
        return c

    def add_vehicle(self, v):
        self.vehicles[v.plate_no] = v

    def available_vehicles(self, min_seats=1):
        return [v for v in self.vehicles.values() if v.available and v.seats >= min_seats]

    def rent(self, customer_id, plate_no, days):
        c = self.customers.get(customer_id)
        v = self.vehicles.get(plate_no)
        if not c or not v or not v.available:
            return None
        self._rental_seq += 1
        v.available = False
        r = Rental(self._rental_seq, c, v, date.today(), days)
        self.rentals[r.rental_id] = r
        return r

    def calc_charge(self, vehicle, days):
        base = vehicle.rental_rate() * days
        tax = base * 0.12
        security = 1000 if isinstance(vehicle, Truck) else 500
        return round(base + tax + security, 2)

    def return_vehicle(self, rental_id):
        r = self.rentals.get(rental_id)
        if not r or r.status != "ACTIVE":
            return None
        r.status = "COMPLETED"
        r.vehicle.available = True
        return self.calc_charge(r.vehicle, r.days)


# --------- Seed Helper ---------
def seed(ag):
    ag.add_vehicle(EconomyCar("MH01AB1234", "Maruti", "Alto", 1200, seats=4))
    ag.add_vehicle(SUV("MH02CD5678", "Hyundai", "Creta", 2000, seats=5))
    ag.add_vehicle(Truck("MH03EF9012", "Tata", "407", 2500, seats=2, payload_ton=2.5))
    ag.add_vehicle(Truck("AP30CF9058", "Tata", "307", 2500, seats=3, payload_ton=2.5))


# --------- Main ---------
def main():
    agency = CarRentalAgency("ByteDrive Rentals")
    seed(agency)
    menu = (
        "\n--- Car Rental Menu ---\n"
        "1. Register Customer\n"
        "2. Show Available Vehicles\n"
        "3. Rent Vehicle\n"
        "4. Return Vehicle\n"
        "0. Exit\n"
    )

    while True:
        try:
            choice = input(menu + "Choose: ")
            if choice == "1":
                name = input("Name: ")
                phone = input("Phone: ")
                lic = input("License No: ")
                c = agency.register_customer(name, phone, lic)
                print("Registered:", c.display_info())

            elif choice == "2":
                seats = int(input("Min seats needed (default 1): ") or 1)
                items = agency.available_vehicles(seats)
                if not items:
                    print("No vehicles available for the given seat count.")
                for v in items:
                    print(v.info())

            elif choice == "3":
                cid = int(input("Customer ID: "))
                plate = input("Vehicle Plate No: ")
                days = int(input("Days: "))
                r = agency.rent(cid, plate, days)
                if r:
                    est = agency.calc_charge(r.vehicle, r.days)
                    print(f"Rented! RentalID={r.rental_id} | Due={r.due_date()} | Est. Bill ₹{est}")
                else:
                    print("Rent failed (check customer/vehicle/availability).")

            elif choice == "4":
                rid = int(input("Rental ID to return: "))
                bill = agency.return_vehicle(rid)
                if bill is not None:
                    print(f"Returned. Total Bill: ₹{bill}")
                else:
                    print("Return failed (invalid rental or already completed).")

            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
