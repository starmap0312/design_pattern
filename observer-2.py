# Observer Pattern
# - subject: core abstraction (independent or common or engine), observer: variable abstraction
#   (dependent or optional or user interface)
# - each observer can call back to subject if needed
# - observer defines a one-to-many relationship so that when one object (subject) changes
#   state, the others (observers) get notified and updated automatically
# - subject is only coupled to observer abstraction class (base/interface), client configures 
#   the number and type of observers (dynamically, at run time)
# - subject can "push" information at observers, or observers can "pull" information they need
#   from subject
# - observer and mediator address how you can decouple senders and receivers, but with different
#   trade-offs: Mediator has senders and receivers reference each other indirectly. Bbserver
#   defines a very decoupled interface that allows for multiple receivers to be configured
#   at run time

class Subject(object):

    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def setState(self, state):
        self.state = state
        self.notify()

class Observer(object):

    def update(self):
        raise NotImplementedError

class ConcreteObserver(Observer):

    def __init__(self, subject):
        self.subject = subject

    def update(self):
        print "Observer %s get updated subject's state: %s" % (self, self.subject.state)

subject = Subject()
subject.register(ConcreteObserver(subject))
subject.register(ConcreteObserver(subject))
subject.register(ConcreteObserver(subject))
subject.setState('new state')
