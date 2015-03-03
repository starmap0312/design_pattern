# Template Method
# behavioral pattern: how classes and objects interact and distribute responsibilities
# class pattern: relationships between classes are established at compile time
# - defines a skeleton of an algorithm
# - Hollywood principle: "Don't call us, we'll call you."
# - inverted control structure: let superclass(template) call you
# - factory method is a specialization of template method

class CaffeineBeverage(object):

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.wantCondiments():
            self.addCondiments()

    def boilWater(self):
        pass

    def brew(self):
        raise NotImplementedError

    def pourInCup(self):
        pass

    def addCondiments(self):
        raise NotImplementedError

    def wantCondiments(self):
        # hook
        return True

class Tea(CaffeineBeverage):

    def brew(self):
        print 'steeping the tea'

    def addCondiments(self):
        print 'adding lemon'

class Coffee(CaffeineBeverage):

    def brew(self):
        print 'dripping coffee through filter'

    def addCondiments(self):
        print 'adding sugar and milk'

    def wantCondiments(self):
        return False

Tea().prepareRecipe()
Coffee().prepareRecipe()
