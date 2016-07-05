# Memento Pattern (a BAD design pattern)
# - it is bad because it implies that objects are mutable
# keeps the saved state external and provides recovery capability
#
# bad design pattern: this idea implies that objects are mutable

class Originator(object):
    # can get current state for saving in memento and can restore from memento's saved state

    def set(self, state):
        print 'Originator: setting state to %s' % state
        self.state = state
 
    def getState(self):
        print "Get originator's state"
        return self.state 

    def restoreFromMemento(self, memento):
        self.state = memento.getSavedState()
        print 'Originator: state after restoring from Memento: %s' % self.state

class Memento(object):

    def __init__(self, stateToSave):
        self.state = stateToSave

    def getSavedState(self):
        return self.state

originator = Originator()
originator.set('State1')
originator.set('State2')
memento = Memento(originator.getState())
originator.set('State3')
originator.set('State4')
originator.restoreFromMemento(memento)
