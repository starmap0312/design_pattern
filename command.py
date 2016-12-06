# Command Pattern (an OK design pattern)
# - encapsulate a request (receiver's operation) as an object (no longer method level)
#   this lets you parameterize clients with different requests, queue requests or log requests, and
#   support undoable operations
# - object pattern: responsibilites between objects are established at run time via composition
#   behavioral pattern: how classes and objects interact and distribute responsibilites
# - a combination of using adapter, delegation, dependency injection, and dependency inversion
#   patterns
# - 4 major roles of command pattern:
#   a) the receiver object: a service object with operations that actually do the work
#                           all service objects are adapted to command interface
#      ex. class Cook: with cook_steak() and cook_pork() methods
#   b) the command object: knows about how to invokes a receiver's operation (implement a uniform interface)
#      (i.e. knows about some subset of the following: the receiver object, one of its operation,
#       and the parameters of the operation)
#      ex. class Order: with a common execute() method 
#   c) the invoker object: knows about how to use a command object (with optional bookkeeping)
#      ex. class Waiter: with execute_orders() method (can queue, log, or undo orders)
#   d) the client object: constructs and uses the invoker object to run the command objects
#                         by injecting command objects into the invoker object
#      ex. class Restaurant: compose Order objects, inject them to Waiter object, then use the Waiter object
#
#                        (HAS_A)               (HAS_A)
#             Client ----------------> Invoker ------> Command
#               |    constructs & uses                    ^
#       (HAS_A) |                                  (IS_A) |       (HAS_A)
#               |--------------------------------> CommandExample ------> Receiver
#                      constructs & injects                        uses
#
# real example:
#
#                        (HAS_A)            (HAS_A)
#           Restaurant ----------> Waiter ----------> Order
#               |     (constructs & uses)             ^   ^
#               |                               (IS_A)|   |(IS_A)   (HAS_A)
#               |---------------------------> SteakOrder  PorkOrder ------> Cook
#                   (constructs & injects)                          (uses)

class Restaurant(object):
    ''' client '''
    def main(self):
        # receiver object: with methods that do the real tasks
        cook = Cook()

        # command objects: encapsulate receiver's methods into object with a common interface
        order1 = SteakOrder(cook)
        order2 = PorkOrder(cook)

        # invoker: consists of (multiple) command object(s), used by client to execute commands
        waiter = Waiter().with_order(order1).with_order(order2)
        waiter.send_orders()

class Cook(object):
    ''' receiver '''

    def cook_steak(self):      # request/method that does the real task
        print('cooking steak')

    def cook_pork(self):       # request/method that does the real task
        print('cooking pork')

class Order(ABC):
    ''' command interface '''

    @abstractmethod
    def execute(self):
        pass

class SteackOrder(Order):
    ''' command '''

    def __init__(self, cook):
        self.cook = cook

    def execute(self):
        self.cook.cook_steak()

class PorkOrder(Order):
    ''' command '''

    def __init__(self, cook):
        self.cook = cook

    def execute(self):
        self.cook.cook_pork()

class Waiter(self):
    ''' invoker '''

    def __init__(self, orders=None):
        self.orders = orders

    def with_order(self, order):
        orders = list(self.orders)
        orders.append(order)
        return Order(orders)

    def send_orders(self):
        for order in self.orders:
            order.execute()

#
# - two important features:
#   a) interface separation (dependency inversion): the invoker is isolated from the receiver
#      (declare an abstraction, i.e. the Command interface, and the invoker depends on the
#       abstraction, which makes adding a new command implementation easier)
#   b) time separation: stores a sequence of commands that will be used later
#      (declare an extra layer, i.e. the Invokder class, between the client object and
#       the command object, which makes logging or undoing commands possible)
# - encapsulate a receiver's operation as a command object, letting you set up in the invoker
#   for different commands, a queue of commands, the logging of commands, or undoable commands
#   (ex. a queue of commands can be assembled into composite (macro) commands)
# - comparison:
#   observer, mediator, chain of responsibility, and command all address how to decouple
#   senders and receivers but with different intents: 
#   a) observer: the receiver (i.e. the observer) registers itself to a sender (i.e. the subject)
#      the sender notifies the receiver when its state changes
#   b) mediator: the sender registers itself and passes the message to an intermediate class,
#      (i.e. the Mediator), which helps to pass on (notifies) the message to correct receivers
#   c) command: all the receivers are adapted to an uniform interface (i.e. the Command)
#      the sender (i.e. the client) sends requests to an intermediate wrapper class (i.e.
#      the Invoker), which passes on the message to the adapted receivers
#      (without the Command interface, the pattern resembles the mediator pattern)
#      (without the Invoker class, the pattern resembles the adapter pattern)
#   d) chain of responsibility: the sender sends message to a "chain" abstraction
#      the sender does not couple with all receivers but holds a reference to the head of
#      a chain, in which each receiver handles the message and passes it on its successor

class Command(object):
    ''' a uniform interface that serves as an adapter for receivers' operations '''

    def execute(self):
        raise NotImplementedError

class NoCommand(Command):
    ''' an implementation of the command interface: for null object '''

    def execute(self):
        pass

class LightOnCommand(Command):
    ''' an implementation of the command interface for the light-on operation '''

    def __init__(self, light):
        # the command object can be constructed only if the receiver object is specified
        self.light = light

    def execute(self):
        # delegates to the passed-in recevier object
        self.light.on()

class LightOffCommand(Command):
    ''' an implementation of the command interface for the light-off operation '''

    def __init__(self, light):
        # the command object can be constructed only if the receiver object is specified
        self.light = light

    def execute(self):
        # delegates to the passed-in recevier object
        self.light.off()

class StereoOnCommand(Command):
    ''' an implementation of the command interface for the stereo-on operation '''

    def __init__(self, stereo):
        # the command object can be constructed only if the receiver object is specified
        self.stereo = stereo

    def execute(self):
        # delegates to the passed-in recevier object
        self.stereo.on()

class Invoker(object):
    ''' an additional layer that serves as the client of the command objects (service objects)
        and provides a setter method for the injection of the command objects
        with this layer, one can bookkeep (log) or redo the commands 
    '''

    def __init__(self):
        # a list that keeps track of a sequence of commands
        self.slots = [ NoCommand(), NoCommand(), NoCommand() ]

    def setCommand(self, command, slot_id):
        # a setter method for the injection of the command objects
        # the construction of the command objects are separated into external code
        self.slots[slot_id] = command

    def runCommand(self, slot_id):
        # use of the command objects
        self.slots[slot_id].execute()

class Light(object):
    ''' a receiver providing some operations '''

    def on(self):
        print 'light on'

    def off(self):
        print 'light off'

class Stereo(object):
    ''' a receiver providing some operations '''

    def on(self):
        print 'stereo turned on'

# the client: constructs receiver objects, adapt them into command interface, and injects the
# command objects into the invoker, and finally uses the invoker to execute the command objects
light = Light()                               # a receiver object
lightOnCommand = LightOnCommand(light)        # command object: adapter of receiver object's method
lightOffCommand = LightOffCommand(light)      # command object: adapter of receiver object's method
stereo = Stereo()                             # another receiver object
stereoTurnedCommand = StereoOnCommand(stereo) # command object: adapter of receiver object's method
invoker = Invoker()                           # invoker object: used to executes command objects
invoker.setCommand(lightOnCommand, 0)         # client constructs invoker and injects command objects to it
invoker.setCommand(stereoTurnedCommand, 1)
invoker.setCommand(lightOffCommand, 2)
invoker.runCommand(0)                         # client uses invoker to executes command objects
invoker.runCommand(1)
invoker.runCommand(2)
