# Flyweight Pattern
# use a centralized collection to reduce memory and creation overhead 

class CoffeeFlavor(object):
    # indivisual objects

    def __init__(self, newFlavor):
        self.name = newFlavor

    def __str__(self):
        return self.name

class Menu(object):
    # use a centralized collection to represent coffee flavor objects
    # objects already created will be shared

    def __init__(self):
        self.flavors = dict()

    def lookup(self, flavorName):
        # create coffee flavor object at run time if not in the centralized collection
        if flavorName not in self.flavors:
            self.flavors[flavorName] = CoffeeFlavor(flavorName)
        return self.flavors[flavorName]

    def totalCoffeeFlavorsMade(self):
        return len(self.flavors)

class Order(object):

    def __init__(self, tableNumber, flavor):
        self.tableNumber = tableNumber
        self.flavor = flavor

    def serve(self):
        print 'Serving %s to table %s' % (self.flavor, self.tableNumber)

class CoffeeShop(object):

    def __init__(self):
        self.orders = []
        self.menu = Menu() # sometimes declared as a static member

    def takeOrder(self, flavorName, tableNumber):
        # if not using flyweight pattern, just create object by CoffeeFlavor(flavorName)
        flavor = self.menu.lookup(flavorName) # get object from a centralized collection
        order = Order(tableNumber, flavor)
        self.orders.append(order)

    def service(self):
        for order in self.orders:
            order.serve()

    def report(self):
        return 'Total CoffeeFlavor objects made: %s' % self.menu.totalCoffeeFlavorsMade()

shop = CoffeeShop()
shop.takeOrder("Cappuccino", 2)
shop.takeOrder("Frappe", 1)
shop.takeOrder("Espresso", 1)
shop.takeOrder("Frappe", 897)
shop.takeOrder("Cappuccino", 97)
shop.takeOrder("Frappe", 3)
shop.takeOrder("Espresso", 3)
shop.takeOrder("Cappuccino", 3)
shop.service()
print shop.report()
