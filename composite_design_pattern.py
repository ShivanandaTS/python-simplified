'''
Composite design pattern:
-   it is a structural design pattern
-   lets you compose objects into tree structures
-   allows client to treat individual objects and compositions of objects uniformly
Components:
-   Component - an abstract class/interface declaring common operations 
                for both simple and complex objects of the composition
    Leaf - simple end objects of the composition. leaf objects cannot have children.
    Composite - complex objects that may have children. it typically delegates the 
                operations to its children.
'''

from abc import ABC, abstractmethod

# Component class
class FamilySystemComponent(ABC):
    @abstractmethod
    def show_info(self):
        '''implemented in subclasses'''

# Composite class
class Clan(FamilySystemComponent):
    def __init__(self, name: str):
        self.name = name + ' ' + self.__class__.__name__
        self.children = []
    
    def add(self, child: FamilySystemComponent):
        '''adds a given child object to the composite object'''
        self.children.append(child)
    
    def remove(self, child: FamilySystemComponent):
        '''unlinks the child (leaf/composite) object from its parent composite object'''
        self.children.remove(child)
    
    def show_info(self):
        '''this function displays the info of the composite object'''
        if not getattr(self, 'children', None):
            print(f'{self.name} has no child.')
            return
        descendants = self.recursive_technique(person=self)
        descendants = list(dict.fromkeys(descendants)) # removing duplicates
        descendants = sorted(descendants, key=lambda x: x.find('Clan')) # moving clan names to the end
        print(f'Descendants of {self.name} are {descendants}')
    
    def looping_technique(self, descendants=[]):
        '''this function returns all the descendants of the composite object by looping method'''
        queue = self.children[:]
        while queue:
            child = queue.pop(0)
            descendants.append(child.name)
            if getattr(child, 'children', None):
                queue.extend(child.children)
        return descendants
    
    def recursive_technique(self, person: FamilySystemComponent, descendants=[]):
        '''this function returns all the descendants of the composite object by recursive method'''
        for child in person.children:
            descendants.append(child.name)
            if getattr(child, 'children', None):
                self.recursive_technique(child, descendants)
        return descendants

# Leaf class
class Member(FamilySystemComponent):
    def __init__(self, name, parent='Unknown'):
        self.name = name
        self.parent = parent
        if isinstance(self.parent, FamilySystemComponent):
            self.parent.add(self)
    
    def show_info(self):
        '''this function displays the info of the leaf object'''
        if isinstance(self.parent, FamilySystemComponent):
            clan_name = self.parent.name
            print(f'{self.name} belongs to {clan_name}')
        elif isinstance(self.parent, str):
            print(f'{self.name} is descendant of {self.parent}')
        else:
            print(f'{self.name} is descendant of unknown clan')
            

if __name__ == '__main__':
    # creating composite objects
    kaguya_clan = Clan('Kaguya')
    uchiha_clan = Clan('Uchiha')
    senju_clan = Clan('Senju')
    uzumaki_clan = Clan('Uzumaki')

    # branching composites
    kaguya_clan.add(uchiha_clan)
    kaguya_clan.add(senju_clan)
    senju_clan.add(uzumaki_clan)

    # creating leaf objects
    kaguya = Member('Kaguya', kaguya_clan)
    hagoromo = Member('Hagoromo', kaguya_clan)
    hamura = Member('Hamura', kaguya_clan)
    indra = Member('Indra', uchiha_clan)
    ashura = Member('Ashura', senju_clan)
    madara = Member('Madara', uchiha_clan)
    hashirama = Member('Hashirama', senju_clan)
    obito = Member('Obito', uchiha_clan)
    itachi = Member('Itachi', uchiha_clan)
    sasuke = Member('Sasuke', uchiha_clan)
    kushina = Member('Kushina', uzumaki_clan)
    naruto = Member('Naruto', uzumaki_clan)

    # calling abstractmethod to display the info of the composite and leaf objects
    senju_clan.show_info()
    kaguya_clan.show_info()
    hashirama.show_info()
    itachi.show_info()
    naruto.show_info()