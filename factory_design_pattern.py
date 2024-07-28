'''
Factory design pattern: 
-   It is a creational pattern.
-   It provides an interface for creating objects in a superclass 
    but allows subclasses to alter the types of objects that will be created.
-   Primary objective - decoupling the creation of objects from their implementation

Significance:
-   Code maintenance made simpler; Object creation logic is centralized.
-   Easy scalability; New object types can be introduced without changing the existing code base.
'''

from abc import ABC, abstractmethod

# Motorcycle Interface
class MotorcycleAbstract(ABC):
    # The following decorator enforces the subclasses derived from MotorcycleAbstract
    # to have the method create() defined in them. If not an error will be raised at 
    # the time of creating an object for such subclasses.
    @abstractmethod
    def create(self):
        ''' Interface method for creating motorcycle '''
        # Body of the function will be decided run time.
        # No need to use even a pass statement if doc strings are added for an abstractmethod

# Subclass of type Hunter
class Hunter(MotorcycleAbstract):
    @staticmethod
    def create():
        cylinder_volume = 350
        print(f'RE Hunter motorcycle created with displacement {cylinder_volume}')

# Subclass of type Guerrilla
class Guerrilla(MotorcycleAbstract):
    @staticmethod
    def create():
        cylinder_volume = 450
        print(f'RE Guerrilla motorcycle created with displacement {cylinder_volume}')

# Factory class
class RE_Factory:
    @staticmethod
    def produce_motorcycle(model: str):
        if model == 'hunter':
            return Hunter()
        elif model == 'guerrilla':
            return Guerrilla()
        else:
            # raise TypeError(f'Model: {model} not found in Royal Enfield factory')
            print(f'Model: {model} not found in Royal Enfield factory')
            return None

if __name__ == '__main__':
    chennai_re_plant = RE_Factory()

    h1 = chennai_re_plant.produce_motorcycle('hunter')
    h1.create() # Output: RE Hunter motorcycle created with displacement 350

    g1 = chennai_re_plant.produce_motorcycle('guerrilla')
    g1.create() # Output: RE Guerrilla motorcycle created with displacement 450

    a1 = chennai_re_plant.produce_motorcycle('ktm adventure 390')
    # Output: Model: ktm adventure 390 not found in Royal Enfield factory
    # a1 receives a None value

    # An attempt to write a subclass without an abstract method defined raises the following error
    class Shotgun(MotorcycleAbstract):
        def __init__(self) -> None:
            super().__init__()
    s1 = Shotgun() # TypeError: Can't instantiate abstract class Shotgun without an 
    # implementation for abstract method 'create'