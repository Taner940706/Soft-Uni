from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def drive():
        pass
    @abstractmethod
    def refuel():
        pass
    
class Car(Vehicle):
    
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    
    def drive(self, distance):
        res = (self.fuel_consumption + 0.9) * distance
        if res <= self.fuel_quantity:
            self.fuel_quantity = self.fuel_quantity - res
        else:
            pass
    def refuel(self, fuel):
        self.fuel_quantity = self.fuel_quantity + fuel
        
class Truck(Vehicle):
    
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    
    def drive(self, distance):
        res = (self.fuel_consumption + 1.6) * distance
        if res <= self.fuel_quantity:
            self.fuel_quantity = self.fuel_quantity - res
        else:
            pass
    def refuel(self, fuel):
        self.fuel_quantity = self.fuel_quantity + fuel*0.95