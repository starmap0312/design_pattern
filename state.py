# State Pattern
# object pattern: responsibilities between objects are established at run time via composition
# behavioral pattern: how classes and objects interact and distribute responsibilities
# - create (or identify) a wrapper class that serves as a state machine
# - each state takes one additional parameter: an instance of the wrapper class
# - the wrapper class maintains a "current" state object
# - all client's requests to wrapper class are delegated the current state object
# - state objects are often singletons
# - the difference between state and strategy is in the intent. With strategy, the choice of
#   algorithm is fairly stable. With state, a change in the state of the "context" object
#   causes it to select from its "palette" of strategy

class State(object):
    # a state interface for all state objects

    def insertQuarter(self):
        raise NotImplementedError

    def ejectQuarter(self):
        raise NotImplementedError

    def turnCrank(self):
        raise NotImplementedError

    def dispense(self):
        raise NotImplementedError

class SoldOutState(State):

    def __init__(self, gumballMachine):
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

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "please wait. you already giving a gumball"

    def ejectQuarter(self):
        print 'your already turned the crank'

    def turnCrank(self):
        print 'you turned twice'

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

class NoQuarterState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print 'you inserted a quarter'
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass

class HasQuarterState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print "you can't insert another quarter"

    def ejectQuarter(self):
        print 'quarter returned'
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print 'you turned'
        self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print 'no gumball dispense'

class GumballMachine(object):

    def __init__(self, numberGumballs):
        self.soldState = SoldState(self)
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.count = numberGumballs
        if numberGumballs > 0:
            self.state = self.noQuarterState
        else:
            self.state = self.soldOutState

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def setState(self, state):
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

gumballMachine = GumballMachine(3)
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
