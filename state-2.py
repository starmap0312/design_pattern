# State Pattern

# 1. create a context class that serves as a state machine
class Context(object):
    ''' the context class holding the current internal state, defining methods for handling
        client's requests, and defining a callback method for the state object to change its
        current state
    '''

    def __init__(self):
        # 2. hold an array of all the concrete state objects
        self.states = (StateA(), StateB(), StateC())
        # 3. hold an index specifying its current internal state
        self.current = 0

    # 4. client's requests are simply delegated to the current state object, so that no need to
    #    define a bunch of conditional statements
    def on(self):
        self.states[self.current].on(self)

    def off(self):
        self.states[self.current].off(self)

    def ack(self):
        self.states[self.current].ack(self)

    def changeState(self, index):
        # a callback method for the state object to change its current state
        self.current = index

# 5. create the state base class that makes the concrete states interchangeable
class State(object):
    ''' the state base class defining the default behavior and default state transition '''

    # 6. the state base class specifies default behavior for all messages
    def on(self, context):
        # the default is to print "error" if the transition is not defined
        print 'error'

    def off(self, context):
        print 'error'

    def ack(self, context):
        print 'error'

class StateA(State):
    ''' a state subclass '''

    # 7. the state derived classes override the messages
    def on(self, context):
        print 'A + on = C'
        # 8. the derived classes call back to the context object to change its current state
        context.changeState(2)

    def off(self, context):
        print 'A + off = B'
        context.changeState(1)

    def ack(self, context):
        print 'A + ack = A'
        context.changeState(0)

class StateB(State):
    ''' a state subclass '''

    def on(self, context):
        print 'B + on = A'
        context.changeState(0)

    def off(self, context):
        print 'B + off = C'
        context.changeState(2)

class StateC(State):
    ''' a state subclass '''

    def on(self, context):
        print 'C + on = B'
        context.changeState(1)

# the client that constructs and uses the context object
context = Context()
msgs = (2, 1, 2, 1, 0, 2, 0, 0)
for i in range(len(msgs)):
    if msgs[i] == 0:
        context.on()
    elif msgs[i] == 1:
        context.off()
    elif msgs[i] == 2:
        context.ack()
