# define number of cars
cars = 100
# define the number of people (drivers or passengers) that can be in a car
space_in_a_car = 4.0
# define the number of drivers
drivers = 30
# define the number of passeners
passengers = 90
# define the number of cars that are not driven by the number of cars subtracted by the number of drivers
cars_not_driven = cars - drivers
# define the number of cars driven defined by the number of drivers
cars_driven = drivers
# define the total space available in driven cars
carpool_capacity = cars_driven * space_in_a_car
# define the average passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
