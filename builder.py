# Builder Pattern
# - when the constructor contains too many parameters, consider use a builder to
#   build the product incrementally
# - separate the construction of a complex object from its representation so that the same
#   construction process can create different representations
# - unlike creational pattern that constructs products in one shot, the builder pattern constructs
#   the product step by step under the control of the director

class Car(object):
    # the product
    # when an object is too complicated to construct by one constructor with many parameters
    # it can be constructed part by part by a builder

    def __init__(self):
        self.numSeats = None
        self.carType = None
        self.hasTripComputer = None
        self.setGPS = None

    def show(self):
        print 'This is a %s with %s seats that has %s trip computer with %s GPS' % (
            self.carType, 
            self.numSeats, 
            'a' if self.hasTripComputer else 'no',
            'a' if self.setGPS else 'no'
            )

class AbstractCarBuilder(object):
    # a builder interface

    def getResult(self):
        raise NotImplementedError

    def setSeats(self, number):
        raise NotImplementedError

    def setCityCar(self):
        raise NotImplementedError

    def setSportsCar(self):
        raise NotImplementedError

    def setTripComputer(self):
        raise NotImplementedError

    def setGPS(self):
        raise NotImplementedError

    def unsetGPS(self):
        raise NotImplementedError

class CarBuilder(AbstractCarBuilder):
    # a builder implementation 

    def __init__(self):
        self.car = Car()

    def getResult(self):
        return self.car

    def setSeats(self, number):
        self.car.numSeats = number

    def setCityCar(self):
        self.car.carType = 'city car'

    def setSportsCar(self):
        self.car.carType = 'sports car'

    def setTripComputer(self):
        self.car.hasTripComputer = True

    def setGPS(self):
        self.car.setGPS = True

    def unsetGPS(self):
        self.car.setGPS = False

# the client build the object part by part and get the result in the end
carBuilder = CarBuilder()
carBuilder.setSeats(2)
carBuilder.setSportsCar()
carBuilder.setTripComputer()
carBuilder.unsetGPS()
car = carBuilder.getResult()
car.show()
