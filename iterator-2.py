# Iterator Pattern
# object pattern: relationships between objects are established at run time via composition
# behavior pattern: how classes and objects interact and distribute responsibilities

class MenuItem(object):
    ''' the element class of the aggregate '''

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

class Iterator(object):
    ''' the iterator interface with hasNext() and next() methods '''

    def hasNext(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

class DinerMenuIterator(Iterator):
    ''' an implementation of the iterator '''

    def __init__(self, items):
        self.position = 0
        self.items = items

    def hasNext(self):
        if self.position >= len(self.items) or self.items[self.position] is None:
            return False
        return True

    def next(self):
        item = self.items[self.position]
        self.position += 1
        return item

class Menu(object):
    ''' the aggregate interface with createIterator() method '''

    def createIterator(self):
        raise NotImplementedError

class DinerMenu(Menu):
    ''' an implementaion of the aggregate interface '''

    MAX_ITEMS = 3

    def __init__(self):
        self.numberOfItems = 0
        self.menuItems = []

    def createIterator(self):
        return DinerMenuIterator(self.menuItems)

    def addItem(self, name, price, description):
        if self.numberOfItems >= DinerMenu.MAX_ITEMS:
            print 'Menu is full!'
        else:
            self.menuItems.append(MenuItem(name, price, description))
            self.numberOfItems += 1

class Waitress(object):
    ''' the client of the iterator '''

    def __init__(self, dinerMenu):
        self.dinerMenu = dinerMenu

    def printMenu(self):
        # use the iterator to print out all elements of the aggregate object
        iterator = self.dinerMenu.createIterator()
        while iterator.hasNext():
            menuItem = iterator.next()
            print menuItem.getName()
            print menuItem.getPrice()
            print menuItem.getDescription()

dinerMenu = DinerMenu()
dinerMenu.addItem('Pancake', 2.99, 'pancake with eggs and toast')
dinerMenu.addItem('Waffles', 3.12, 'waffles with blueberries')
dinerMenu.addItem('Waffles A', 4.12, 'waffles with blueberries')
dinerMenu.addItem('Waffles B', 5.12, 'waffles with blueberries')
waitress = Waitress(dinerMenu)
waitress.printMenu()
