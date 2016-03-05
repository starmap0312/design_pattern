# Liskov Substitution Principle
# - derived classes must be completely substitutable for their base classes
#   i.e. if S is a subclass of T, then objects of class T can be replaced with objects of
#   class S without altering the program
# - follow (strong) behavioral subtyping when creating class hierarchies
#   i.e. new derived classes are extending the base classes without changing their behavior
# - design by contrast methodology:
#   a) preconditions cannot be strengthened in a subtype (ex. method arguments)
#   b) postconditions cannot be weakened in a subtype (ex. return types)
#   c) invariants of the supertype must be preserved in a subtype (ex. one cannot define a 
#      mutable point as a subtype of an immutable point; on the other hand, additional fields 
#      added in the subtype may however be modified)
#      i.e. the state of the class is maintained within specified tolerances
# - a counter example: Square as a subclass of Rectangle

class Rectangle(object):
    ''' super class '''

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
    ''' a subclass: assuming that width is always equal to height
        this violates the Liskov substitution principle, as in the behavior of Rectangle 
        the width and height can be modified independently
        i.e. the subclass weakens the postconditions for the Rectangle setters
    '''

    def setWidth(self, width):
        self.width = width
        self.height = width

    def setHeight(self, height):
        self.width = height
        self.height = height

class AbstractFactory(object):

    @staticmethod
    def getRectangle():
        return Square()

rectangle = AbstractFactory.getRectangle()
rectangle.setWidth(5)
rectangle.setHeight(10)
print rectangle.getArea()
