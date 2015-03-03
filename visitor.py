# Visitor Pattern
# a way to easily add new operations on existing object structures
# open/closed principle: open for extension, but closed for modification

class Visitor(object):
    # visitor interface, can define many implementation of new operations on car elements
    # in addition, a visitor can have state, so that an operation can depend on previous action
    # visitor embodies strategy

    def visit(self, carElement):
        raise NotImplementedError

class CarElement(object):
    # car element interface, accepts any visitor implementation of new operation, by
    # calling back to the visitor, the visit method, and passes itself as an argument
    # to perform the new operation it defines

    def accept(self, visitor):
        # any CarElement object can accepts a visitor object, implementing a new operation
        # on the CarElement object, therefore the CarElement object has to pass itself (self)
        # to the visitor's visit method
        raise NotImplementedError

class Wheel(CarElement):
    # an indivisual object

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def accept(self, visitor):
        visitor.visit(self)

class Body(CarElement):
    # an indivisual object

    def accept(self, visitor):
        visitor.visit(self)

class Car(CarElement):
    # a composite component

    def __init__(self):
        self.elements = [Wheel('front left'), Wheel('front right'),
                         Wheel('back left'), Wheel('back right'),
                         Body()]

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)
        visitor.visit(self)

class PrintVisitor(Visitor):
    # the codes of the new operation on all the car elements are centralized here

    def visit(self, carElement):
    # the new operation is defined in visitor which avoids polluting the original classes
        if type(carElement) is Wheel:
            print 'Visiting %s wheel' % carElement.getName()
        elif type(carElement) is Body:
            print 'Visiting body'
        elif type(carElement) is Car:
            print 'Visiting car'

# the client calls its accept method, which in effect calls the visitor defined new operation
car = Car()
car.accept(PrintVisitor())
