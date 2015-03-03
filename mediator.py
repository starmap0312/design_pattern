# Mediator Pattern
# behavioral pattern: encapsulate how a set of objects interact 
# objects no longer interact with each other directly, instead they communicate through mediator,
# thus lowers the coupling of objects
# - promotes loose coupling, keeping objects from referring to each other explicitly
# - mediator promotes a "many-to-many relationship network" to "full object status"
# - mediator enhances encapsulation, and allows the inter-relationships to be modified or
#   extended through subclassing

class Mediator(object):

    def setMedic(self, medic):
        self.medic = medic

    def setInfantry(self, infantry):
        self.infantry =  infantry

    def work(self, msgType, msgCondition, colleague):
        raise NotImplementedError

class ConcreteMediator(Mediator):
    # mediator will pass on the message to the right colleague

    def work(self, msgType, msgCondition, colleague):
        print "mediator receives %s's message: %s" % (colleague, msgCondition)
        if msgType == 'hurt':
            self.medic.takeAction(msgCondition, colleague)
        elif msgType == 'attack':
            self.infantry.takeAction(msgCondition, colleague)
        else: # msgType == 'normal'
            if colleague != self.medic:
                self.medic.receive(msgCondition, colleague)
            if colleague != self.infantry:
                self.infantry.receive(msgCondition, colleague)

class Colleague(object):

    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def __str__(self):
        return self.name

    def send(self, msgType, msgCondition):
        self.mediator.work(msgType, msgCondition, self)

    def receive(self, msgCondition, colleague):
        print '%s receives message from %s: %s' % (self, colleague, msgCondition)

class Medic(Colleague):

    def __init__(self, name, mediator):
        super(Medic, self).__init__(name, mediator)
        mediator.medic = self

    def takeAction(self, msgCondition, colleague):
        print "%s receives %s's message: %s. I will go heal you." % (self, colleague, msgCondition)

class Infantry(Colleague):

    def __init__(self, name, mediator):
        super(Infantry, self).__init__(name, mediator)
        mediator.infantry = self

    def takeAction(self, msgCondition, colleague):
        print "%s receives %s's message: %s. I will go help you." % (self, colleague, msgCondition)

mediator = ConcreteMediator()
medic = Medic('nurse', mediator)
infantry = Infantry('soldier', mediator)
medic.send('normal', 'the wind blows')
infantry.send('normal', 'a rabbit passes by')
medic.send('attack', 'i am under attack')
infantry.send('hurt', 'i am hurt')
