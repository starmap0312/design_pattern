# Mediator Pattern
# - mediator and observer are competing patterns. Mediator has senders and receivers reference
#   each other indirectly. Observer defines a very decoupled interface that allows for multiple
#   receivers to be configured at run-time
# - observer distributes communication by introducing "observer" and "subject" objects, whereas
#   mediator encapsulates the communication between objects
# - subject notifies all registered observers whenever its state changes
#   a colleague(observer) notifies another colleague(observer) with the help of mediator(subject)
# - it is easier to make reusable observers and subjects than to make reusable mediators
# - observable/subject vs. observer, if subject changes all observers get notified
# - both mediator and facade abstract functionality of existing classes
#   mediator abstracts/centralizes communication between peer(colleague) objects, it often
#   adds value and is known/referenced by peer objects, i.e. it defines multidirectional protocol
#   facade defines a unified/simpler interface of subsystem classes, i.e. it defines a
#   uniderectional protocol
# - sendor(a peer), receiver(another peer), intermediary(mediator)
# - a peer (observer) sends messages to another peer (observer) through intermediary 
#   mediator (subject), so mediator must know all peers in order to handle their interaction

class Mediator(object):
    # mediator interface

    def send(self, message, colleague):
        raise NotImplementedError

# 1. create an intermediary that decouples sendors from receivers
class ConcreteMediator(Mediator):

    def registerColleague1(self, colleague):
        self.colleague1 = colleague

    def registerColleague2(self, colleague):
        self.colleague2 = colleague2

    def send(self, message, colleague):
        if colleague is self.colleague1:
            self.colleague2.notify(message)
        else:
            self.colleague1.notify(message)

class Colleague(object):
    # colleague interface

    def __init__(self, mediator):
        # every colleague has a reference to mediator
        self.mediator = mediator


class ConcreteColleague1(Colleague):

    def send(self, message):
        # a colleague relies on mediator to send the message to another colleague
        self.mediator.send(message, self)

    def notify(self, message):
        print 'Colleague1 object gets message: %s' % message

class ConcreteColleague2(Colleague):

    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print 'Colleague2 object gets message: %s' % message

mediator = ConcreteMediator()
colleague1 = ConcreteColleague1(mediator)
colleague2 = ConcreteColleague2(mediator)
mediator.registerColleague1(colleague1)
mediator.registerColleague2(colleague2)
colleague1.send('How are you?')
colleague2.send('Fine, thanks.')
