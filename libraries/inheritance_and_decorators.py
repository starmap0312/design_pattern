# two types of decorations:
#   Type 1) decorating an exsiting functionality of an object
#   Type 2) adding one additional functionality to an object (works as inheritance)
#
# how to define a family of decorators, each of which add one additional functionality to the object 
#   define an abstract decorator, which is inherited by a set of decorator subclasses
#
# inheritence/subclassing itself is not evil, it enables polymorphism
#   it derives a characteristic from a base object
#   ex. MallardDuck (subclass) is a type of Duck (superclass): Duck should be able to quack() and fly()

from abc import ABCMeta, abstractmethod

# how to define multiple decorators, each of which add one more additional functionality 
class Interface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def basic_func(self):
        pass

class ConcreteObject(Interface):

    def basic_func(self):
        return 'this is a basic functionality of the concrete object'

# example 1: (Type 1) simple decorator, decorating the object's basic funcationality

class SimpleDecorator(Interface):

    def __init__(self, interface):
        self.interface = interface

    def basic_func(self):
        return self.interface.basic_func() + ', added something new to the basic functionality'

obj = SimpleDecorator(ConcreteObject())
print obj.basic_func()


# example 2: (bad design) inheritance that adds one additional funcationality to an object

class SubclassObject(ConcreteObject):

    def more_func(self):
        return 'this is a new functionality'

# this is a bad design, as it inherits (may override) an concrete class
# it creates tight coupling between SubclassObject (derived class) and ConcreteObject (base class)
# implementation inheritance is bad:
#   a procedural technique for code reuse and turns objects into containers with data and procedures
obj = SubclassObject()
print obj.basic_func()
print obj.more_func()


# example 2: (good design) decorator that adds one additional funcationality to an object

class MoreFuncDecorator(Interface):

    def __init__(self, interface):
        self.interface = interface

    def basic_func(self):
        return self.interface.basic_func()   # preserves the object's basic functionality

    def more_func(self):
        return 'this is a new functionality'

# we program to interface instead, not to implementation
# it creates loose coupling between MoreFuncDecorator (decorator class) and ConcreteObject (base class)
obj = MoreFuncDecorator(ConcreteObject())
print obj.basic_func()
print obj.more_func()


# example 4: (Type 2) a famility of decorators, each of which adds one additional functionality to the object

class AbstractDecorator(Interface):          # should not be instantiated (declare as abstract class in Java)
                                             # it's for code reusibility
    def __init__(self, interface):
        self.interface = interface

    def basic_func(self):
        return self.interface.basic_func()

class ConcreteDecorator1(AbstractDecorator): # inherit the basic func() from the AbstractDecorator directly

    def __init__(self, interface):
        super(ConcreteDecorator1, self).__init__(interface) # calls the superclass's constructor

    def more_func_1(self):                                  # implement an additional functionality
        return 'this is a new functionality'


class ConcreteDecorator2(AbstractDecorator): # inherit the basic func() from the AbstractDecorator directly

    def __init__(self, interface):
        super(ConcreteDecorator2, self).__init__(interface) # calls the superclass's constructor

    def more_func_2(self):                                  # implement an additional functionality
        return 'this is another new functionality'

obj = ConcreteDecorator1(ConcreteObject())
print obj.basic_func()
print obj.more_func_1()

obj = ConcreteDecorator2(ConcreteObject())
print obj.basic_func()
print obj.more_func_2()
