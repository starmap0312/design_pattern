# State Pattern
# - the structure of bridge and state patterns are identical, but they are used to solve
#   different problems. State allows an object's
#   behavior to change along with its state, while bridge's intent is to decouple an
#   abstraction from its implementation so that the two can vary independently, i.e. 
#   handle/body idiom
# - the implementation of state pattern builds on strategy pattern

# 1. create a "wrapper" class that models the state machine
class Wrapper(object):

    def __init__(self):
        # 2. the wrapper class contains an array of state concrete objects
        self.states = (A(), B(), C())
        # 3. the wrapper class contains index to its "current" state
        self.current = 0

    # 4. client's requests are simply delegated to the current state and "self" is passed
    def on(self):
        self.states[self.current].on(self)

    def off(self):
        self.states[self.current].off(self)

    def ack(self):
        self.states[self.current].ack(self)

    def changeState(self, index):
        self.current = index

# 5. create the state base class that makes the concrete states interchangeable
class State(object):

    # 6. the state base class specifies default behavior for all messages
    def on(self, wrapper):
        # the default is to print "error" if the transition is not defined
        print 'error'

    def off(self, wrapper):
        print 'error'

    def ack(self, wrapper):
        print 'error'

class A(State):

    # 7. the state derived classes override the messages they need to
    def on(self, wrapper):
        print 'A + on = C'
        # 8. the derived classes call back to the wrapper class to change its current
        wrapper.changeState(2)

    def off(self, wrapper):
        print 'A + off = B'
        wrapper.changeState(1)

    def ack(self, wrapper):
        print 'A + ack = A'
        wrapper.changeState(0)

class B(State):

    def on(self, wrapper):
        print 'B + on = A'
        wrapper.changeState(0)

    def off(self, wrapper):
        print 'B + off = C'
        wrapper.changeState(2)

class C(State):

    def on(self, wrapper):
        print 'C + on = B'
        wrapper.changeState(1)

# client codes
wrapper = Wrapper()
msgs = (2, 1, 2, 1, 0, 2, 0, 0)
for i in range(len(msgs)):
    if msgs[i] == 0:
        wrapper.on()
    elif msgs[i] == 1:
        wrapper.off()
    elif msgs[i] == 2:
        wrapper.ack()
