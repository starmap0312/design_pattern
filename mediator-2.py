# Mediator Pattern
# - mediator and observer are competing patterns
#   a) observer distributes communication by introducing "observer" and "subject" objects
#      the subject object notifies all registered observers whenever its state changes
#   b) mediator encapsulates the communication between objects in a mediator object
#      the colleague object notifies another colleague object with the help of the mediator object
#   c) it is easier to make reusable observers and subjects than to make reusable mediators
# - both mediator and facade abstract functionality of existing classes
#   a) mediator abstracts (centralizes) communication between peer (colleague) objects
#      it adds value and is referenced by peer objects (i.e. defining multidirectional protocol)
#   b) facade defines a unified (simpler) interface of subsystem classes (i.e. defining a
#      uniderectional protocol)

class Mediator(object):
    ''' the mediator interface, providing an exchangeMsg() method for the colleague objects
        to call, and also register() method for the colleague objects to register themselves
    '''

    def exchangeMsg(self, message, colleague):
        raise NotImplementedError

    def registerColleague1(self, colleague):
        self.colleague1 = colleague

    def registerColleague2(self, colleague):
        self.colleague2 = colleague2

# 1. create an intermediary that decouples sendors from receivers
class ConcreteMediator(Mediator):
    ''' an implementation of the mediator defining how the colleague objects exchange messages ''' 

    def exchangeMsg(self, message, colleague):
        # the concrete implementation of how to exchange messages between colleague objects
        if colleague is self.colleague1:
            self.colleague2.notify(message)
        else:
            self.colleague1.notify(message)

class Colleague(object):
    ''' the colleague interface providing a notify() method for the mediator object to call '''

    def __init__(self, mediator):
        # a colleague object can be constructed only if the mediator object is specified
        self.mediator = mediator

    def notify(self, message):
        raise NotImplementedError

class ConcreteColleague1(Colleague):
    ''' an implementation of the colleague '''

    def send(self, message):
        # a colleague relies on mediator to send the message to another colleague
        self.mediator.exchangeMsg(message, self)

    def notify(self, message):
        print 'Colleague1 object gets message: %s' % message

class ConcreteColleague2(Colleague):
    ''' an implementation of the colleague '''

    def send(self, message):
        self.mediator.exchangeMsg(message, self)

    def notify(self, message):
        print 'Colleague2 object gets message: %s' % message

mediator = ConcreteMediator()
colleague1 = ConcreteColleague1(mediator)
colleague2 = ConcreteColleague2(mediator)
mediator.registerColleague1(colleague1)
mediator.registerColleague2(colleague2)
colleague1.send('How are you?')
colleague2.send('Fine, thanks.')
