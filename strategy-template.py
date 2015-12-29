# Strategy Pattern
#
# example: strategy pattern with template methods

class Strategy(object):
    ''' an interface of the algorithm objects '''

    def solve(self):
        raise NotImplementedError

class TemplateMethod1(Strategy):
    ''' a subclass of the interface with template methods '''

    def solve(self):
        self.start()
        while self.nextTry() and not self.isSolution():
            pass
        self.stop()

    def start(self):
        raise NotImplementedError

    def nextTry(self):
        raise NotImplementedError

    def isSolution(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

class Impl1(TemplateMethod1):
    ''' an implementation of the subclass '''

    def __init__(self):
        self.state = 1

    def start(self):
        print 'start  '

    def nextTry(self):
        print 'nextTry  %s' % self.state
        self.state += 1
        return True

    def isSolution(self):
        print 'isSolution %s' % (self.state == 3)
        return self.state == 3

    def stop(self):
        print 'stop  '

class TemplateMethod2(Strategy):
    ''' a subclass of the interface with template methods '''

    def __init__(self):
        self.state = 1

    def solve(self):
        while True:
            self.preProcess()
            if self.search():
                break
            self.postProcess()

    def preProcess(self):
        raise NotImplementedError

    def postProcess(self):
        raise NotImplementedError

    def search(self):
        raise NotImplementedError

class Impl2(TemplateMethod2):
    ''' an implementation of the subclass '''

    def preProcess(self):
        print 'preProcess  '

    def postProcess(self):
        print 'postProcess  '

    def search(self):
        print 'search  %s' % self.state
        self.state += 1
        return self.state == 3

# the client creates the implementation object but calls the superclass' template method
# the coupling can be minimized if the construction of the object is separated, ex. by injection
algorithm1 = Impl1()
algorithm1.solve()
algorithm2 = Impl2()
algorithm2.solve()
