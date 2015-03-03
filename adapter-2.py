# Adapter Pattern
# - wraps an existing class with a new interface

class LegacyLine(object):

    def draw(self, x1, y1, x2, y2):
        print 'line from (%s, %s) to (%s, %s)' % (x1, y1, x2, y2)

class LegacyRectangle(object):

    def draw(self, x, y, w, h):
        print 'rectangle at (%s, %s) with width %s and height %s' % (x, y, w, h)

class Shape(object):
    # adapter interface: a new interface that wraps an existing class

    def draw(self, x1, y1, x2, y2):
        raise NotImplementedError

class Line(Shape):
    # an implementation of adapter

    def __init__(self):
        self.adaptee = LegacyLine()

    def draw(self, x1, y1, x2, y2):
        self.adaptee.draw(x1, y1, x2, y2)

class Rectangle(Shape):
    # an implementation of adapter

    def __init__(self):
        self.adaptee = LegacyRectangle()

    def draw(self, x1, y1, x2, y2):
        self.adaptee.draw(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

shape1 = Line()
shape2 = Rectangle()
shape1.draw(10, 20, 30, 60)
shape2.draw(10, 20, 30, 60)
