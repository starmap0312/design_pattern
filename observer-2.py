# Observer Pattern
# - subject is only coupled to observer abstraction class (base/interface), and the number 
#   and type of observers are determined dynamically, at run time
# - alternatives:
#   by maintaining a reference of the subject interface:
#   a) the observer can call back to the subject
#   b) the observers can "pull" information from subject
# - both observer and mediator address how to decouple senders and receivers, but with different
#   trade-offs:
#   a) both defines a decoupled interface (Observalbe & Mediator) that allows for multiple
#      receivers to be configured at run-time
#   b) the colleague objects of mediator pattern exchange messages with each other indirectly,
#      using a exchangeMsg() method defined in Mediator class
#   c) the observer and colleague objects in both patterns provide a notify() method for the
#      subject or mediator objects to call
#   d) the observer object gets notified by the subject object when the state of the subject
#      object has changed
#   e) the colleague object get notified by the mediator object when the other colleague object
#      send message to it via the mediator object
#
#   observer pattern:
#                                (HAS_A)
#       Subject Interface <.................> Observer Interface
#               ^          notify & register        ^
#        (IS_A) |                                   | (IS_A)
#        SubjectExample                        ObserverExample
#
#       (when the observer object is constructed, the subject object should be specified)
#
#   mediator pattern:
#
#                                                                    --------- ColleagueExample1
#                                (HAS_A)                             | (IS_A)
#                           <...............>                     <--- 
#        Mediator Interface <...............> Colleague Interface <---
#                ^           send & register                         | (IS_A)
#         (IS_A) |           & send                                  --------- ColleagueExample2
#          MediatorExample
#
#       (when the colleague object is constructed, the mediator object should be specified)
#       (the mediator object implements how two colleague objects communicate with each other)
#

class Subject(object):
    ''' the subject interface couples to the observer interface, not implementation '''

    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify(self):
        # push information to observers
        for observer in self.observers:
            observer.update()

    def setState(self, state):
        self.state = state
        self.notify()

class Observer(object):
    ''' the observer interface '''

    def update(self):
        raise NotImplementedError

class ConcreteObserver(Observer):

    def __init__(self, subject):
        self.subject = subject

    def update(self):
        print "Observer %s get updated subject's state: %s" % (self, self.subject.state)

# client code that construct the subject and observer objects and set up the registeration
subject = Subject()
observer1 = ConcreteObserver(subject)
observer2 = ConcreteObserver(subject)
observer3 = ConcreteObserver(subject)
subject.register(observer1)
subject.register(observer2)
subject.register(observer3)
subject.setState('new state')
