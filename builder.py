# Builder Pattern
# - unlike creational pattern that constructs products in one shot, the builder pattern constructs
#   the product step by step
# - when the constructor of a product contains too many parameters, consider use a builder
#   to build the product incrementally
#
#             Builder Interface (buildParts() & getProduct() methods) 
#                     ^
#                     | (IS_A)   (HAS_A)
#               BuilderExample  ........> Product (a complex products with many parts to build)
#
#   (BuilderExample implements buildParts() methods defined in the Builder Interface)
#

class Car(object):
    ''' a complex product to be built '''

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
    ''' a builder interface defining build-parts methods '''

    def getProduct(self):
        # a factory method to get the final result of the built product
        raise NotImplementedError

    def buildSeats(self, number):
        raise NotImplementedError

    def buildCityCar(self):
        raise NotImplementedError

    def buildSportsCar(self):
        raise NotImplementedError

    def buildTripComputer(self):
        raise NotImplementedError

    def buildGPS(self):
        raise NotImplementedError

    def unsetGPS(self):
        raise NotImplementedError

class CarBuilder(AbstractCarBuilder):
    ''' an implementation of the builder '''

    def __init__(self):
        self.car = Car()

    def getProduct(self):
        return self.car

    def buildSeats(self, number):
        self.car.numSeats = number

    def buildCityCar(self):
        self.car.carType = 'city car'

    def buildSportsCar(self):
        self.car.carType = 'sports car'

    def buildTripComputer(self):
        self.car.hasTripComputer = True

    def buildGPS(self):
        self.car.setGPS = True

    def unsetGPS(self):
        self.car.setGPS = False

# use the concrete builder to construct the complex product
carBuilder = CarBuilder()
carBuilder.buildSeats(2)
carBuilder.buildSportsCar()
carBuilder.buildTripComputer()
carBuilder.unsetGPS()
# the above steps are fixed, so one can consider to put them in a template method of the builder
# or in an aditional class, i.e. Director, that uses the builder object
car = carBuilder.getProduct() # get the final result of the built product
car.show() # use of the product
