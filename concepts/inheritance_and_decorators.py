# 1) types of decorators:
#    Type 1) simple decoration
#      decorating an exsiting functionality of an object
#    Type 2) delegation and extension (works like extension/inheritance)
#      when you don't want to inherit all the interface methods of a class
#      you can use delegation and add one additional functionality to an object
#
# 2) how to a family of decorators
#    define an abstract decorator, which is inherited by a set of decorator subclasses
#      each of which add one additional functionality to the object 
#

# example 1: simple implementation 
from abc import ABCMeta, abstractmethod

class Interface(object):      # a type: ex. class Animal
    __metaclass__ = ABCMeta

    @abstractmethod
    def basic_func(self):
        pass

class SimpleImpl(Interface): # a concrete object of some type: ex. class Duck

    def basic_func(self):    # a common behavior of some type: ex. def move(self):
        return 'this is a basic functionality of the concrete object'

# good practice: write the SimpleImpl inside the Interface class and name it Simple/Base/Default
#   use Interface.Simple / Interface.Base / Interface.Default when needed
#   this reduces the number of class files and helps the code readability

class Interface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def basic_func(self):
        pass

    class Simple(object):   # a simple concrete object of some type: ex. class Animal.Simple
        # base class

        def basic_func(self):
            return 'this is a basic functionality of the concrete object'

obj = Interface.Simple()
print obj.basic_func()


# example 2: (Type 1) simple decoration

class Decorator(Interface):            # decorates behavior of a concrete object of some type: ex. class Walking

    def __init__(self, interface):
        self.interface = interface

    def basic_func(self):              # ex. decorates the object's move(self) by walking with legs
        return self.interface.basic_func() + ', added something new to the basic functionality'

obj = Decorator(SimpleImpl())          # ex. Walking(Animal.Simple()).move() will move with legs
print obj.basic_func()


# example 3: use inheritance to add one additional funcationality to an object

class SubclassObject(SimpleImpl):
    # subclass

    def more_func(self):               # a bad practice if we override a concrete class by inheritance 
        return 'this is a new functionality'

# pros:
#   code reuse and less complexity 
# cons:
#   less flexible, as we must inherit all the interface methods
#   tight coupling between derived class and base class (and between derived classes)
#   implementation inheritance: a procedural technique for code reuse and turns objects into containers with data and procedures
obj = SubclassObject()
print obj.basic_func()
print obj.more_func()

# example 4: use wrapper & delegation to add one additional funcationality to an object

class Wrapper(Interface):              # decorate a type by adding an additional behavior: ex. class Jumpping
    # wrapper class

    def __init__(self, interface):
        self.interface = interface

    def basic_func(self):              # a delegating method 
        return self.interface.basic_func()

    def more_func(self):               # add an additional behavior to the object: ex. def jump(self)
        return 'this is a new functionality'

obj = Wrapper(SimpleImpl())        # ex. animal = Jumpping(Animal.Simple())
print obj.basic_func()                       # ex. animal.move()
print obj.more_func()                        # ex. animal.jump()
# pros:
#   decouples client form delegate
#     client is programmed to interface, not to implementation

# good practice: write the Wrapper inside the Inferface class
#   better code organization and improved readability
class Interface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def basic_func(self):
        pass

    class Wrapper(object):         # ex. class Animal.Jumpping, i.e. Animal.Jumpping(Animal.Simple())

        def __init__(self, interface):
            self.interface = interface

        def basic_func(self):
            return self.interface.basic_func()   # preserves the object's basic functionality

        def more_func(self):
            return 'this is a new functionality'

obj = Interface.Wrapper(SimpleImpl())
print obj.basic_func()
print obj.more_func()


# example 5: a famility of decorators, each of which adds one additional functionality to the object

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

# example 6: inheritence
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
