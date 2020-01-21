from User import user

class Admin(user):

    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self):
        print(self.privileges)

def main():
    Aoligei = Admin("Jumo","Zhanjiang")
    Aoligei.show_privileges()

if __name__ == '__main__':
    main()
