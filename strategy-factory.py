
class Duck(object):
    # Factory Method: a specialization of template method

    def createFlyBehavior(self):
        raise NotImplementedError

    def createQuackBehavior(self):
        raise NotImplementedError

    def performFly(self):
        self.flyBehavior = self.createFlyBehavior()
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior = self.createQuackBehavior()
        self.quackBehavior.quack()

    def swim(self):
        print 'all ducks float'


class FlyBehavior(object):

    def fly(self):
        raise NotImplementedError

class FlyWithWings(FlyBehavior):

    def fly(self):
        print "I'm flying"

class FlyNoWay(FlyBehavior):

    def fly(self):
        print "I can't fly"

class QuackBehavior(object):

    def quack(self):
        raise NotImplementedError

class Quack(QuackBehavior):

    def quack(self):
        print 'Quack'

class MuteQuack(QuackBehavior):

    def quack(self):
        print 'Silence'

class MallardDuck(Duck):

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
