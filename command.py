# Command Pattern
# object pattern: responsibilites between objects are established at run time via composition
# behavioral pattern: how classes and objects interact and distribute responsibilites
# - chain of responsibility, command, mediator, and observer all address how to decouple
#   senders and receivers, but with different trade-offs: command normally specifies
#   a sender-receiver connection with a subclass
# - encapsulate a request as an object, letting you parameterize clients with different
#   requests, queue of request, log the requests, or support undoable operations
# - command decouples the object that invokes the operation (sender) from the one that
#   knows how to handle it (receiver)
# - create a base class with "execute()" method that simply calls the action on the receiver
# - all clients of command objects treat each object as a black box by simply invoking 
#   the object's execute() method whenever the clients needs receivers' services
# - sequences of command objects can be assembled into composite (macro) commands
# - two important aspects of command: interface separation (invoker is isolated from receiver)
#   and time separation (stores a ready-to-go processing request that is to be stated later)

class Command(object):
    # an identical interface, encapsulate a request as a command object
    # there can be different kinds of requests, implemented in subclasses

    def execute(self):
        raise NotImplementedError

class NoCommand(Command):

    def execute(self):
        pass

class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class StereoTurnedCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.turned()

class Invoker(object):
    # as requests are encapsulated as objects, the invokder hence can maintain a queue of requests
    # or log the request history, or undo a request

    def __init__(self):
        self.slots = []
        for i in range(2):
            self.slots.append(NoCommand())

    def setCommand(self, command, slot_id):
        self.slots[slot_id] = command

    def runCommand(self, slot_id):
        self.slots[slot_id].execute()

class Light(object):

    def on(self):
        print 'light on'

class Stereo(object):

    def turned(self):
        print 'stereo turned on'

invoker = Invoker()
light = Light()
lightOnCommand = LightOnCommand(light)
invoker.setCommand(lightOnCommand, 0)
stereo = Stereo()
stereoTurnedCommand = StereoTurnedCommand(stereo)
invoker.setCommand(stereoTurnedCommand, 1)
invoker.runCommand(0)
invoker.runCommand(1)
