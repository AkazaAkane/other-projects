from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'roadster', 2015)
print(my_tesla.battery.get_range())
my_tesla.battery.upgrade_battery()
print(my_tesla.battery.get_range())
