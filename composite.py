# Composite Pattern (a GOOD design pattern)
# object pattern: relationships between objects are established at run time via composition
# structural pattern: composes classes and objects into larger structures
# - containers that contain containees, each of which could be a container
# - like decorator, create a "lowest common denominator" interface that makes your containers
#   and containees interchangeable, which specifies behaviors that can be exercised "uniformly"
#   accross all containee and container objects
# - all container and containee classes IS_A the same interface
# - all container classes HAS_A one-to-many interface
# - container classes delegate to their containee objects
# - container classes should have child management methods (add/remove child), 
#   safety vs. transparency: to treat leaf and composite objects uniformly, these methods
#   can be promoted to the interface
# - composite and decorator have similar structure diagrams, both relying on recursive
#   composition to organize open-ended (can be endless/infinite) number of objects
# - composite can use iterator to traverse its object, use visitor to add new operation
# - decorator is to let you add new responsibility to objects without subclassing, while
#   composite's focus is not on embellishment but on "representation"
# - transparency: perform operations on an object without needing to know there are many
#   objects inside

class MenuComponent(object):
    # a common interface, implemented by both indivisual and composite components
    # treat internal and leaf elements uniformly

    # child management operation, put in interface for transparency
    def add(self, menuComponent):
        raise NotImplementedError

    def getName(self):
        raise NotImplementedError

    def getDescription(self):
        raise NotImplementedError

    # operation
    def printOut(self):
        raise NotImplementedError

    # iterator
    def createIterator(self):
        raise NotImplementedError

class MenuItem(MenuComponent):
    # an indivisual component (leaf object)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    # iterator
    def createIterator(self):
        return NullIterator()

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def printOut(self):
        print 'Name: %s' % self.getName()
        print 'Description: %s' % self.getDescription()

class Menu(MenuComponent):
    # a composite component (composite objects), 
    # having aggregate of items (indiviual & composite components)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menuComponents = []
        self.iterator = None

    # iterator
    def createIterator(self):
        if self.iterator is None:
            self.iterator = CompositeIterator(MenuIterator(self.menuComponents))
        return self.iterator

    # composite related methods
    def add(self, menuComponent):
        self.menuComponents.append(menuComponent)

    # indivisual related methods
    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def printOut(self):
        print 'Name: %s' % self.name
        print 'Description: %s' % self.description

class Iterator(object):
    # iterator interface

    def hasNext(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

class MenuIterator(Iterator):

    def __init__(self, menuComponents):
        self.menuComponents = menuComponents
        self.position = 0

    def hasNext(self):
        if self.position < len(self.menuComponents):
            return True
        return False

    def next(self):
        menuComponent = self.menuComponents[self.position]
        self.position += 1
        return menuComponent

class CompositeIterator(Iterator):

    def __init__(self, iterator):
        self.stack = []
        self.stack.append(iterator)
        
    def hasNext(self):
        if self.stack == []:
            return False
        iterator = self.stack[-1]
        if not iterator.hasNext():
            self.stack.pop()
            return self.hasNext()
        return True

    def next(self):
        if self.hasNext():
            iterator = self.stack[-1]
            component = iterator.next()
            if isinstance(component, Menu):
                self.stack.append(component.createIterator())
            return component
        return None

class NullIterator(Iterator):

    def hasNext(self):
        return False

    def next(self):
        return None

class Waitress(object):
    # an client for trasvering all composite components

    def __init__(self, allMenus):
        self.allMenus = allMenus

    def printMenu(self):
        iterator = self.allMenus.createIterator()
        while iterator.hasNext():
            iterator.next().printOut()


pancakeMenu = MenuItem('Pancake Menu', 'Breakfast')

dessertMenu = Menu('Dessert Menu', 'Dessert')
dessertMenu.add(MenuItem('Apple Pie', 'Apple pie with vanilla'))

dinnerMenu = Menu('Dinner Menu', 'Dinner')
dinnerMenu.add(MenuItem('Pasta', 'Spagetti with bread'))
dinnerMenu.add(dessertMenu)

allMenus = Menu('All Menus', 'All that combined') # root
allMenus.add(pancakeMenu)
allMenus.add(dinnerMenu)

waitress = Waitress(allMenus)
waitress.printMenu()

