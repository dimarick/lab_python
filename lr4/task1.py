class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        return (
            f"Transport(coordinates = {self.coordinates}; "
            f"speed = {self.speed}; "
            f"brand = {self.brand}; "
            f"year = {self.year}; "
            f"number = {self.number})"
        )

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        x, y = self.coordinates

        return pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width

class Passenger():
    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    def __str__(self):
        return (
            f"Passenger(passengers_capacity = {self.passengers_capacity}; "
            f"number_of_passengers = {self.number_of_passengers})"
        )

    def get_passengers_capacity(self):
        return self.passengers_capacity


    def set_passengers_capacity(self, passengers_capacity):
        self.passengers_capacity = passengers_capacity


    def get_number_of_passengers(self):
        return self.number_of_passengers


    def set_number_of_passengers(self, number_of_passengers):
        self.number_of_passengers = number_of_passengers

class Cargo():
    def __init__(self, carrying):
        self.carrying = carrying

    def __str__(self):
        return (
            f"Cargo(carrying = {self.carrying})"
        )

    def get_carrying(self):
        return self.carrying

    def set_carrying(self, carrying):
        self.carrying = carrying


class Plane(Transport):
    def __init__(self, height, coordinates, speed, brand, year, number):
        Transport.__init__(self, coordinates, speed, brand, year, number)
        self.height = height

    def __str__(self):
        return (
            f"Plane({super().__str__()}; "
            f"height = {self.height})"
        )

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height


class Auto(Transport):
    def __str__(self):
        return (
            f"Auto({super().__str__()})"
        )


class Ship(Transport):
    def __init__(self, port, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    def __str__(self):
        return (
            f"Ship({super().__str__()}; "
            f"port = {self.port})"
        )

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

class Car(Auto):
    def __str__(self):
        return (
            f"Car({super().__str__()})"
        )


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

    def __str__(self):
        return (
            f"Bus({Auto.__str__(self)}; "
            f"{Passenger.__str__(self)})"
        )


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)

    def __str__(self):
        return (
            f"CargoAuto({Auto.__str__(self)}; "
            f"{Cargo.__str__(self)})"
        )

class Boat(Ship):
    def __str__(self):
        return (
            f"Boat({super().__str__()})"
        )

class PassengerShip(Ship, Passenger):
    def __init__(self, port, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Ship.__init__(self, port, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

    def __str__(self):
        return (
            f"PassengerShip({Ship.__str__(self)}; "
            f"{Passenger.__str__(self)})"
        )

class CargoShip(Ship, Cargo):
    def __init__(self, port, coordinates, speed, brand, year, number, carrying):
        Ship.__init__(self, port, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)

    def __str__(self):
        return (
            f"CargoShip({Ship.__str__(self)}; "
            f"{Cargo.__str__(self)})"
        )

class Seaplane(Plane, Ship):
    def __init__(self, height, port, coordinates, speed, brand, year, number):
        Plane.__init__(self, height, coordinates, speed, brand, year, number)
        Ship.__init__(self, port, coordinates, speed, brand, year, number)

    def __str__(self):
        return (
            f"Seaplane({Plane.__str__(self)}; "
            f"{Ship.__str__(self)})"
        )

class Airplane(Plane):
    def __str__(self):
        return (
            f"Airplane({Plane.__str__(self)})"
        )

if __name__ == "__main__":
    print(Transport((1, 2), 3, "N/A", 2025, 1))
    print(Passenger(6, 5))
    print(Cargo(7))
    print(Plane(8,(9, 10), 11, 'Airbus', 2024, 2))
    print(Auto((12, 13), 3, "Volvo", 2023, 3))
    print(Ship("Bsu", (14, 15), 2, "Evergreen", 2022, 4))
    print(Car((16, 17), 3, "UAZ", 2021, 5))
    print(Bus((18, 19), 3, "PAZ", 2020, 6, 39, 37))
    print(CargoAuto((20, 21), 3, "Ural", 2019, 7, 11))
    print(Boat("Atas", (22, 23), 1, "N/A", 2018, 8))
    print(PassengerShip("Eicp", (24, 25), 3, "N/A", 2017, 9, 42, 42))
    print(CargoShip("Emvn", (26, 27), 2, "N/A", 2016, 10, 43))
    print(Seaplane(28, "Tenrehte", (29, 30), 3, "N/A", 2015, 11))
    print(Airplane(31, (32, 33), 34, "N/A", 2014, 12))
