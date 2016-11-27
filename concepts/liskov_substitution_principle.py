# Liskov Substitution Principle
# - base class objects can be replaced by derived class objects without altering the program
#   i.e. if class S extends class T, then
#        anywhere T's objects can be replaced by S's objects without altering the program
# - follow (strong) behavioral subtyping when creating class hierarchies
#   i.e. new derived classes are extending the base classes without changing their behavior
# - design by contrast methodology:
#   a) preconditions cannot be strengthened in a subtype
#      ex. method arguments cannot be strengthened
#   b) postconditions cannot be weakened in a subtype
#      ex. return types cannot be weakened
#   c) invariants of the supertype must be preserved in a subtype
#      ex. one cannot define a mutable point as a subtype of an immutable point
#          however, additional fields added in the subtype may be modified
#          (the state of the class is maintained within specified tolerances)
#
# example
#
# (bad design: class Square extends class Rectangle)

class Rectangle(object):
    ''' base class '''

    def __init__(self):
        self.width = None
        self.height = None

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

class Square(Rectangle):
    ''' derived class: assuming that width is always equal to height
        violate the Liskov substitution principle: derived class weakens the postconditions
        the width and height of Rectangle can be modified independently
        the width and height of Square cannot be modified independently
        we cannot replace Rectangle objects by Square objects
    '''

    def setWidth(self, width):
        self.width = width
        self.height = width

    def setHeight(self, height):
        self.width = height
        self.height = height

class AbstractFactory(object):

    @staticmethod
    def getSquare():
        return Square()

    @staticmethod
    def getRectangle():
        return Rectangle()

rectangle = AbstractFactory.getRectangle()
rectangle.setWidth(5)
rectangle.setHeight(10)
print rectangle.getArea()

# we cannot replace Rectangle objects by Square objects
square = AbstractFactory.getSquare()
square.setWidth(5)
square.setHeight(10)
print square.getArea()

# (good design: class Rectangle extends class Square)

class Square(object):
    ''' super class '''

    def __init__(self):
        self.width = None
        self.height = None

    def setWidth(self, width):
        self.width = width
        self.height = width

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.width = height
        self.height = height

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.getWidth() * self.getHeight()

class Rectangle(Square):
    ''' derived class '''

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

square = AbstractFactory.getSquare()
square.setWidth(5)
square.setHeight(10)
print square.getArea()

# Square objects can be completely replaced by Rectangle objects
rectangle = AbstractFactory.getRectangle()
rectangle.setWidth(5)
rectangle.setHeight(10)
print rectangle.getArea()
