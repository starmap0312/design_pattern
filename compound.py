
class QuackObservable(object):
    # an observable interface

    def registerObserver(self, observer):
        raise NotImplementedError

    def notifyObservers(self):
        raise NotImplementedError

class Observable(QuackObservable):
    # every quackable subclass has an observable that can register and notify observers

    def __init__(self, duck):
        self.observers = []
        self.duck = duck

    def registerObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        iterator = Iterator(self.observers)
        while iterator.hasNext():
            observer = iterator.next()
            observer.update(self.duck)

class Quackable(object):
    # an quackable interface

    def quack(self):
        raise NotImplementedError

class MallardDuck(Quackable):
    # a quackable implementation and has an observable

    def __init__(self):
        self.observable = Observable(self)

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def quack(self):
        print 'Quack'

class Observer(object):

    def update(self, duck):
        raise NotImplementedError

class Quackologist(Observer):

    def update(self, duck):
        print 'Quackologist: %s just quacked' % duck

class RubberDuck(Quackable):

    def __init__(self):
        self.observable = Observable(self)

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def quack(self):
        print 'Squeak'

class GooseAdapter(Quackable):
    # an adapter for goose object to quack

    def __init__(self, goose):
        self.goose = goose

    def quack(self):
        self.goose.honk()

class Goose(object):

    def honk(self):
        print 'Honk'

class QuackCounter(Quackable):
    # a decorator thad add new behavior that counts

    def __init__(self, duck):
        self.duck = duck
        self.numberOfQuacks = 0

    def quack(self):
        self.duck.quack()
        self.numberOfQuacks += 1

    def getQuacks(self):
        return self.numberOfQuacks

class Iterator(object):

    def __init__(self, items):
        self.items = items
        self.position = 0

    def hasNext(self):
        if self.position >= len(self.items) or self.items[self.position] is None:
            return False
        return True

    def next(self):
        item = self.items[self.position]
        self.position += 1
        return item

class Flock(Quackable):
    # a composite containing an aggregate of items

    def __init__(self):
        self.quackers = []

    def add(self, quacker):
        self.quackers.append(quacker)

    def quack(self):
        iterator = Iterator(self.quackers)
        while iterator.hasNext():
            quacker = iterator.next()
            quacker.quack()

class QuackObservable(object):

    def registerObserver(self, observer):
        raise NotImplementedError

    def notifyObservers(self):
        raise NotImplementedError

class AbstractDuckFactory(object):
    # an abstract factory interface

    def createMallardDuck(self):
        raise NotImplementedError

    def createRubberDuck(self):
        raise NotImplementedError

class DuckFactory(AbstractDuckFactory):
    # an implementation of abstract factory

    def createMallardDuck(self):
        return MallardDuck()

    def createRubberDuck(self):
        return RubberDuck()

class CountingDuckFactory(AbstractDuckFactory):
    # an implementation of abstract factory

    def createMallardDuck(self):
        return QuackCounter(MallardDuck())

    def createRubberDuck(self):
        return QuackCounter(RubberDuck())

duckFactory = CountingDuckFactory()
mallardDuck = duckFactory.createMallardDuck()
mallardDuck.quack()
mallardDuck.quack()
print mallardDuck.getQuacks()
duckFactory = DuckFactory()
rubberDuck = duckFactory.createRubberDuck()
quackologist = Quackologist()
rubberDuck.registerObserver(quackologist)
rubberDuck.quack()
rubberDuck.notifyObservers()
