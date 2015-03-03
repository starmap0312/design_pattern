# Facade Pattern
# creational pattern
# - provides a simplified interface to a larger body of code, hides the complexity of larger
#   systems both facade and abstract factory can be used to hide platform-specific classes
# - the client is coupled to one single facade, instead of all the subsystems or components
# - adapter makes two existing interfaces work together, as opposed to facade which defines
#   an entirely new one
# - mediator is similar to facade in that it abstracts functionality of existing classes
#   facade defines a simpler interface to a subsystem, it doesn't add new functionality, and 
#   it is not known by the subsystem classes. In contrast, mediator abstracts/centralizes
#   arbitrary communication between colleague objects. It routinely "adds value", and it is
#   known/referenced by the colleague objects
# - abstract factory can be used as an alternative to facade to hide platform-specific classes
# - Adapter and facade are both wrappers, but they are different kinds of wrappers.
#   the intent of facade is to produce a simpler interface, while the intent of adapter is
#   to design to an existing interface
# - while facade usually wraps multiple objects and adapter wraps one, facade could also front-end
#   a single complex object and adapter could wrap several legacy objects

class CPU(object):

    def freeze(self):
        print 'freeze cpu'

    def jump(self, position):
        print 'jump to cpu position %s' % position

    def execute(self):
        print 'execute cpu'

class Memory(object):

    def load(self):
        print 'load memory'

class HardDrive(object):

    def read(self, size):
        print 'read size %s' % size

class ComputerFacade(object):
    # a simplified interface with start method as entry point

    def __init__(self):
        self.cpu = CPU()
        self.ram = Memory()
        self.hd = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.ram.load()
        self.cpu.jump(10)
        self.cpu.execute()

computer = ComputerFacade()
computer.start()
