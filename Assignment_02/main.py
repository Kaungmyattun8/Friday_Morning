from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "2EV567", 75)
motorbike = Motorbike("Honda", "CBR500R", "3MB890", 500)


# Create a renter
renter = Renter("John", 12345)

print("Renter:")
print("Name:", renter.name)
print("License:", renter.license_no)
print("Rented vehicles:", renter.rented)

print()


# Print vehicles before renting
print("Vehicles before renting:")
print(car)
print(electric_car)
print(motorbike)

print()


# Rent a vehicle
car.rent()
renter.rented.append(car)

print("After renting the car:")
print(car)

print()


# Return the vehicle
car.return_vehicle()
renter.rented.remove(car)

print("After returning the car:")
print(car)

print()


# Test invalid renter name
try:
    bad_renter = Renter("", 12345)
except ValueError as e:
    print("Caught ValueError:", e)


# Test invalid license number
try:
    bad_renter = Renter("Alice", -10)
except ValueError as e:
    print("Caught ValueError:", e)

print()


# Test changing values after creation
try:
    renter.name = ""
except ValueError as e:
    print("Caught ValueError when changing name:", e)

try:
    renter.license_no = 0
except ValueError as e:
    print("Caught ValueError when changing license:", e)

print()


# Polymorphism
print("Mixed vehicle list:")

vehicles = [
    Vehicle("Toyota", "Yaris", "1AB234"),
    ElectricCar("Tesla", "Model 3", "2EV567", 75),
    Motorbike("Honda", "CBR500R", "3MB890", 500)
]

for vehicle in vehicles:
    print(vehicle)