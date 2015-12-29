# Observer Pattern
# object pattern: relationships between objects are established at run time via composition
# behavioral pattern: how classes and objects interact and distribute responsibilities
# - define a one-to-many dependency between objects so that when one object changes state,
#   all its dependents are notified and updated automatically
# - subject passes its changed state to registered observers by calling their update method
# - encapsulate the core components (common or engine) in a subject abstraction and
#   the variable components (optional or UI) in an observer hierarchy
# - the "view" part of model-view-controller (MVC)
#   a) subject: keeper of the data model (or business logic), observer: decoupled and distinct
#      objects containing the delegated "view" functionality
#   b) whenever there is a state change, the views get notified by the controller
#   c) the view objects can be configured dynamically, instead of being specified statically
#      at compile-time
# - note that observers can be created only if its subject is defined (observers register 
#   themselves with the subject when they are created)
#
#   a) observer pattern:
#                                (HAS_A)
#       Subject Interface <.................> Observer Interface
#               ^          notify & register        ^
#        (IS_A) |                                   | (IS_A)
#        SubjectExample                        ObserverExample
#
#       (when the observer object is constructed, the subject object should be specified)
#
#   b) mediator pattern:
#
#                                                                    --------- ColleagueExample1
#                                (HAS_A)                             | (IS_A)
#                           <...............>                     <--- 
#        Mediator Interface <...............> Colleague Interface <---
#                ^           send & register                         | (IS_A)
#         (IS_A) |                                                   --------- ColleagueExample2
#          MediatorExample
#
#       (when the colleague object is constructed, the mediator object should be specified)
#       (the mediator object implements how two colleague objects communicate with each other)


class Subject(object):
    ''' the subject interface defining register(), remove(), and notify() methods for the
        observers to register themselves to or remove from the subject, and got notified
        whenever there is a state change in the subject
    '''

    def registerObserver(self, observer):
        raise NotImplementedError

    def removeObserver(self, observer):
        raise NotImplementedError

    def notifyObservers(self):
        raise NotImplementedError

class Observer(object):
    ''' the observer interface defining update() method, which will be called by the subject
        whenever the subject has a state change
    '''

    def update(self, temperature, humidity, pressure):
        raise NotImplementedError

class DisplayElement(object):

    def display(self):
        raise NotImplementedError

class WeatherData(Subject):
    ''' an implementation of the subject, maintaining a list of registered observers '''

    def __init__(self):
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        # notify all the registered observers by calling their update() method
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature =temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

class CurrentConditionsDisplay(Observer, DisplayElement):
    ''' an implementation of the observer with a specific implementation of the update method '''

    def __init__(self, weatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print 'Current conditions: %s F degrees and %s%% humidity' % (
            self.temperature, self.humidity
            )

weatherData = WeatherData() # the subject object
currentDisplay = CurrentConditionsDisplay(weatherData) # the observer object, which is passed in
                                                       # the subject object to set up registeration
                                                       # in the constructor
weatherData.setMeasurements(80, 65, 30.4) # the state of the subject object changes

