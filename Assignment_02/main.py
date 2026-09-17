from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "EV123", 60)
motorbike = Motorbike("Honda", "Click", "MB456", 150)

# Create a renter
renter = Renter("Nyi Sett", 12345)

# Print vehicle before renting
print(car)

# Rent the vehicle
car.rent()
print(car)

# Return the vehicle
car.return_vehicle()
print(car)

print()

# Test invalid renter name
try:
    bad_renter = Renter("", 12345)
except ValueError as error:
    print("Caught error:", error)

# Test invalid licence number
try:
    bad_renter = Renter("John", -1)
except ValueError as error:
    print("Caught error:", error)

print()

# Polymorphism
vehicles = [car, electric_car, motorbike]

for vehicle in vehicles:
    print(vehicle)