# Bridge Pattern (a GOOD design pattern)
# - provides a way to decouple abstraction (interface) from implementation
# - bridge pattern is designed up-front to let the abstraction and implementation
#   so that they can vary independently, whereas adapter makes things work after they're designed
#
# (conventional)
#                     Shape             ...... (interface: by which the client knows how to use the implementation)
#                      | |
#                  ----   ---- (IS_A)
#                  |         |
#            DrawingAPI1  DrawingAPI2   ...... (implementation)
#
# (bridge pattern)
#
#                         (HAS_A)
#           Shape ------------------------> DrawingAPI
#            | |                              |    | 
#       -----  --------(IS_A)            -----    ----- (IS_A)
#       |             |                  |            |
#   CircleShape RectangleShape      DrawingAPI1  DrawingAPI2 .......... (the actual implementation has their own interface)
#       .             .                                                 (thus decoupled from actual interface implementation)
#       .             .
#   (the actual interface implementation: by which the client  knows how to use the implementation)
#

class Shape(object):
    # an interface for the abstractions

    def __init__(self, drawingAPI):
        # the abstraction interface, it HAS_A implementation interface (working like an adapter) 
        self.drawingAPI = drawingAPI

    def draw(self):
        raise NotImplementedError

class CircleShape(Shape):
    # an implementation of the abstraction interface
    # so that the abstraction can have many implementations and new abstractions can be added easily

    def __init__(self, x, y, radius, drawingAPI):
        super(CircleShape, self).__init__(drawingAPI)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawingAPI.drawCircle(self.x, self.y, self.radius)

class DrawingAPI(object):
    # an interface for the implemenation instances

    def drawCircle(self, x, y, radius):
        raise NotImplementedError

class DrawingAPI1(DrawingAPI):
    # an instance of the implementation interface

    def drawCircle(self, x, y, radius):
        print 'API1 draws a circle at (%.2f, %.2f) with radius %.2f' % (x, y, radius)

class DrawingAPI2(DrawingAPI):
    # an instance of the implementation interface

    def drawCircle(self, x, y, radius):
        print 'API2 draws a circle at (%.2f, %.2f) with radius %.2f' % (x, y, radius)

# the abstraction instance takes the implementation instance as a parameter of its constructor
shape = CircleShape(1, 2, 3, DrawingAPI1())
shape.draw()
shape2 = CircleShape(2, 3, 4, DrawingAPI2())
shape2.draw()
