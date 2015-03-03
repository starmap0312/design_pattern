# Decorator Pattern
# object pattern: relationships between objects are established at run time via composition
# structural pattern: composes classes or objects into larger structures
# - attach additional responsibilities to an object "dynamically" (wraps object at run time)
# - provide a flexible alternative to subclassing for extending functionality
# - both the decorator objects and the original object inherit the same base interface
# - the decorator class declares a composition relationship to the base interface
#   with a data member initialized in its constructor
# - adapter provides a different interface to its subject, proxy provides the same interface,
#   decorator provides an enhanced interface
# - decorator is more transparent to the client than adapter, supporting recursive composition
# - composite and decorator have similar structure diagram, both rely on recursive composition
#   to organize an open-ended number of objects
#   decorator: single child, composite: a list of children (internal nodes: decorator objects, 
#   leaves: core objects)
# - decorator can be viewed s a degenerate composite with single child. 
#   decorator adds additional responsibilities, not intended for object aggregation(composite)
# - decorator and proxy have similar structures but different purposes, both describe how
#   to provide a level of indirection to another object by keeping a reference to the object
#   to which they forward requests

class Beverage(object):
    # common interface

    def __init__(self):
        self.description = 'Unknown Beverage'

    def getDescription(self):
        return self.description

    def cost(self):
        raise NotImplementedError

class CondimentDecorator(Beverage):
    # decorator interface

    def getDescription(self):
        raise NotImplementedError

class Expresso(Beverage):
    # concrete implementation, core

    def __init__(self):
        self.description = 'Expresso'

    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    # concrete implementation, core

    def __init__(self):
        self.description = 'House Blend Coffee'

    def cost(self):
        return 0.89

class Mocha(CondimentDecorator):
    # decorator implementation

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ', Mocha'

    def cost(self):
        return self.beverage.cost() + 0.2


class Soy(CondimentDecorator):
    # decorator implementation

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ', Soy'

    def cost(self):
        return self.beverage.cost() + 0.4

beverage = Soy(Mocha(Expresso()))
print beverage.getDescription(), '$%s' % beverage.cost()
beverage2 = Soy(Soy(Mocha(HouseBlend())))
print beverage2.getDescription(), '$%s' % beverage2.cost()
