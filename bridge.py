# Bridge Pattern (a GOOD design pattern)
# - provides a way to decouple abstraction (abstract class) from implementation (interface)
#   builds abstraction and an implementation in such a way that either can vary independently 
# - adapter vs. bridge pattern:
#   bridge: designed up-front to let the abstraction and implementation vary independently
#   adapter: makes things work after they're designed
#
# (conventional)
#                     Shape                                .. (abstraction: by which client knows what it is)
#                      | |
#                  ----   ---- (IS_A)
#                  |         |       (IS_A)
#               Circle     Rectangle -------> WithDrawingAPIImpl1 .. (actual implementation)
#                                    -------> WithDrawingAPIImpl2
#
# (bridge pattern)
#
#                         (HAS_A)
#           Shape ------------------------> DrawingAPI        .. (implementation has its own interface)
#            | |                              |    |             (decouple abstrction and implementation)
#       -----  --------(IS_A)            -----    ----- (IS_A)
#       |             |                  |            |
#   Circle         Rectangle      DrawingImpl1  DrawingImpl2
#       .             .                 .             .                 
#       .             .                 .             .
#   (interface-implementation)       (actual implementation)
#
# example:
#
# (bad design)
class Shape(object):
    # abstraction

    def draw(self):
        raise NotImplementedError

class Circle(Shape):

    def draw(self, x, y, radius):
        raise NotImplementedError

class Rectangle(Shape):

    def draw(self, x, y, width, height):
        raise NotImplementedError

class CircleRedDrawing(Circle):

    def draw(self, x, y, radius):
        print "Drawing [ color: red, radius: " + radius + ", x: " + x + ", " + y + "]"

class CircleGreenDraw(Circle):

    def draw(self, x, y, radius):
        print "Drawing Circle[ color: green, radius: " + radius + ", x: " + x + ", " + y + "]"

class RectangleRedDrawing(Rectangle):

    def draw(self, x, y, width):
        print "Drawing Rectangle[ color: red, width: " + width + ", " + x + ", " + y + "]"

class RectangleGreenDrawing(Shape):

    def draw(self, x, y, width):
        print "Drawing Rectangle[ color: green, width: " + width + ", " + x + ", " + y + "]"

# why is it bad?
#   abastraction and implemenation are tightly coupled; they cannot vary independently
# 
# (abstraction)               (implementation)
# Shape ------> Circle -----> CircleRedDrawing
#                      -----> CircleGreenDrawing
#       ------> Rectangle --> RectangleRedDrawing
#                         --> RectangleGreenDrawing

# (good design: extract implementation, creating its own interface for variation)
class Shape(object):
    # abstraction

    def __init__(self, drawingAPI):
        self.drawingAPI = drawingAPI # abstraction HAS_A implementation interface (working like an adapter) 

    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    # abstraction can have many implementations and new abstractions can be added easily

    def __init__(self, x, y, radius, drawingAPI):
        super(Circle, self).__init__(drawingAPI)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawingAPI.drawCircle(self.x, self.y, self.radius)

class Rectangle(Shape):
    # abstraction can have many implementations and new abstractions can be added easily

    def __init__(self, x, y, width, drawingAPI):
        super(Circle, self).__init__(drawingAPI)
        self.x = x
        self.y = y
        self.width = width

    def draw(self):
        self.drawingAPI.draw(self.x, self.y, self.width)

class DrawingAPI(object):
    # implemenation has its own interface 

    def draw(self):
        raise NotImplementedError

class DrawingRed(DrawingAPI):
    # a concrete implementation

    def draw(self, x, y, radius):
        print 'API1 draws a red shape at (%.2f, %.2f) with radius %.2f' % (x, y, radius)

class DrawingGreen(DrawingAPI):
    # a concrete implementation

    def draw(self, x, y, width):
        print 'API2 draws a green shape at (%.2f, %.2f) with width %.2f' % (x, y, width)

# the abstraction instance takes the implementation instance as a parameter of its constructor
shape = Circle(1, 2, 3, DrawingRed())
shape.draw()
shape2 = Circle(2, 3, 4, DrawingGreen())
shape2.draw()
shape = Rectangle(1, 2, 3, DrawingRed())
shape.draw()
shape2 = Rectangle(2, 3, 4, DrawingGreen())
shape2.draw()

