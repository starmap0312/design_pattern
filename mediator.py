# Mediator Pattern
# behavioral pattern: encapsulate how a set of objects interact 
# objects no longer interact with each other directly, instead they communicate through a
# mediator object, thus lowering the coupling of objects
# - promote loose coupling, keeping objects from referring to each other explicitly
# - promote a "many-to-many relationship network" to "full object status"
# - enhance encapsulation, and allows the inter-relationships to be modified or
#   extended through subclassing
#
#                                                                    --------- ColleagueExample1
#                                (HAS_A)                             | (IS_A)
#                           <...............>                     <--- 
#        Mediator Interface <...............> Colleague Interface <---
#                ^           notify & register                       | (IS_A)
#         (IS_A) |           & send                                  --------- ColleagueExample2
#          MediatorExample
#
#       (when the colleague object is constructed, the mediator object should be specified)
#       (the mediator object implements how two colleague objects communicate with each other)
#

class Mediator(object):
    ''' the mediator interface, responsible for the communication of two specified colleague
        objects: one medic and one infantry
    '''

    def registerMedic(self, medic):
        self.medic = medic

    def registerInfantry(self, infantry):
        self.infantry =  infantry

    def exchangeMsg(self, msgType, msgCondition, colleague):
        # provide a exchangeMsg() method for the colleague objects to call
        raise NotImplementedError

class ConcreteMediator(Mediator):
    ''' a concrete mediator implements how to pass on the message to the right colleague '''

    def exchangeMsg(self, msgType, msgCondition, colleague):
        # the mediator object calls the notify() method of the specified colleague object
        print "mediator receives %s's message: %s" % (colleague, msgCondition)
        if msgType == 'hurt':
            self.medic.notify(msgCondition, colleague)
        elif msgType == 'attack':
            self.infantry.notify(msgCondition, colleague)
        else: # msgType == 'normal'
            if colleague != self.medic:
                self.medic.receive(msgCondition, colleague)
            if colleague != self.infantry:
                self.infantry.receive(msgCondition, colleague)

class Colleague(object):
    ''' the interface of the colleague '''

    def __init__(self, name, mediator):
        # a colleague can be constructed only if the mediator object is specified
        self.name = name
        self.mediator = mediator

    def __str__(self):
        return self.name

    def send(self, msgType, msgCondition):
        # a colleague object relies on the mediator object to send messages to another colleague
        # object
        self.mediator.exchangeMsg(msgType, msgCondition, self)

    def receive(self, msgCondition, colleague):
        print '%s receives message from %s: %s' % (self, colleague, msgCondition)

class Medic(Colleague):
    ''' an implementation of the colleague which is named medic '''

    def __init__(self, name, mediator):
        super(Medic, self).__init__(name, mediator)
        mediator.registerMedic(self)

    def notify(self, msgCondition, colleague):
        print "%s receives %s's message: %s. I will go heal you." % (self, colleague, msgCondition)

class Infantry(Colleague):
    ''' an implementation of the colleague which is named infantry '''

    def __init__(self, name, mediator):
        super(Infantry, self).__init__(name, mediator)
        mediator.registerInfantry(self)

    def notify(self, msgCondition, colleague):
        print "%s receives %s's message: %s. I will go help you." % (self, colleague, msgCondition)

mediator = ConcreteMediator()
medic = Medic('nurse', mediator)
infantry = Infantry('soldier', mediator)
medic.send('normal', 'the wind blows')
infantry.send('normal', 'a rabbit passes by')
medic.send('attack', 'i am under attack')
infantry.send('hurt', 'i am hurt')
