# Template Method
# behavioral pattern: how classes and objects interact and distribute responsibilities
# class pattern: relationships between classes are established at compile time
# - the skeleton of the algorithm is defined in superclass, whereas parts of the algorithm
#   are implemented in subclasses
# - Hollywood principle: "Don't call us, we'll call you."
#   inversion of control: don't call superclass' method, let superclass' method calls you
# - factory method is a specialization of template method (the factory method is specifically
#   for object creation, and the implementation of factory method is defined in subclasses)

class CaffeineBeverage(object):
    ''' a superclass with a template method for a specific task '''

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.wantCondiments():
            self.addCondiments()

    def boilWater(self):
        pass

    def brew(self):
        # part of the algorithm will be defined in subclasses
        raise NotImplementedError

    def pourInCup(self):
        pass

    def addCondiments(self):
        # part of the algorithm will be defined in subclasses
        raise NotImplementedError

    def wantCondiments(self):
        # hook
        return True

class Tea(CaffeineBeverage):
    ''' a sublcass that implements parts of the algorithm '''

    def brew(self):
        print 'steeping the tea'

    def addCondiments(self):
        print 'adding lemon'

class Coffee(CaffeineBeverage):
    ''' a sublcass that implements parts of the algorithm '''

    def brew(self):
        print 'dripping coffee through filter'

    def addCondiments(self):
        print 'adding sugar and milk'

    def wantCondiments(self):
        return False

# the client creates the implementation object but calls the template method of the superclass
# the dependency of the client on the implementation object can be minimized if the construction
# of the object is separated, ex. by injection
beverage = Tea()
beverage.prepareRecipe()
beverage = Coffee()
beverage.prepareRecipe()
