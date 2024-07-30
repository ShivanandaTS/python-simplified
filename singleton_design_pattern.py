'''
Singleton design pattern:
-   is a creational pattern
-   it ensures the class has only one instance
-   greatly reduces the cost and expense of the project in terms of space and time

Use case: 
1. Database connectivity
-   Each object creating a new connection to the database will take a lot of time and space for execution
2. Configuration manager
'''

class ConfigManagerSingleton():
    _instance = None

    @staticmethod
    def get_instance():
        '''This method returns the instance of singleton method'''
        if ConfigManagerSingleton._instance is None:
            ConfigManagerSingleton()
        return ConfigManagerSingleton._instance

    def __init__(self, config={}):
        if ConfigManagerSingleton._instance is not None:
            raise Exception('Cannot instantiate singleton class multiple times!\nUse get_instance method.')
        self.config = config
        ConfigManagerSingleton._instance = self
    
    # Following static methods is not important as fas as 
    # understanding the concept of singleton concept is concerned
    @staticmethod
    def get(key):
        if not key in ConfigManagerSingleton._instance.config:
            return None
        ConfigManagerSingleton._instance.config.get(key)
    
    # Following static methods is not important as fas as 
    # understanding the concept of singleton concept is concerned
    @staticmethod
    def set(key, value):
        ConfigManagerSingleton._instance.config[key] = value

if __name__ == '__main__':
    cm1 = ConfigManagerSingleton() # first instance of singleton
    cm1.set('language', 'Python')
    cm1.set('db', 'MySQL')
    print('cm1 =', cm1)

    try:
        # an attempt to create second instance of singleton, results in an error.
        cm2 = ConfigManagerSingleton()
    except:
        # obtaining pre-existing singleton instance through get_instance staticmethod
        cm2 = ConfigManagerSingleton.get_instance()
    print('cm2 =', cm2)
    print(cm1 is cm2) # Output: True

    cm2.set('language', 'C++')
    # Checking whether changing config data through cm2 will be reflected in
    # config data of cm1 as well. Just to be absolutely sure that cm1 and cm2 are same.
    print(cm1.config) # Output: {'language': 'C++', 'db': 'MySQL'}
