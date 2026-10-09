# Class Hierarchy (by Nawpol Sanarnporn 6830252229)

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Number of Doors: {self.number_of_doors}"

# Example usage
v = Vehicle("Toyota", "Hilux", 2028)
c = Car("Mitsubishi", "X-Force", 2025, 4)

print(v.get_info())
print(c.get_info())