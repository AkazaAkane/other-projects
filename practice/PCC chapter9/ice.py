from restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__ (self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        return self.flavors
        
def main():
    hagendasi = IceCreamStand("Icecream Shop","Icecream","Strawberry")
    hagendasi.describe_restaurant()
    hagendasi.show_flavors()

if __name__ == '__main__':
    main()
