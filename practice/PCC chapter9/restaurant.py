class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is {}".format(self.restaurant_name))
        print("Cusine types are {}".format(self.cuisine_type))

    def open_restaurant(self):
        print("Restaurant is on")

    def set_number_served(self,num):
        if self.number_served >= 0:
            self.number_served = num
        else:
            print("You can not serve negative people")

    def increment_number_served(self,num):
        self.number_served += num

    def read_number_served(self):
        print("There are {} people".format(self.number_served))

def main():
    mcd = Restaurant("Mc Donald","Hamburger, fries")
    mcd.describe_restaurant()
    mcd.open_restaurant()

    mcd.read_number_served()
    mcd.set_number_served(100)
    mcd.read_number_served()
    mcd.increment_number_served(10)
    mcd.read_number_served()

if __name__ == '__main__':
    main()
