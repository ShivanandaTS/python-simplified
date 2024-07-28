'''
Proxy design pattern:
-   it is a structural design pattern
-   in this pattern a substitute object is created for original object
-   very similar to decorator 

Significance:
-   Control access; useful in implementing lazy initialization
'''

import time

class HeavyResource(): # creating an object for HeavyResource is very costly in terms of time and space
    def __init__(self) -> None: # constructor that loads huge data
        self._data = self._load_super_huge_data()
    
    def _load_super_huge_data(self): # costly function in terms of time and space
        print('Loading huge data...')
        time.sleep(3)
        return [x**2 for x in range(1, 100)]
    
    def getdata(self):
        return self._data

class HeavyResourceProxy(HeavyResource): # proxy class for heavy resource
    def __init__(self) -> None:
        self._real_resource = None
    
    def operation(self, l_limit, u_limit): # simple operation like data slicing is done on the huge data
        print('Performing operation on huge data...')
        if self._real_resource is None:
            self._real_resource = HeavyResource()
        data = self._real_resource.getdata()
        data_slice = data[l_limit:u_limit]
        print(f'Squares of numbers from {l_limit} to {u_limit} is {data_slice}')

if __name__ == '__main__':
    proxy = HeavyResourceProxy() # At this point, HeavyResource is not yet created

    # Lazy initialization: HeavyResource was loaded only when it was absolutely necessary
    proxy.operation(20, 25)
    # Output: Loading huge data...
    # Performing operation on huge data...
    # Squares of numbers from 20 to 25 is [441, 484, 529, 576, 625]