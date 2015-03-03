# Bridge Pattern
# - provides a way to decouple abstraction(interface) and implementation
# - bridge pattern is designed up-front to let the abstraction and implementation
#   vary independently. Adapter makes things work after they're designed

class Shape(object):
    # abstraction interface

    def __init__(self, drawingAPI):
        # abstraction HAS_A implementation
        self.drawingAPI = drawingAPI

    def draw(self):
        raise NotImplementedError

class CircleShape(Shape):
    # an abstraction implementation, note that abstraction can also have many implementations
    # new abstraction can be added easily

    def __init__(self, x, y, radius, drawingAPI):
        super(CircleShape, self).__init__(drawingAPI)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawingAPI.drawCircle(self.x, self.y, self.radius)

class DrawingAPI(object):
    # implementation interface

    def drawCircle(self, x, y, radius):
        raise NotImplementedError

class DrawingAPI1(DrawingAPI):
    # implementation of implementation
    # new implementation can be added easily

    def drawCircle(self, x, y, radius):
        print 'API1 draws a circle at (%.2f, %.2f) with radius %.2f' % (x, y, radius)

class DrawingAPI2(DrawingAPI):
    # implementation of implementation

    def drawCircle(self, x, y, radius):
        print 'API2 draws a circle at (%.2f, %.2f) with radius %.2f' % (x, y, radius)

# the abstraction instance takes the implementation instance as a parameter of constructor
shape = CircleShape(1, 2, 3, DrawingAPI1())
shape.draw()
shape2 = CircleShape(2, 3, 4, DrawingAPI2())
shape2.draw()
