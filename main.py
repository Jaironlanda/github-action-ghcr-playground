# Write OOP python code to create a class called "Car"
# The class should have the following attributes:
# - make
# - model
# - year
# - odometer_reading
# The class should have the following methods:
# - get_descriptive_name() - returns a formatted descriptive name
# - read_odometer() - prints the car's mileage
# - update_odometer() - updates the odometer_reading attribute
# - increment_odometer() - increments the odometer_reading attribute
# Create an instance of the class and call each method

class Car:
    def __init__(self, make, model, year, odometer_reading):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

