# Command Pattern
# - client issue requests to receiver's operations using invoker without knowing about
#   requested operation or the receiver object (client is decoupled from receivers)
# - command object encapsulates (wraps) receiver object
#   a) receiver's operation to be invoked
#   b) arguments to be passed in
#
# example: a simplified version without receiver (command objects do the real tasks directly)

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
    ''' the invoker class works like a composite object
        only knows how to use command objects but delegates the construction to external code (client)
    '''

    def __init__(self):
        self.queue = []

    def addCommand(self, cmd):
        self.queue.append(cmd)

    def runCommands(self):
        for command in self.queue:
            command.execute()

# client
invoker = Invoker()
invoker.addCommand(EngineerCommand())
invoker.addCommand(PoliticianCommand())
invoker.addCommand(ProgrammerCommand())
invoker.runCommands()
