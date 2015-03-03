# Strategy Pattern
# object pattern: relationships between objects are established at run time via composition
# behavior pattern: how classes and objects interact and distribute responsibilities
# - strategy pattern is like template method except in its granularity
# - both defers implementation to subclasses, but
# - template method uses inheritance to vary "part" of an algorithm, while strategy
#   pattern uses delegation to vary the entire algorithm
# - template method modifies the logic of individual objects, while strategy pattern modifies
#   the logic of an entire class
# - open/close principle: clients couple themselves to an interface (rarely change), not to 
#   implementation (constantly change); the implementations of interface are effectively hidden
# - maximize cohesion, minimize coupling
# - strategy is like template method except in its granularity
# - state is like strategy except in its intent
# - strategy is a bind-once pattern, whereas state is more dynamic

class Duck(object):
    # an interface (program to interface, not an implementation)

    def performFly(self):
        # an operation on the delegated algorithm, can be replaced as a whole
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print 'all ducks float'


class FlyBehavior(object):
    # interface: easy to add new behavior via inheritance, open for extension
    # defer implementation to subclasses

    def fly(self):
        raise NotImplementedError

class FlyWithWings(FlyBehavior):
    # implementation

    def fly(self):
        print "I'm flying"

class FlyNoWay(FlyBehavior):

    def fly(self):
        print "I can't fly"

class QuackBehavior(object):
    # Interface

    def quack(self):
        raise NotImplementedError

class Quack(QuackBehavior):

    def quack(self):
        print 'Quack'

class MuteQuack(QuackBehavior):

    def quack(self):
        print 'Silence'

class MallardDuck(Duck):
    # Favor composition over inheritance
    # - uses delegation to vary the entire algorithm

    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print "I'm a real Mallard duck"

# client codes: program to interface not implementation, thus closed for modification
# - minimize coupling, since the client is coupled only to abstraction(interface)
mallard = MallardDuck()
mallard.performQuack()
mallard.performFly()
