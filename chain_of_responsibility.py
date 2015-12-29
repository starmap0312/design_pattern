# Chain of Responsibility
# 1) it decouples the sender of requests from the receivers by encapsulating the receivers
#    inside a "chain" abstraction
#    (therefore, the sender and receivers do not communicate directly, which avoids the
#     coupling of senders with all receivers, making the handle of requests more flexible)
# 2) the sender sends message to the head of a chain of receivers, in which the message
#    is handled and passed on to the next receiver in turns
# 3) each receiver holds a reference to its successor, and the chain is constructed via the 
#    receiver's setter method or the constructor
#    (the number and type of receivers are configured dynamically at run-time)
#
#                                     (IS_A)
#                   (HAS_A)          <------ HandlerExample1
#            Client ......> Handler  <------ HandlerExample2
#                            |   ^   <------ HandlerExample3
#                            ....|
#                           (HAS_A)
#
# - the chaining mechanism uses recursive composition to allow an unlimited number of
#   handlers to be linked
# - the chain serves as a "safety net" to catch requests unhandled
# - when not to use chain of responsibility:
#   a) when the request can be handled by one sinlge handler
#   b) when the client knows which handler needs to take care the request
#

class Handler(object):
    ''' a base class with a reference to the next handler in the chain, a setter method for the
        reference, and an operation that handles the request (implemented in subclasses)
    '''

    def __init__(self):
        # a reference to the next handler object in the chain
        self.next = None

    def setNext(self, handler):
        # a setter method for the reference (an alternative is to use the constructor)
        self.next = handler

    def handle(self, request):
        # a specific operation that handles the request, if the reference points to
        # the next implementation in the chain, it should call the next object's handle
        raise NotImplementedError

class ConcreteHandler1(Handler):

    def handle(self, request):
        if request >= 0 and request < 10:
            print '%s handled request %s' % (self.__class__.__name__, request)
        elif self.next:
            self.next.handle(request)

class ConcreteHandler2(Handler):

    def handle(self, request):
        if request >= 10 and request < 20:
            print '%s handled request %s' % (self.__class__.__name__, request)
        elif self.next:
            self.next.handle(request)

class ConcreteHandler3(Handler):

    def handle(self, request):
        if request >= 20 and request < 30:
            print '%s handled request %s' % (self.__class__.__name__, request)
        elif self.next:
            self.next.handle(request)

# the client constructs a chain of handlers using the handler's setter method
h1 = ConcreteHandler1()
h2 = ConcreteHandler2()
h3 = ConcreteHandler3()
h1.setNext(h2)
h2.setNext(h3)
h1.handle(2)
h1.handle(5)
h1.handle(14)
h1.handle(22)

