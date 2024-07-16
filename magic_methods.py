# Magic Methods: Special methods that allow us to define how objects of a class behave in response to built-in operations. 
# They are implicitly called by Python in response to certain operations.
# They can be over-ridden to customize the behaviour of an object.
# Also known as dunder methods.

class Vector:
    def __init__(self, x, y) -> None:
        # Constructor: Initializes the object.
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        # Official string representation of the object. Useful for debugging.
        return f'Vector({self.x}, {self.y})'

    def __str__(self) -> str:
        # User-friendly string representation of the object.
        return f'({self.x}, {self.y})'
    
    def __len__(self):
        # Behaviour for the len() of the object
        # return (self.x**2 + self.y**2)**0.5 # len() cannot return float type, it should always be of int type.
        return int((self.x**2 + self.y**2)**0.5)
    
    def __add__(self, other):
        # Behaviour for the '+' operator
        if isinstance(other, Vector):
            return (self.x + other.x, self.y + other.y)
        raise TypeError('Operand must be of type Vector')
    
    def __getitem__(self, index):
        # Behaviour for accessing elements with 'square brackets'. Syntax: obj[key]
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif isinstance(index, int):
            raise IndexError('Index out of range')
        else:
            raise TypeError('Index should be of type int')

v1 = Vector(2,3)
print('String representation of the object for end user', v1)
print('String representation of the object for developer:', v1.__repr__())
print(f'Length of the vector: {len(v1)}')
v2 = Vector(5,9)
print(f'Sum of vectors: {v1 + v2}')
print('getitem result', v1[1])
# print(v1[3])
print(v1['Shivu'])