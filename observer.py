# Observer Pattern
# object pattern: relationships between objects are established at run time via composition
# behavioral pattern: how classes and objects interact and distribute responsibilities
# - define a one-to-many dependency between objects so that when one object changes state,
#   all its dependents are notified and updated automatically
# - encapsulate the core components (common or engine) in a subject abstraction and
#   the variable components (optional or user interface) in an observer hierarchy
# - the "view" part of model-view-controller
# - subject: keeper of the data model (or business logic), observer: decoupled and distinct
#   objects containing the delegated "view" functionality
# - observers register themselves with the subject as they are created (so an observer can
#   be created only if its subject is defined)
# - whenever subject changes, it broadcasts (notifies) to all registered observers
# - allow the number of "view" objects to be configured dynamically, instead of being
#   specified statically at compile-time
# - subject passes its changed states to observers by calling their update method

class Subject(object):

    def registerObserver(self, observer):
        raise NotImplementedError

    def removeObserver(self, observer):
        raise NotImplementedError

    def notifyObservers(self):
        raise NotImplementedError

class Observer(object):

    def update(self, temperature, humidity, pressure):
        raise NotImplementedError

class DisplayElement(object):

    def display(self):
        raise NotImplementedError

class WeatherData(Subject):
    # an observable, can be registered by and notified to observers

    def __init__(self):
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
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
    # an observer, will update if notified by observable

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

weatherData = WeatherData()
currentDisplay = CurrentConditionsDisplay(weatherData)
weatherData.setMeasurements(80, 65, 30.4)

