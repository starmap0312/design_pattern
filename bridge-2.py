# Bridge Pattern
# - decompose the component's interface and implementation into orthogonal class hierarchies
# - a synonym for "handle/body" idiom: interface object -> handle, implementation object -> body
# - the handle/body idiom is used to decompose a complex abstraction into smaller, more
#   manageable classes
# - for example, used in the sharing of a single resource by multiple classes that controll
#   access to it
# - decide two orthogonal dimensions exist in domain, ex: abstraction/platform, or
#   domain/infrastructure, or front-end/back-end, or interface/implementation
# - separation of concerns: what does the client want (abstraction), and what do the platforms
#   provide (implemenation)
# - define a derived class of that interface for each platform
# - create the abstraction base class that HAS_A platform object and
#   delegates the platform-oriented functionality to it
# - adapter makes things work after they're designed; bridge makes them work before they are
# - state, strategy, bridge (and to some degree adapter) have similar solution structure
#   they all share elements of the "handle/body" idiom. They differ in intent (solve different
#   problems)
# - if the interface classes delegate the creation of their implementation classes (instead
#   of coupling themselves directly), then the design usually uses the abstract factory pattern
#   to create the implementation objects

class Stack(object):
    # interface that HAS_A an actual stack implementation object and delegates all requests to it (a wrapper class)

    def __init__(self, a_type):
        # creation of implementation classes through parameter, direct coupling
        # here we can also change the design to pass in an abstract factory for creation,
        # decoupling abstraction and implementation 
        if a_type == 'mine':
            self.imp = StackMine()
        else:
            StackNull() # other actual implementation 

    def push(self, num):
        self.imp.push(int(num))

    def pop(self):
        return self.imp.pop()

    def isEmpty(self):
        return self.imp.empty()

class StackHanoi(Stack):
    # specific interface implemenation: specify the handle (the way to access the body)

    def __init__(self, a_type=None):
        super(StackHanoi, self).__init__(a_type if a_type else 'mine')
        self.totalRejected = 0

    def reportRejected(self):
        return self.totalRejected

    def push(self, num):
        # only smaller number can be pushed to the top of stack; otherwise, reject it
        if not self.imp.empty() and num > self.imp.peek():
            self.totalRejected += 1
        else:
            self.imp.push(num)

class StackImp(object):
    # create an abstraction for implementation, i.e. implementation interface (i.e. body base class)

    def push(self, obj):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def empty(self):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

class StackMine(StackImp):
    # actual implementation of the Stack 

    def __init__(self):
        self.items = []
        self.total = -1

    def push(self, obj):
        self.total += 1
        return self.items.append(obj)

    def peek(self):
        return self.items[self.total]

    def pop(self):
        item = self.items[self.total]
        self.total -= 1
        return item

    def empty(self):
        return self.total == -1

stacks = (Stack('mine'), StackHanoi('mine'))
from random import randrange
for i in range(20):
    num = randrange(1000) % 40
    for j in range(len(stacks)):
        stacks[j].push(num)

for i in range(len(stacks)):
    while not stacks[i].isEmpty():
        print stacks[i].pop(), 
    print ''

print 'total rejected: %s' % stacks[1].reportRejected()
