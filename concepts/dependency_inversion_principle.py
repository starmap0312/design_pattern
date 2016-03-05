# Dependency Inversion Principle
# - a way to decouple classes (objects): inverts the way people think of dependency
#   conventional:
#                       (HAS_A)
#   high-level objects ........> low-level objects
#
#   dependency inversion principle: (i.e. program to an interface, not an implementation)
#
#           .....> abstraction class <----
#   (HAS_A) |                            | (IS_A)
#           |                            |
#   high-level objects           low-level objects
#
#   a) high-level modules do not depend on low-level modules
#      both should depend on the same "abstraction"
#   b) abstractions do not depend on details
#      details should depend on abstractions
#
# - classical examples:
#   1) dependency injection pattern
#      the construction and use of a service object are separated in Injector and Client
#      classes respectively (add an abstraction class: Service)
#
#                         (HAS_A)             (IS_A)                  (HAS_A)
#                Client  ........> "Service" <------- ServiceExample <........ Injector
#                   ^       uses  "abstraction"                      constructs    |
#                   |..............................................................| (HAS_A)
#                                               injects

# dependency injection pattern
class Service(object):
    ''' an abstraction class '''

    def getName(self):
        raise NotImplementedError

class ServiceExample(Service):
    ''' an implementation of the abstraction class '''

    def getName(self):
        return "ServiceExample"

class Client(object):
    ''' the client class that uses the implementation but depends on its abstraction class ''' 

    def __init__(self, service):
        # the client simply accepts a reference to the implemention and has no knowledge of
        # how it is constructed
        self.service = service

    def greet(self):
        # use of the implementation
        return "Hello " + self.service.getName()

class Injector(object):
    ''' another class that takes out the responsibility of constructing the implementation '''

    def __init__(self):
        self.service = ServiceExample()
        self.client = Client(self.service)

injector = Injector()
print injector.client.greet()

#  conventional desgin (without dependency inversion principle)

class ConventionalClient(object):
    ''' the client constructs and uses the service object all by itself
        the client directly depends on the service object (downside: any changes to the 
        ServiceExample may affect the ConventionalClient)
    '''

    def __init__(self):
        self.service = ServiceExample()

    def greet(self):
        return "Hello " + self.service.getName()

client = ConventionalClient()
print client.greet()

#   2) adapter pattern:
#   - allows the interface of an existing class to be used from another interface, making
#     existing classes work together without modifying their source code
#   - the adapter bridges between the existing adaptee interface and the target interface
#
#            Target Interface
#                   ^
#            (IS_A) |     (HAS_A)             (IS_A) 
#                Adapter ........> "Adaptee" <------- AdapteeExample
#                                "abstraction"
#
#     (Adapter & AdapteeExample both depend on an abstraction, making them "loosely coupled")
#

class Duck(object):
    ''' the target interface '''

    def quack(self):
        raise NotImplementedError

class Turkey(object):
    ''' an abstraction class of the adaptee, the adaptee interface '''

    def gobble(self):
        raise NotImplementedError

class WildTurkey(Turkey):
    ''' an implementation of the abstraction class '''

    def gobble(self):
        return "WildTurkey gobbles"

class TurkeyToDuckAdapter(Duck):
    ''' an adapter class that depends on the abstraction class '''

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def quack(self):
        return self.adaptee.gobble() + " (adapted to quacks)"

turkey = WildTurkey()
duck = TurkeyToDuckAdapter(turkey)
print duck.quack()

#  conventional desgin (without dependency inversion principle)

class ConventionalAdapter(Duck):
    ''' the adapter directly depends on the adaptee object (downside: any changes to the 
        WildTurkey may affect the ConventionalAdapter)
    '''

    def __init__(self):
        self.adaptee = WildTurkey()

    def quack(self):
        return self.adaptee.gobble() + " (adapted to quacks)"

duck = ConventionalAdapter()
print duck.quack()

# - comparison of dependency injection pattern and adapter patter
#   both apply the dependency inversion principle, creating an abstraction class
#     adapter: the Adaptee class
#     dependency injection: the Service class
#   they are different in their purposes:
#     adapter: the Adapter class implements an existing interface (the Target)
#     dependency injection: the Client class delegates the construction of the Service
#       implementaion to another class (the Injector class)
