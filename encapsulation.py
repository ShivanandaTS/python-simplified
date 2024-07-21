'''
Encapsulation: bundling attributes and methods to a single unit, typically a class, 
resticting access to some of the object's components. It is useful in hiding internal
state of the object and exposing only the necessary attributes and methods.
'''

class Person:
    def __init__(self, name, age):
        # Protected attribute starts with single underscore
        self._name = name
        # Private attribute starts with double underscore
        self.__age = age
    
    @property
    def age(self):
        '''Getter for the age property'''
        return self.__age
    
    @age.setter
    def age(self, value):
        '''Setter for the age property'''
        # It allows us to add control mechanism before
        # setting a value for the private attribute
        if not isinstance(value, (int, float)):
            print('Age should be of type int or float')
        elif value < 0:
            print('Age cannot be a neagative number')
        else:
            self.__age = value


p1 = Person('Naruto', 17)
print(p1._name) # Output: Naruto
# Private attributes donot have direct access
# print(p1.__age) # Output: AttributeError
print(f'{p1._name} was {p1.age} young at the end of 4th great ninja war.')

p1.age = 33
print(f'{p1._name} in new Boruto series is {p1.age} young.')