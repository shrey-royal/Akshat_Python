"""
> Duck Typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines.

> When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.

> Duck typing is usually explained as: "If it looks like a duck and quacks like a duck, it must be a duck."

For example:
"""

class FuelPoweredVehicles:
    def refuel(self):
        print("FuelPoweredVehicles Refueling...")

class ElectricPoweredVehicles:
    def recharge(self):
        print("ElectricPoweredVehicles Recharging...")

class HybridVehicle:
    def refuel(self):
        print("FuelPoweredVehicles Refueling...")

    def recharge(self):
        print("ElectricPoweredVehicles Recharging...")

for vehicle in FuelPoweredVehicles(), ElectricPoweredVehicles(), HybridVehicle():
    vehicle.refuel()