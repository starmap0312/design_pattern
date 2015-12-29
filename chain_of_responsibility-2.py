# Chain of Responsibility
#
# example: the chain is constructed via the receiver's constructor

class Handler(object):
    ''' a base class with a reference to the next handler in the chain, and an operation that 
        handles the request (implemented in subclasses)
    '''

    def __init__(self, handler):
        # a reference to the next handler object in the chain
        # the handler can be constructed only if its successor is specified
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

# the client constructs the chain of handlers using the handler's constructor
handler = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3(None)))
handler.handle(2)
handler.handle(5)
handler.handle(14)
handler.handle(22)

