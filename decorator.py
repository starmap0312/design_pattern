# Decorator Pattern (a GOOD design pattern)
# - adapter pattern vs. decorator pattern:
#   (both applying the dependency inversion principle: adding an abstraction layer)
#
#   adapter pattern:
#
#            Target Interface
#                   ^
#            (IS_A) |     (HAS_A)             (IS_A) 
#                Adapter ........> "Adaptee" <------- AdapteeExample
#                                "abstraction"
#
#     (Adapter & AdapteeExample both depend on an abstraction, making them "loosely coupled")
#
#   decorator pattern:
#
#                         "abstraction"
#                   --> "Common Interface" <-----
#                   |             ^             |
#            (IS_A) |     (HAS_A) |             | (IS_A) 
#                Decorater ........         Decoratee
#                   ^
#            (IS_A) |
#            DecoraterExample
#
#     (Decorater & Decoratee both depend on an abstraction, making them "loosely coupled")
#

# 1. create a "lowest common denominator" (common interface), making classes interchangeable
class Widget(object):

    def draw(self):
        raise NotImplementedError

# 3. core class IS_A common interface
class TextField(Widget):
    # core object

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def draw(self):
        print 'TextField: %s x %s' % (self.width, self.height)

# 2. create a decorator base class also IS_A common interface
class Decorator(Widget):

    def __init__(self, widget):
        # 4. decorator class HAS_A instance of the common interface (core object)
        self.widget = widget

    # 5. decorator delegates to the HAS_A object (core object)
    def draw(self):
        self.widget.draw()

# 6. create a decorator derived classes for optional embellishment
class BorderDecorator(Decorator):

    def draw(self):
        self.widget.draw()
        print 'BorderDecorator'

class ScrollDecorator(Decorator):

    def draw(self):
        self.widget.draw()
        print 'ScrollDecorator'

# 8. client has the responsibility to compose desired configurations
widget = BorderDecorator(BorderDecorator(ScrollDecorator(TextField(80, 24))))
widget.draw()
