# State Pattern

class Chain(object):
    # the wrapper class

    def __init__(self):
        # the wrapper class maintains a "current" state object
        self.current = Off()

    def setState(self, state):
        # change the current state in the wrapper
        self.current = state

    def pull(self):
        # all client's requests are simply delegated to the current state object and
        # the wrapper object's self is passed
        self.current.pull(self)

class State(object):
    # state base class

    def pull(self, wrapper):
        # state base class specifies default behavior
        wrapper.setState(Off())
        print 'turning off'

class Off(State):
    # state derived class

    def pull(self, wrapper):
        # state derived class overrides the behaviro
        wrapper.setState(Low())
        print 'low speed'

class Low(State):

    def pull(self, wrapper):
        wrapper.setState(Medium())
        print 'medium speed'

class Medium(State):

    def pull(self, wrapper):
        wrapper.setState(High())
        print 'high speed'

class High(State):
    pass

from sys import stdin
chain = Chain()
print 'Press Enter for next state and Control-C for exit'
while True:
    stdin.readline()
    chain.pull()
