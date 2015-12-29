# State Pattern

class Chain(object):
    ''' the context class '''

    def __init__(self):
        # the context class maintains a "current" state object
        self.state = StateOff()

    def setState(self, state):
        # a callback method for the state object to change its current state
        self.state = state

    def pull(self):
        # the client's request is delegated to the current state object
        self.state.pull(self)

class State(object):
    ''' the state base class, defining the default behavior and state transition '''

    def pull(self, context):
        # the default behavior and the default transition of the context object
        context.setState(StateOff())
        print 'turning off'

class StateOff(State):
    ''' a state subclass '''

    def pull(self, context):
        # override the default behavior and default state transition
        context.setState(StateLow())
        print 'low speed'

class StateLow(State):
    ''' a state subclass '''

    def pull(self, context):
        # override the default behavior and default state transition
        context.setState(StateMedium())
        print 'medium speed'

class StateMedium(State):
    ''' a state subclass '''

    def pull(self, context):
        # override the default behavior and default state transition
        context.setState(StateHigh())
        print 'high speed'

class StateHigh(State):
    ''' a state subclass '''

# the client constructs and uses the context object
from sys import stdin
chain = Chain()
print 'Press Enter for next state and Control-C for exit'
while True:
    stdin.readline()
    chain.pull()
