# Bridge Pattern (a GOOD design pattern)
# - provides a way to decouple abstraction (interface) from implementation
#   builds an interface and an implementation in such a way that either can vary independently 
# - bridge pattern is designed up-front to let the abstraction and implementation vary independently
#   whereas adapter makes things work after they're designed
#
# (conventional)
#                     Shape                                   .. (interface: by which client knows how to use implementation)
#                      | |
#                  ----   ---- (IS_A)
#                  |         |         (HAS_A)
#               Circle     Rectangle -----------> DrawingImpl .. (actual implementation)
#
# (bridge pattern)
#
#                         (HAS_A)
#           Shape ------------------------> DrawingAPI        .. (actual implementation has their own interface)
#            | |                              |    |             (decouple interface-implementation from actual implementation)
#       -----  --------(IS_A)            -----    ----- (IS_A)
#       |             |                  |            |
#   Circle         Rectangle      DrawingImpl1  DrawingImpl2
#       .             .                 .             .                 
#       .             .                 .             .
#   (interface-implementation)       (actual implementation)
#

class Shape(object):
    # an interface for the abstractions

    def __init__(self, drawingAPI):
        # the abstraction interface, it HAS_A implementation interface (working like an adapter) 
        self.drawingAPI = drawingAPI

    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    # an implementation of the abstraction interface
    # so that the abstraction can have many implementations and new abstractions can be added easily

    def __init__(self, x, y, radius, drawingAPI):
        super(Circle, self).__init__(drawingAPI)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawingAPI.drawCircle(self.x, self.y, self.radius)

class DrawingAPI(object):
    # an interface for the implemenation instances

    def drawCircle(self, x, y, radius):
        raise NotImplementedError

class DrawingImpl1(DrawingAPI):
    # an instance of the implementation interface

    def drawCircle(self, x, y, radius):
        print 'API1 draws a circle at (%.2f, %.2f) with radius %.2f' % (x, y, radius)

class DrawingImpl2(DrawingAPI):
    # an instance of the implementation interface

    def drawCircle(self, x, y, radius):
        print 'API2 draws a circle at (%.2f, %.2f) with radius %.2f' % (x, y, radius)

# the abstraction instance takes the implementation instance as a parameter of its constructor
shape = Circle(1, 2, 3, DrawingImpl1())
shape.draw()
shape2 = Circle(2, 3, 4, DrawingImpl2())
shape2.draw()
