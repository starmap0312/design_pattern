class Strategy(object):
    # 1. define the interface of the algorithm

    def solve(self):
        raise NotImplementedError

class TemplateMethod1(Strategy):
    # 2. bury implementation: defer implementation to subclasses
    # 3. template method

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

class Implementation1(TemplateMethod1):

    def __init__(self):
        self.state = 1

    def start(self):
        print 'start '

    def nextTry(self):
        print 'nextTry-%s  ' % self.state
        self.state += 1
        return True

    def isSolution(self):
        print 'isSolution-%s  ' % (self.state == 3)
        return (self.state == 3)

    def stop(self):
        print 'stop  '

class TemplateMethod2(Strategy):
    # 2. bury implementation
    # 3. template method

    def solve(self):
        while True:
            self.preProcess()
            if self.search():
                break
            self.postProcess()

    def preProcess(self):
        raise NotImplementedError 

    def search(self):
        raise NotImplementedError 

    def postProcess(self):
        raise NotImplementedError 

class Implementation2(TemplateMethod2):

    def __init__(self):
        self.state = 1

    def preProcess(self):
        print 'preProcess  '

    def search(self):
        print 'search-%s  ' % self.state
        self.state += 1
        return True if self.state == 3 else False

    def postProcess(self):
        print 'postProcess  '

# 4. clients couple strictly to the interface

algorithm = Implementation1()
algorithm.solve()
algorithm2 = Implementation2()
algorithm2.solve()
