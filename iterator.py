# Iterator Pattern
# object pattern: relationships between objects are established at run time via composition
# behavior pattern: how classes and objects interact and distribute responsibilities

class MenuItem(object):
    # items

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
    # iterator interface

    def hasNext(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

class DinerMenuIterator(Iterator):
    # an iterator over items

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
    # an aggregate interface that can create an iterator for its items

    def createIterator(self):
        raise NotImplementedError

class DinerMenu(Menu):
    # an implementaion of aggregate interface

    MAX_ITEMS = 3

    def __init__(self):
        self.numberOfItems = 0
        self.menuItems = []
        self.addItem('Pancake', 2.99, 'pancake with eggs and toast')
        self.addItem('Waffles', 3.12, 'waffles with blueberries')
        self.addItem('Waffles A', 4.12, 'waffles with blueberries')
        self.addItem('Waffles B', 5.12, 'waffles with blueberries')

    def createIterator(self):
        return DinerMenuIterator(self.menuItems)

    def addItem(self, name, price, description):
        if self.numberOfItems >= DinerMenu.MAX_ITEMS:
            print 'Menu is full!'
        else:
            self.menuItems.append(MenuItem(name, price, description))
            self.numberOfItems += 1

class Waitress(object):
    # aggregates of items, able to create iterators for item traversal

    def __init__(self, dinerMenu):
        self.dinerMenu = dinerMenu

    def printMenu(self):
        iterator = self.dinerMenu.createIterator()
        self.printIterator(iterator)

    def printIterator(self, iterator):
        # can print out any iterators
        while iterator.hasNext():
            menuItem = iterator.next()
            print menuItem.getName()
            print menuItem.getPrice()
            print menuItem.getDescription()

dinerMenu = DinerMenu()
waitress = Waitress(dinerMenu)
waitress.printMenu()
