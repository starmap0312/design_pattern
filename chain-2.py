# Chain of Responsibility
# - avoid coupling sender and receiver by giving more than one object a chance to 
#   handle the request
# - pass the request along the chain until an object handles it
# - encapsulate request receivers inside a "pipeline" abstraction, and client
#   send requests at the entrance to the pipeline
# - the number and type of receivers (request handlers) can be configured dynamically
# - the chaining mechanism uses recursive composition to allow an unlimited number of
#   handlers to be linked
# - simplifies object interconnections: instead of senders and receivers maintaining
#   references to all candidate receivers, each sender need only to keep a single reference
#   to the head of the chain, and each receiver keeps a single reference to its suceccessor
#   receiver in the chain
# - define a "safety net" to catch requests unhandled
# - don't use chain of responsibility when each request is only handled by one handler, or
#   when client knows which handler needs to take care the request
# - sender and receiver do not communicate directly, but through an assembled chain of receivers,
#   this avoids coupling of sender and all the receivers, and make the handle of requests more
#   flexible
# - the handler's base class has a "next" reference, the derived handler class calls back to
#   base class to delegate to its next handler
# - chain of responsibility, mediator, and observer all decouple senders and receivers

class Handler(object):

    def __init__(self):
        self.next = None

    def setNext(self, successor):
        self.next = successor

    def handleRequest(self, request):
        raise NotImplementedError

class ConcreteHandler1(Handler):

    def handleRequest(self, request):
        if request >= 0 and request < 10:
            print '%s handled request %s' % (self.__class__.__name__, request)
        elif self.next is not None:
            self.next.handleRequest(request)

class ConcreteHandler2(Handler):

    def handleRequest(self, request):
        if request >= 10 and request < 20:
            print '%s handled request %s' % (self.__class__.__name__, request)
        elif self.next is not None:
            self.next.handleRequest(request)

class ConcreteHandler3(Handler):

    def handleRequest(self, request):
        if request >= 20 and request < 30:
            print '%s handled request %s' % (self.__class__.__name__, request)
        elif self.next is not None:
            self.next.handleRequest(request)

# client codes
h1 = ConcreteHandler1()
h2 = ConcreteHandler2()
h3 = ConcreteHandler3()
h1.setNext(h2)
h2.setNext(h3)
requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
for request in requests:
    h1.handleRequest(request)

