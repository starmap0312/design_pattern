# Template Pattern
# - 2-layers template pattern (template method of template method)
# - define the skeleton of an algorithm in an operation, deferring some steps
#   to client suclasses
# - the hollywood principle: "don't call us (derived don't call base), 
#   we call you (base calls derived)"
# - strategy is like template method except in its granularity
# - factory method is a specilization of template method

class Generalization(object):
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

    # 4. derived classes can override placeholder methods
    def stepTwo(self):
        print 'Realization.stepTwo'

    def step3_2(self):
        print 'Realization.step3_2'

    # 4. derived classes can override implemented methods
    def stepFour(self):
        print 'Realization.stepFour'
        super(Realization, self).stepFour()

algorithm = Realization()
algorithm.findSolution()
