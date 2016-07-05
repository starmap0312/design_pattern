# State Pattern (a BAD design pattern)
# - it is bad because it usually implies object mutability
# object pattern: responsibilities between objects are established at run time via composition
# behavioral pattern: how classes and objects interact and distribute responsibilities
# - used when a service object needs to provide different behaviors based on various conditions:
#   a) create a state interface and define the different behaviors in its subclasses
#   b) create a context class (wrapper) holding a current state object and defining a callback
#      method for the transition of the current state object
#   c) similar to strategy pattern but different in that the current state object in strategy
#      pattern rarely changes and that the wrapper class in strategy pattern may hold more than
#      one state types (i.e. strategy or algorithm)
# - state pattern features:
# a) allow an object to change its behavior at run-time (i.e. a context object varies its 
#    behavior based on its internal state)
# b) all client's requests to the context object are delegated to the state objects
#    (i.e. the responsibility of handling client's requests is separated into the state class)
# c) without the state pattern, many conditional statements are needed in the context class, 
#    impairing the code maintainability
#    (i.e. adding a new state requires constantly changing the conditional statements)
# d) each state object holds a reference to the context object, and the context class provides
#    a callback method for the state object to change its current state
#
#                  (HAS_A)                  (HAS_A)
#           Client .......> Context <....................> State
#                                    uses, state transits  ^   ^
#                                                          |   |
#                                                   (IS_A) |   | (IS_A)
#                                                      StateA StateB
#
# - strategy pattern vs. state pattern:
#   (the state pattern builds upon strategy pattern, and they are different in their intents)
#   a) strategy: the choice of strategy (algorithm) is fairly stable
#   b) state: the state of the context object constantly changes
# - bridge pattern vs. state pattern:
#   (the two have an identical structure, but are different in their intents)
#   a) bridge: decouple an abstraction from its implementation so that the two can vary
#      independently (i.e. handle & body idiom)
#   b) state: allow an object's behavior to change along with its state
# - state objects are often defined as singletons
# - one can use a state transition diagram to show the state transitions

class State(object):
    ''' the state interface with state operation methods, including state transition '''

    def insertQuarter(self):
        raise NotImplementedError

    def ejectQuarter(self):
        raise NotImplementedError

    def turnCrank(self):
        raise NotImplementedError

    def dispense(self):
        raise NotImplementedError

class SoldOutState(State):
    ''' an implementation of the state, holding a reference to the context object
        (via dependency injection)
    '''

    def __init__(self, gumballMachine):
        # a state object can be constructed only if the context object is specified
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print 'it is sold out'

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass

class SoldState(State):
    ''' an implementation of the state, holding a reference to the context object
        (via dependency injection)
    '''

    def __init__(self, gumballMachine):
        # a state object can be constructed only if the context object is specified
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "please wait. you already giving a gumball"

    def ejectQuarter(self):
        print 'your already turned the crank'

    def turnCrank(self):
        print 'you turned twice'

    def dispense(self):
        # use the context object to change its current state
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

class NoQuarterState(State):
    ''' an implementation of the state, holding a reference to the context object
        (via dependency injection)
    '''

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        # use the context object to change its current state
        print 'you inserted a quarter'
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass

class HasQuarterState(State):
    ''' an implementation of the state, holding a reference to the context object
        (via dependency injection)
    '''

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "you can't insert another quarter"

    def ejectQuarter(self):
        # use the context object to change its current state
        print 'quarter returned'
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        # use the context object to change its current state
        print 'you turned'
        self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print 'no gumball dispense'

class GumballMachine(object):
    ''' the context class holding a current state object, defining methods to handle the
        client's requests, and defining a callback method for the state object to change its
        current state
    '''

    def __init__(self, numberGumballs):
        self.soldState = SoldState(self)
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.count = numberGumballs
        # initialize the current state
        self.state = self.noQuarterState if numberGumballs > 0 else self.soldOutState

    def insertQuarter(self):
        # delegate the client's request to the current state object
        self.state.insertQuarter()

    def ejectQuarter(self):
        # delegate the client's request to the current state object
        self.state.ejectQuarter()

    def turnCrank(self):
        # delegate the client's request to the current state object
        self.state.turnCrank()
        self.state.dispense()

    def setState(self, state):
        # a callback method for the state object
        self.state = state

    def releaseBall(self):
        print 'A gumball comes rolling out the slot'
        if self.count != 0:
            self.count -= 1

    def getCount(self):
        return self.count

    def getNoQuarterState(self):
        return self.noQuarterState

    def getHasQuarterState(self):
        return self.hasQuarterState

    def getSoldState(self):
        return self.soldState

    def getSoldOutState(self):
        return self.soldOutState

# the client constructs and uses the context object
gumballMachine = GumballMachine(3)
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
