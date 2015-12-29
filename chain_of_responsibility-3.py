# Chain of Responsibility

class Handler(object):
    ''' a base class with a reference to the next handler in the chain, a setter method for
        the reference, and an operation to be implemented in subclasses
    '''

    (ERR, INFO, DEBUG) = (3, 5, 7)

    def __init__(self, mask):
        self.mask = mask
        self.next = None # a reference to the next handler

    def setNext(self, handler):
        self.next = handler

    def handle(self, msg, priority):
        # a template method for handling the message, with the writeMessage() method to be
        # implemented in subclasses
        if priority <= self.mask:
            self.writeMessage(msg)
        if self.next is not None:
            self.next.handle(msg, priority)

    def writeMessage(self, msg):
        # specific implmentations are defined in subclasses
        raise NotImplementedError

class DebugHandler(Handler):
    ''' an implementation of the handler '''

    def writeMessage(self, msg):
        print 'Writing to debug: %s' % msg


class InfoHandler(Handler):
    ''' an implementation of the handler '''

    def writeMessage(self, msg):
        print 'Writing to info: %s' % msg


class StderrHandler(Handler):
    ''' an implementation of the handler '''

    def writeMessage(self, msg):
        print 'Sending to stderr: %s' % msg

class Chain(object):
    ''' a class that creats the chain of handlers '''

    def __init__(self):
        # create a chain that handles the message from lower to higher priorities
        debugHandler = DebugHandler(Handler.DEBUG)
        infoHandler = InfoHandler(Handler.INFO)
        stderrHandler = StderrHandler(Handler.ERR)
        debugHandler.setNext(infoHandler)
        infoHandler.setNext(stderrHandler)
        self.head = debugHandler

    def getHead(self):
        return self.head

# the sender
chain = Chain()
headHandler = chain.getHead()
headHandler.handle('Entering function func.', Handler.DEBUG)
headHandler.handle('Step 1 is completed.', Handler.INFO)
headHandler.handle('An error occurs.', Handler.ERR)
