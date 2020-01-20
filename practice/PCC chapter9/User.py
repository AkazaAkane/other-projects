class User():

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("The User is {}".format(self.first_name + self.last_name))

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print(str(self.login_attempts)+"login attempts exist.")

yuhaoc = User("Yuhao","Chen")
yuhaoc.describe_user()
yuhaoc.greet_user()

yuhaoc.read_login_attempts()
yuhaoc.increment_login_attempts()
yuhaoc.increment_login_attempts()
yuhaoc.read_login_attempts()
yuhaoc.reset_login_attempts()
yuhaoc.read_login_attempts()
