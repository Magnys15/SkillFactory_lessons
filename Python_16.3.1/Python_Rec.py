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