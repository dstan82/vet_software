
class Animal:

    def __init__(name, type, breed, age):
        self.name = name
        self.type = type
        self.breed = breed
        self.age = age

name = input('Animal name')
type = input('Animal type')
breed = input('Animal breed')
age = input('Animal age')

animal1 = Animal(name, type, breed, age)

print('Animal {name}, type {type}, breed {breed} and age of {age} was added'.format(name, type, breed, age))
