# Strategy Pattern
# a combination of strategy pattern and template methods

class Strategy(object):
    # define the interface of the algorithm

    def solve(self):
        raise NotImplementedError

class TemplateMethod1(Strategy):
    # bury implementation, template method

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
    # bury implementation, template method

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

    def preProcess(self):
        print 'preProcess  '

    def postProcess(self):
        print 'postProcess  '

    def search(self):
        print 'search  %s' % self.state
        self.state += 1
        return self.state == 3

# clients couple strictly to the interface
algorithms = (Impl1(), Impl2())
for i in range(len(algorithms)):
    algorithms[i].solve()
