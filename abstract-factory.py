# Abstract Factory Pattern

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
    # abstract class for creating factory objects, having a static method for creating abstract
    # factory objects based on parameters
    # single entry point for creating factory objects

    (EMBER, ENGINOLA) = (1, 2)

    @staticmethod
    def getFactory(architecture):
        if architecture == AbstractToolkit.EMBER:
            return EmberToolkit()
        elif architecture == AbstractToolkit.ENGINOLA:
            return EnginolaToolkit()

    def createCPU(self):
        raise NotImplementedError

    def createMMU(self):
        raise NotImplementedError

class EmberToolkit(AbstractToolkit):
    # abstract factory implementation

    def createCPU(self):
        return EmberCPU()

    def createMMU(self):
        return EmberMMU()

class EnginolaToolkit(AbstractToolkit):
    # abstract factory implementation

    def createCPU(self):
        return EnginolaCPU()

    def createMMU(self):
        return EnginolaMMU()

# the client codes
abstractFactory = AbstractToolkit.getFactory(AbstractToolkit.EMBER)
cpu = abstractFactory.createCPU()
mmu = abstractFactory.createMMU()
