# Chain of Responsibility Pattern
# decouples the sender of the request and its receivers
# the senders instead sends to a chain of receivers, in which a receiver passes the message to
# its following receivers

class Logger(object):
    # a tempalte containing "next" reference that can be used as a list node

    ERR = 3
    INFO = 5
    DEBUG = 7

    def __init__(self, mask):
        self.mask = mask
        self.next = None # points to the next logger

    def setNext(self, logger):
        self.next = logger

    def message(self, msg, priority):
        # message will be passed on to the next logger
        if priority <= self.mask:
            self.writeMessage(msg)
        if self.next is not None:
            self.next.message(msg, priority)

    def writeMessage(self, msg):
        raise NotImplementedError

class StdoutLogger(Logger):

    def writeMessage(self, msg):
        print 'Writing to stdout: %s' % msg


class EmailLogger(Logger):

    def writeMessage(self, msg):
        print 'Sending via email: %s' % msg


class StderrLogger(Logger):

    def writeMessage(self, msg):
        print 'Sending to stderr: %s' % msg

class Chain(object):
    # create chain of logger, from lower to higher priorities

    def create(self):
        # create a list of loggers
        logger = StdoutLogger(Logger.DEBUG)
        logger1 = EmailLogger(Logger.INFO)
        logger.setNext(logger1)
        logger2 = StderrLogger(Logger.ERR)
        logger1.setNext(logger2)
        # return the head of the list
        return logger

chain = Chain().create()
chain.message('Entering function func.', Logger.DEBUG)
chain.message('Step 1 is completed.', Logger.INFO)
chain.message('An error occurs.', Logger.ERR)
