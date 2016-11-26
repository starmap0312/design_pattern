# two types of decorations:
#   Type 1) decorating an exsiting functionality of an object
#   Type 2) adding one additional functionality to an object (works as inheritance)
#
# how to define a family of decorators, each of which add one additional functionality to the object 
#   define an abstract decorator, which is inherited by a set of decorator subclasses
#

from abc import ABCMeta, abstractmethod

class Interface(object):      # a type: ex. class Animal
    __metaclass__ = ABCMeta

    @abstractmethod
    def basic_func(self):
        pass

class SimpleImpl(Interface): # a concrete object of some type: ex. class Duck

    def basic_func(self):    # a common behavior of some type: ex. def move(self):
        return 'this is a basic functionality of the concrete object'

# a good practice is to write the SimpleImpl inside the Interface class: name it Simple/Base/Default
# use Interface.Simple / Interface.Base / Interface.Default when needed
# this reduces the number of class files and helps the code readability

class Interface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def basic_func(self):
        pass

    class Simple(object):   # a simple concrete object of some type: ex. class Animal.Simple

        def basic_func(self):
            return 'this is a basic functionality of the concrete object'

obj = Interface.Simple()
print obj.basic_func()


# example 1: (Type 1) simple decorator, decorating the object's basic funcationality

class Decorator(Interface):            # decorates behavior of a concrete object of some type: ex. class Walking

    def __init__(self, interface):
        self.interface = interface

    def basic_func(self):              # ex. decorates the object's move(self) by walking with legs
        return self.interface.basic_func() + ', added something new to the basic functionality'

obj = Decorator(SimpleImpl())          # ex. Walking(Animal.Simple()).move() will move with legs
print obj.basic_func()


# example 2: (bad design) inheritance that adds one additional funcationality to an object

class SubclassObject(SimpleImpl):

    def more_func(self):               # a bad practice if we override a concrete class by inheritance 
        return 'this is a new functionality'

# this is a bad design, as it inherits (may override) an concrete class
# it creates tight coupling between SubclassObject (derived class) and SimpleImpl (base class)
# implementation inheritance is bad:
#   a procedural technique for code reuse and turns objects into containers with data and procedures
obj = SubclassObject()
print obj.basic_func()
print obj.more_func()


# example 2: (good design) decorator that adds one additional funcationality to an object

class MoreFuncDecorator(Interface):         # decorate a type by adding an additional behavior: ex. class Jumpping

    def __init__(self, interface):
        self.interface = interface

    def basic_func(self):                   # preserve the object's basic functionality: ex. def move(self)
        return self.interface.basic_func()

    def more_func(self):                    # add an additional behavior to the object: ex. def jump(self)
        return 'this is a new functionality'

# we program to interface instead, not to implementation
# it creates loose coupling between MoreFuncDecorator (decorator class) and SimpleImpl (base class)
obj = MoreFuncDecorator(SimpleImpl())        # ex. animal = Jumpping(Animal.Simple())
print obj.basic_func()                       # ex. animal.move()
print obj.more_func()                        # ex. animal.jump()

# as we program to interface, a good practice is to write the MoreFuncDecorator inside the Inferface class
#   because they are closely related/coupled and it also helps code readability
#   then use Interface.MoreFuncDecorator when needed 
class Interface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def basic_func(self):
        pass

    class MoreFuncDecorator(object):         # ex. class Animal.Jumpping, i.e. Animal.Jumpping(Animal.Simple())

        def __init__(self, interface):
            self.interface = interface

        def basic_func(self):
            return self.interface.basic_func()   # preserves the object's basic functionality

        def more_func(self):
            return 'this is a new functionality'

obj = Interface.MoreFuncDecorator(SimpleImpl())
print obj.basic_func()
print obj.more_func()


# example 4: (Type 2) a famility of decorators, each of which adds one additional functionality to the object

class AbstractDecorator(Interface):          # declare as abstract class in Java: for code reusibility
                                             # ex. class AnimalBehavior
    def __init__(self, interface):
        self.interface = interface

    def basic_func(self):                    # ex. def move(self)
        return self.interface.basic_func()

class ConcreteDecorator1(AbstractDecorator): # inherit the basic func() from the AbstractDecorator directly
                                             # ex. class Jumpping(AnimalBehavior)
    def __init__(self, interface):
        super(ConcreteDecorator1, self).__init__(interface) # calls the superclass's constructor

    def more_func_1(self):                   # implement an additional functionality: ex. def jump(self)
        return 'this is a new functionality'


class ConcreteDecorator2(AbstractDecorator): # inherit the basic func() from the AbstractDecorator directly
                                             # ex. class Swimming(AnimalBehavior)
    def __init__(self, interface):
        super(ConcreteDecorator2, self).__init__(interface) # calls the superclass's constructor

    def more_func_2(self):                   # implement an additional functionality: ex. def swim(self)
        return 'this is another new functionality'

obj = ConcreteDecorator1(SimpleImpl())       # ex. animal = Jumpping(Animal.Simple())
print obj.basic_func()                       # ex. animal.move()
print obj.more_func_1()                      # ex. animal.jump()

obj = ConcreteDecorator2(SimpleImpl())       # ex. animal = Swimming(Animal.Simple())
print obj.basic_func()                       # ex. animal.move()
print obj.more_func_2()                      # ex. animal.swim()

# inheritence/subclassing itself is not evil, it enables polymorphism
#   it derives a characteristic from a base type
#   ex. MallardDuck (subclass) is a subtype of Duck (superclass)
#       Duck should be able to quack()
#       MallardDuck should be able to quack() and fly()

class Duck(object):          # all ducks can quack()
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self):
        pass

class MallardDuck(Duck):     # a subtype of duck (MallardDuck) can also fly()
    __metaclass__ = ABCMeta

    @abstractmethod
    def fly(self):
        pass
