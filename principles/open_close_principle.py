# Open/Close Principle
# - "open for extension, but closed for modification"
# - a program design that is easy to change with minimum changes in existing code
# - i.e adding a new feature does not affect the existing functionalities in an unwanted manner
#   and future changes are achieved by adding new code, not by changing exisiting code
# - common approaches:
#   a) dependency inversion (introduce new layer of abstraction, and program to interface)
#   b) inversion of control (dependency injection or service look-up)
#   c) used in decorator pattern, factory method, and observer pattern, etc.
#
# example
#
# (bad design: without open/close principle)

class Shape(object):
    ''' base class '''

    def __init__(self):
        self.type = None

class Rectangle(Shape):
    ''' a subclass of the base class '''

    def __init__(self):
        self.type = 1

class Circle(Shape):
    ''' a subclass of the base class '''

    def __init__(self):
        self.type = 2

class GraphicEditor(object):
    ''' a client class that uses the subclasses, but is not designed to be close for modification
        i.e. if a new shape is added, this class has to been modified accordingly
    '''

    def drawShape(self, shape):
        if shape.type == 1:
            self.drawRectangle()
        elif shape.type == 2:
            self.drawCircle()

    def drawRectangle(self):
        print "draw a rectangle"

    def drawCircle(self):
        print "draw a circle"

editor = GraphicEditor()
editor.drawShape(Rectangle())
editor.drawShape(Circle())

# (good design: with open/close principle)

class Shape(object):
    ''' an interface '''

    def draw(self):
        raise NotImplementedError

class Rectangle(Shape):
    ''' an implementation of the interface '''

    def draw(self):
        print "draw a rectangle"

class Circle(Shape):
    ''' an implementation of the interface '''

    def draw(self):
        print "draw a circle"

class GraphicEditor(object):
    ''' a client class that may uses the shape implementations
        it follows the open/close principle, i.e. adding a new implementation does not need to
        modify the code of the class
    '''

    def drawShape(self, shape):
        shape.draw()

editor = GraphicEditor()
editor.drawShape(Rectangle())
editor.drawShape(Circle())
