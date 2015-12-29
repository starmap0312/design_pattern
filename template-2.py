# Template Pattern
# - 2-layers template pattern (template method of template method)
# - define the skeleton of an algorithm in a superclass and defer some steps to suclasses
# - the hollywood principle: "don't call us (derived don't call base), 
#   we call you (base calls derived)"
# - strategy pattern is like template pattern except in its granularity
#   (strategy pattern: defer the implementation of the whole algorithm in subclasses
#    template pattern: defer the implementation of parts of the algorithm in subclasses)
# - factory method is a specilization of template method
#   (factory method is specifically for object creation)

class Generalization(object):
    ''' a superclass with a template method being the skeleton of an algorithm '''

    # 1. standardize the skeleton of an algorithm in a "template method"
    def findSolution(self):
        self.stepOne()
        self.stepTwo()
        self.stepThree()
        self.stepFour()

    # 2. common implementation of individual steps are defined in base class
    def stepOne(self):
        print 'Generalization.stepOne'

    # 3. steps requiring peculiar implementations are placeholders in base class
    def stepTwo(self):
        raise NotImplementedError

    def stepThree(self):
        raise NotImplementedError

    def stepFour(self):
        print 'Generalization.stepFour'

class Specialization(Generalization):
    ''' a subclass in which parts of the algorithm are implemented here '''

    # 4. derived classes can override placeholder methods
    # 1. standardize the skeleton of an algorithm in a "template method"
    def stepThree(self):
        self.step3_1()
        self.step3_2()
        self.step3_3()

    # 2. common implementation of individual steps are defined in base class
    def step3_1(self):
        print 'Specialization.step3_1'

    # 3. steps requiring peculiar implementations are placeholders in base class
    def step3_2(self):
        raise NotImplementedError

    def step3_3(self):
        print 'Specialization.step3_1'

class Realization(Specialization):
    ''' a sub-subclass in which parts of the algorithm are implemented here '''

    # 4. derived classes can override placeholder methods
    def stepTwo(self):
        print 'Realization.stepTwo'

    def step3_2(self):
        print 'Realization.step3_2'

    # 4. derived classes can override implemented methods
    def stepFour(self):
        print 'Realization.stepFour'
        super(Realization, self).stepFour()

# the client creates the implementation object but calls the superclass' template method
# the coupling of the client and the implementation object can be minimized if the construction
# of the object is separated, ex. by injection
algorithm = Realization()
algorithm.findSolution()
