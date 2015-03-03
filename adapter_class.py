class Duck(object):

    def quack(self):
        raise NotImplementedError

    def fly(self):
        raise NotImplementedError

'''
class MallardDuck(Duck):

    def quack(self):
        print 'Quack'

    def fly(self):
        print "I'm flying."
'''

class Turkey(object):

    def gobble(self):
        raise NotImplementedError

    def fly(self):
        raise NotImplementedError

class WildTurkey(Turkey):
    # adaptee

    def gobble(self):
        print 'gobble'

    def fly(self):
        print "I'm flying a short distance"

class TurkeyClassAdapter(Duck, WildTurkey):

    def quack(self):
        self.gobble()

    def fly(self):
        for i in range(5):
            WildTurkey.fly(self)

turkeyAdapter = TurkeyClassAdapter()
turkeyAdapter.quack()
turkeyAdapter.fly()
