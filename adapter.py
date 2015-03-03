# Adapter Pattern
# class pattern: relationships between classes are established at compile time
# structural pattern: composes classes or objects into larger structures
# - adapter provides a different interface to its subject. proxy provides the same interface.
#   decorator provides an enhanced interface
# - facade defines a new interface, whereas adapter reuses an old(existing) interface.
#   adapter makes two existing interfaces work together as opposed to defining an entirely new one

class Duck(object):
    # an interface

    def quack(self):
        raise NotImplementedError

    def fly(self):
        raise NotImplementedError

class MallardDuck(Duck):

    def quack(self):
        print 'Quack'

    def fly(self):
        print "I'm flying."

class Turkey(object):

    def gobble(self):
        raise NotImplementedError

    def fly(self):
        raise NotImplementedError

class WildTurkey(Turkey):
    # adaptee: turkey

    def gobble(self):
        print 'gobble'

    def fly(self):
        print "I'm flying a short distance"

class TurkeyAdapter(Duck):
    # an adapter of turkey to duck

    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()

turkeyAdapter = TurkeyAdapter(WildTurkey())
turkeyAdapter.quack()
turkeyAdapter.fly()
