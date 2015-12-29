# Interface Segregation Principle
# - no class should be forced to implement methods it does not use
# - split large interfaces into smaller, more cohesive ones, so that most classes only need
#   to know about the methods they are interested in
# - what is an interface?
#   a) the conceptual explanation of a class, i.e. self-explanatory code
#   b) a mean to prevent dependencies, ex. use of dependency inversion
# - examples
#   a) without interface segregation principle
# - with the interface segregation principle, the code is more flexible and extensible
#
#                  Working (one large, polluted interface)
#                   ^  ^
#            (IS_A) |  | (IS_A)
#        Worker ----|  |---- Robot
#

class Working(object):
    ''' one large, polluted interface '''

    def work(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError

class Worker(Working):

    def work(self):
        print "do some work"

    def eat(self):
        print "do some eating"

class Robot(Working):
    ''' a class that implements the large, polluted interface '''

    def work(self):
        print "do some robot work"

    def eat(self):
        # a robot never needs to eat
        raise NotImplementedError

class Manager(object):
    ''' a client of worker that only uses service object and delegates the construction of the
        service to external code
    '''

    def setWorker(self, worker):
        self.worker = worker

    def manage(self):
        self.worker.work()

manager = Manager()
manager.setWorker(Worker())
manager.manage()

#   a) with interface segregation principle
#
#          Eatable    ------>    Workable  (two smaller interfaces)
#             ^       |             ^
#      (IS_A) |       | (IS_A)      | (IS_A)
#          Worker ----|           Robot
#

class Workable(object):
    ''' a smaller interface '''

    def work(self):
        raise NotImplementedError

class Eatable(object):
    ''' a smaller interface '''

    def eat(self):
        raise NotImplementedError

class Worker(Workable, Eatable):
    ''' a class that implements both interfaces '''

    def work(self):
        print "do some work"

    def eat(self):
        print "do some eating"

class Robot(Workable):

    ''' a class that implements only one of the interfaces '''
    def work(self):
        print "do some robot work"

manager = Manager()
manager.setWorker(Robot())
manager.manage()
