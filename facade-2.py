# Facade Pattern
# - a unified interface to a set of interfaces in a subsystem, a higher-level interface
#   that makes the subsystem easier to use
# - decouples the subsystem from its clients
# - facade defines a new interface, whereas adapter makes two existing interfaces work together
# - both mediator and facade abstracts functionality of existing classes; mediator abstracts/
#   centralizes arbitrary communications between colleague objects; facade defines a simpler
#   interface to a subsystem
# - mediator routinely "adds value" and is known/referenced by the colleague objects; in contrast,
#   facade does not add new functionality and is not known by the subsystem classes
# - abstract factory can be used as an alternative to facade to "hide platform-specific classes"
# - facade and adapter are different kinds of wrappers: the intent of facade is to produce a 
#   simpler interface, whereas the intent of adapter is to design to an existing interface
# - although facade often wraps multiple objects and adapter wraps a single object,
#   facade could front-end a single complex object and adapter could wrap several legacy objects
# - facade objects are often singletons because only one facade object is required

# 1. identify the desired unified interface for a set of subsystems
class PointCarte(object):
    # a subsystem

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class PointPolar(object):
    # another subsystem

    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle

    def rotate(self, ang):
        self.angle += ang 
        self.angle %= 360

    def __str__(self):
        return '[%s@%s]' % (self.radius, self.angle)

class Point(object):
    # a desired, unified interface with move & rotate methods

    def __init__(self, x, y):
        self.pc = PointCarte(x, y)

    def __str__(self):
        return self.pc.__str__()

    # 4. the facade/wrapper "maps" to the APIs of the subsystems
    def move(self, dx, dy):
        self.pc.move(dx, dy)

    def rotate(self, angle, point):
        x = self.pc.getX() - point.pc.getX()
        y = self.pc.getY() - point.pc.getY()
        import math
        pp = PointPolar(math.sqrt(x*x+y*y), math.atan2(y, x)*180/math.pi)
        pp.rotate(angle)
        print '  PointPolar is %s' % pp

class Line(object):

    def __init__(self, ori, end):
        self.o = ori
        self.e = end

    def move(self, dx, dy):
        self.o.move(dx, dy)
        self.e.move(dx, dy)

    def rotate(self, angle):
        self.e.rotate(angle, self.o)

    def __str__(self):
        return 'origin is %s, end is %s' % (self.o, self.e)

# 3. the client uses the facade (thus is coupled to facade, and decouples from subsystems)
line1 = Line(Point(2, 4), Point(5, 7))
line1.move(-2, -4)
print 'after move: %s' % line1
