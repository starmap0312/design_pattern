# Strategy Pattern
# object pattern: relationships between objects are established at run time via composition
# behavior pattern: how classes and objects interact and distribute responsibilities
# - strategy pattern is like template method except in its granularity
#   (both defers implementation to subclasses)
# - template method uses inheritance to vary "part" of an algorithm, while strategy
#   pattern uses delegation to vary the entire algorithm
# - template method modifies the logic of individual objects, while strategy pattern modifies
#   the logic of an entire class
# - open/close principle: clients couple themselves to an interface (rarely change), not to 
#   implementation (constantly change); the implementations of interface are effectively hidden
# - maximize cohesion and minimize coupling
# - state is like strategy except in its intent
# - strategy is a bind-once pattern, whereas state is more dynamic
#
#                                (HAS_A)
#       Client ...................................> Service1 ... ...    Service2
#          ^                                           ^                   ^
#          | (IS_A)  constructs via composition        | (IS_A)            |
#    ClientExample ..............................> Service1Example ... Service2Example
#
# example: strategy pattern with composition

class Duck(object):
    ''' a superclass with (template) methods defining how the client will use the algorithms
        the construction of the algorithm objects is defined in subclasses
        the client is coupled only to abstraction (interface) of the algorithms
        minimize coupling: program to interface not implementation (closed for modification)
    '''

    def performFly(self):
        # use of the algorithm object (an operation on the delegated algorithm
        self.flyBehavior.fly()

    def performQuack(self):
        # use of the algorithm object (an operation on the delegated algorithm
        self.quackBehavior.quack()

    def swim(self):
        print 'all ducks float'

class FlyBehavior(object):
    ''' an interface for the fly behavior
        easy to add new behavior via inheritance (open for extension)
        defer implementation to subclasses
    '''

    def fly(self):
        raise NotImplementedError

class FlyWithWings(FlyBehavior):
    ''' an implementation of the FlyBehavior interface '''

    def fly(self):
        print "I'm flying"

class FlyNoWay(FlyBehavior):
    ''' an implementation of the FlyBehavior interface '''

    def fly(self):
        print "I can't fly"

class QuackBehavior(object):
    ''' an interface for the quack behavior
        easy to add new behavior via inheritance (open for extension)
        defer implementation to subclasses
    '''

    def quack(self):
        raise NotImplementedError

class Quack(QuackBehavior):
    ''' an implementation of the QuackBehavior interface '''

    def quack(self):
        print 'Quack'

class MuteQuack(QuackBehavior):
    ''' an implementation of the QuackBehavior interface '''

    def quack(self):
        print 'Silence'

class MallardDuck(Duck):
    ''' an implementation of the Duck superclass '''

    def __init__(self):
        # creation of the algorithm objects, can be replaced as a whole
        # it favors composition over inheritance
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print "I'm a real Mallard duck"

# the client creates the Duck implementation object, but calls the superclass' template method
# if the construction of the implementation object is separated (ex. injected), the client can
# be loosely coupled with the implementation object
mallard = MallardDuck()
mallard.performQuack()
mallard.performFly()
