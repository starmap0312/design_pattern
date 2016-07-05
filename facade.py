# Facade Pattern (a BAD design pattern)
# - it is bad because we need objects themselves only, not facades for them
# - it is procedural in its spirit (a facade is nothing more than a collection of procedures)
# creational pattern
# - provides a simplified interface to a larger body of code, ex. a class library, and hides
#   the complexity of larger systems
# - the client is coupled to one single facade, instead of all the subsystems or compponents
# - abstract factory can be used as an alternative to facade to hide platform-specific classes
# - adapter pattern vs. facade pattern:
#   (both are wrappers but different in their intent)
#   a) adapter makes two existing interfaces work together
#   b) facade defines an entirely new interface (a simplified interface)
#   c) facade usually wraps multiple objects and adapter wraps one, but facade could also
#      front-end a single complex object and adapter could wrap several legacy objects
# - mediator pattern vs. facade pattern:
#   a) facade defines a simpler interface to a subsystem, it doesn't add new functionality and 
#      is not known by the subsystem classes
#   b) mediator abstracts (centralizes) arbitrary communication between colleague objects
#      it routinely "adds value" and is known or referenced by the colleague objects
#
#                                   (HAS_A)
#                    (HAS_A)        ......> Service1
#             Client ......> Facade ......> Service2
#                     uses          ......> Service3
#

class CPU(object):
    ''' a subsystem '''

    def freeze(self):
        print 'freeze cpu'

    def jump(self, position):
        print 'jump to cpu position %s' % position

    def execute(self):
        print 'execute cpu'

class Memory(object):
    ''' a subsystem '''

    def load(self):
        print 'load memory'

class HardDrive(object):
    ''' a subsystem '''

    def read(self, size):
        print 'read size %s' % size

class ComputerFacade(object):
    ''' a simplified interface that provides methods as an entry point to the subsystems '''

    def __init__(self):
        self.cpu = CPU()
        self.ram = Memory()
        self.hd = HardDrive()

    def start(self):
        # the client can use the subsystems through this method
        self.cpu.freeze()
        self.ram.load()
        self.cpu.jump(10)
        self.cpu.execute()

computer = ComputerFacade()
computer.start()
