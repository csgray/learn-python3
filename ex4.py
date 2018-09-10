# Sets the variable "cars" to 100
cars = 100
# Sets the variable "space_in_a_car" to 4.0, which is a floating-point number
space_in_a_car = 4.0
# Sets the variable "drivers" to 30
drivers = 30
# Sets the variable "passengers" to 90
passengers = 90
# Subtracts drivers (30) from cars (100) and sets the variable "cars_not_driven" to the result (70)
cars_not_driven = cars - drivers
# Sets the variable "cars_driven" to the same value as "drivers" (30)
cars_driven = drivers
# Multiples the value of "cars_driven" by the value of "space_in_a_car" (4.0) and sets "carpool_capacity" to the result (120.0)
carpool_capacity = cars_driven * space_in_a_car
# Divides the value of "passengers" (90) by the value of "cars_driven" (30) and sets "average_passengers_per_car" to the result (3.0)
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")