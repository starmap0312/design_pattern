# Abstract Factory Pattern (an OK design pattern)
#
#             AbstractFactory
#              ^          ^
#       (IS_A) |          | (IS_A)                (HAS_A)                        (IS_A)
#  FactoryExample1 ...  FactoryExample2 .......................> Service1Example ------> Service1
#                |....                |........................> Service2Example ------> Service2
#                                     construct via factory method
#
#  (use the implementation of the abstract factory to create a family of related objects)

class CPU(object):
    # abstract class of productA
    pass

class EmberCPU(CPU):
    # implementation of productA

    def __init__(self):
        print 'EmberCPU created'

class EnginolaCPU(CPU):
    # implementation of productA

    def __init__(self):
        print 'EnginolaCPU created'

class MMU(object):
    # abstract class of productB
    pass

class EmberMMU(MMU):
    # implementation of productB

    def __init__(self):
        print 'EmberMMU created'

class EnginolaMMU(MMU):
    # implementation of productB

    def __init__(self):
        print 'EnginolaMMU created'

class AbstractToolkit(object):
    ''' an interface for creating a family of objects
        in this example, a static method is defined, using which one can get specific
        implmentation of the abstract factory by passing in a type parameter
    '''

    (EMBER, ENGINOLA) = (1, 2)

    @staticmethod
    def getFactory(architecture):
        # a simple factory: a static method that creates objects based on its parameters
        if architecture == AbstractToolkit.EMBER:
            return EmberToolkit()
        elif architecture == AbstractToolkit.ENGINOLA:
            return EnginolaToolkit()

    def createCPU(self):
        raise NotImplementedError

    def createMMU(self):
        raise NotImplementedError

class EmberToolkit(AbstractToolkit):
    # abstract factory implementation: a family of realted objects

    def createCPU(self):
        return EmberCPU()

    def createMMU(self):
        return EmberMMU()

class EnginolaToolkit(AbstractToolkit):
    # abstract factory implementation: a family of related objects

    def createCPU(self):
        return EnginolaCPU()

    def createMMU(self):
        return EnginolaMMU()

# the client depends on the abstract factory and the parameter is passes to the static method
abstractFactory = AbstractToolkit.getFactory(AbstractToolkit.EMBER)
cpu = abstractFactory.createCPU()
mmu = abstractFactory.createMMU()
