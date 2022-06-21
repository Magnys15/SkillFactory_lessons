# Python_16.7 - 16.9.3
class Rectangle:
    def __init__(self, width, height):
        self.widht = width
        self.height = height

    def getWidht(self):
        return self.widht

    def getHeigt(self):
        return self.height

    def getArea(self):
        return self.widht * self.height

    def parameters(self):
        return self.widht, self.height


class Square:
    def __init__(self, x):
        self.x = x

    def getArea(self):
        return self.x ** 2


class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Circle:
    def __init__(self, rad):
        self.rad = rad

    def getArea(self):
        return self.rad ** 2 * 3.14


# Python_16.9.3

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    def __str__(self):
        return f"Имя покупателя: {self.name}. "\
               f"Баланс: {self.balance}. "

    @classmethod
    def add_new_customer(cls):
        nc = Customer(input("Введите имя клиента: "),
                      int(input("Введите баланс клиента: ")))
        return nc


class CustomerNew(Customer):
    def __init__(self, name, balance, city, status):
        super().__init__(name, balance)
        self.city = city
        self.status = status




    def __str__(self):
        return f"Имя покупателя: {self.name}. " \
               f"Баланс: {self.balance}. " \
               f"Город: {self.city}. " \
               f"Статус: {self.status}. "

    @classmethod
    def add_new_customer(cls):
        nc = CustomerNew(input("Введите имя клиента: "),
                        input("Введите баланс клиента: "),
                        input("Введите город клиента: "),
                        input("Введите статус клиента: "))
        return nc


class CustomerList:
    customer_list = []

    def show_customers(self):
        for i in range(len(self.customer_list)):
            print(self.customer_list[i])


# Python_16.10.5

class SquareException(Exception):
    pass


class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        if a < 0:
            raise NonPositiveDigitException('Неправильно указанна сторона квадрата')
