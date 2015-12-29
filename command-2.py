# Command Pattern
# - issue requests to objects' operations (in the invoker) without knowing about the requested
#   operation or the receiver object
# - a command object encapsulates (wraps): 
#   a) a receiver object
#   b) the receiver's operation to be invoked
#   c) the arguments to be passed in

# a simple example

class Command(object):
    ''' a uniform interface '''

    def execute(self):
        raise NotImplementedError

class PoliticianCommand(Command):
    ''' an implmentation of the interface '''

    def execute(self):
        print 'politician: take money from the rich'

class EngineerCommand(Command):
    ''' an implmentation of the interface '''

    def execute(self):
        print 'engineer: take out the trash'

class ProgrammerCommand(Command):
    ''' an implmentation of the interface '''

    def execute(self):
        print 'programmer: sell the bugs'

class Invoker(object):
    ''' the invoker class: knows how to use command objects but delegates the construction to
        external code (i.e. the client)
    '''

    def __init__(self):
        self.queue = []

    def addCommand(self, cmd):
        self.queue.append(cmd)

    def runCommands(self):
        for command in self.queue:
            command.execute()

# the client
invoker = Invoker()
invoker.addCommand(EngineerCommand())
invoker.addCommand(PoliticianCommand())
invoker.addCommand(ProgrammerCommand())
invoker.runCommands()
