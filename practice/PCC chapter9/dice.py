from random import randint

class Die():

    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        x = randint(1,6)
        return x

def main():
    d1 = Die()
    d2 = Die(10)
    d3 = Die(20)

    for i in range(10):
        print("The result of sides 6 die is {}".format(d1.roll_die()))
        print("The result of sides 10 die is {}".format(d2.roll_die()))
        print("The result of sides 20 die is {}".format(d3.roll_die()))


if __name__ == "__main__":
    main()
