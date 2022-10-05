
class Student:

    def __init__(self, name, age, address, phone_number, user_name="", password=""):
        self.__age = age
        self.__address = address
        self.__name = name
        self.__phone_number = phone_number
        self.__user_name = user_name
        self.__password = password



    def get_username(self):
        return self.__user_name

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address