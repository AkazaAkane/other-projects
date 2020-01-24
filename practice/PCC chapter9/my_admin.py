from User import user
from admin import Admin,Privileges

def main():
    YC = Admin("Yuhao","Chen")
    YC.privileges.show_privileges()

if __name__ == "__main__":
    main()
