# Command Pattern
# - issue requests to objects without knowing about the operation being requested or
#   the receiver of the request
# - command encapsulates (wraps) in an object: an object, a method name, and some arguments
# - create a class that encapsulates: 1. a "receiver" object, 2. the method to invoke
#   3. the arguments to pass

class Command(object):

    def execute(self):
        raise NotImplementedError

class Politician(Command):

    def execute(self):
        print 'politician: take money from the rich'

class Engineer(Command):

    def execute(self):
        print 'engineer: take out the trash'

class Programmer(Command):

    def execute(self):
        print 'programmer: sell the bugs'

class CommandQueue(object):

    def produceRequests(self):
        queue = []
        queue.append(Engineer())
        queue.append(Politician())
        queue.append(Programmer())
        return queue

    def runRequests(self, queue):
        for command in queue:
            command.execute()

# client codes
cmd_queue = CommandQueue()
queue = cmd_queue.produceRequests()
cmd_queue.runRequests(queue)

