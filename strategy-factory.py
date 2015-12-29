# example: strategy pattern with factory methods

class Duck(object):
    ''' an interface that defines how the client will use the algorithm objects '''

    def createFlyBehavior(self):
        # a factory method for the algorithm object
        raise NotImplementedError

    def createQuackBehavior(self):
        # a factory method for the algorithm object
        raise NotImplementedError

    def performFly(self):
        # the use of the algorithm object
        self.flyBehavior = self.createFlyBehavior()
        self.flyBehavior.fly()

    def performQuack(self):
        # the use of the algorithm object
        self.quackBehavior = self.createQuackBehavior()
        self.quackBehavior.quack()

    def swim(self):
        print 'all ducks float'

class FlyBehavior(object):
    ''' an interface of the fly algorithm '''

    def fly(self):
        raise NotImplementedError

class FlyWithWings(FlyBehavior):
    ''' an implementation of the fly algorithm '''

    def fly(self):
        print "I'm flying"

class FlyNoWay(FlyBehavior):
    ''' an implementation of the fly algorithm '''

    def fly(self):
        print "I can't fly"

class QuackBehavior(object):
    ''' an interface of the quack algorithm '''

    def quack(self):
        raise NotImplementedError

class Quack(QuackBehavior):
    ''' an implementation of the quack algorithm '''

    def quack(self):
        print 'Quack'

class MuteQuack(QuackBehavior):
    ''' an implementation of the quack algorithm '''

    def quack(self):
        print 'Silence'

class MallardDuck(Duck):
    ''' an implementation of the factory methods '''

    def createFlyBehavior(self):
        return FlyWithWings()

    def createQuackBehavior(self):
        return Quack()

    def display(self):
        print "I'm a real Mallard duck"

mallard = MallardDuck()
mallard.performQuack()
mallard.performFly()
mallard.swim()
mallard.display()
