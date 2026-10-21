class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area} m2, {self.rooms} rooms, price: {self.price}, address: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, garden_area):
        super().__init__(area, rooms, price, address)
        self.garden_area = garden_area

    def __str__(self):
        return f"House: {self.area} m2, {self.rooms} rooms, price: {self.price}, address: {self.address}, garden area: {self.garden_area} m2"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.area} m2, {self.rooms} rooms, price: {self.price}, address: {self.address}, floor: {self.floor}"


house = House(140, 5, 850000, "Lesna 12, Warsaw", 500)
flat = Flat(58, 3, 620000, "Dluga 8, Krakow", 3)

print(house)
print(flat)