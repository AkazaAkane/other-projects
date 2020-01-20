class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is {}".format(self.restaurant_name))
        print("Cusine types are {}".format(self.cuisine_type))

    def open_restaurant(self):
        print("Restaurant is on")

mcd = Restaurant("Mc Donald","Hamburger, fries")
mcd.describe_restaurant()
mcd.open_restaurant()
