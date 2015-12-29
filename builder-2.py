# Builder Pattern
# - an example of builder pattern with dependency injection
#   a) the use of a builder object is separated into a Director class
#   b) the builder pattern constructs the product step by step under the control of the director
#
#             (HAS_A)
#    Director .......> Builder Interface
#              uses           ^
#                             | (IS_A)   (HAS_A)
#                       BuilderExample  ........> Product
#
# - creational patterns:
#   a) simple factory: a class with a method that takes a type parameter, constructing and
#      returning the product created based on the paramter
#   b) builder pattern: an interface with bulidParts() and getProduct() methods for constructing
#      a complex product (an additional Director class that takes and uses a builder object
#      can be added to the design)
#   c) factory method: an interface with create() method that constructs and returns a product
#      the construction of a specific type of the product is implemented in a subclass
#   d) abstract factory: an interface with some create() methods for a family of related products
#      the construction of a specific family of products is implemented in a subclass
#   (note that the construction of the product is often separated from its representation, so
#    that the same construction process can create different representations)
#   

class Pizza(object):
    ''' a complex product to be built '''

    def __init__(self):
        self.dough = ''
        self.sauce = ''
        self.topping = ''

    def setDough(self, dough):
        self.dough = dough

    def setSauce(self, sauce):
        self.sauce = sauce

    def setTopping(self, topping):
        self.topping = topping

class PizzaBuilder(object):
    ''' the builder interface defining the buildParts() and getProduct() methods '''

    def createPizza(self):
        self.pizza = Pizza()

    def getPizza(self):
        return self.pizza

    def buildDough(self):
        raise NotImplementedError

    def buildSauce(self):
        raise NotImplementedError

    def buildTopping(self):
        raise NotImplementedError

class HawaiianPizzaBuilder(PizzaBuilder):
    ''' a concrete builder implementing the buildParts() methods '''

    def buildDough(self):
        self.pizza.setDough('cross')

    def buildSauce(self):
        self.pizza.setSauce('mild')

    def buildTopping(self):
        self.pizza.setTopping('ham and pineapple')

class SpicyPizzaBuilder(PizzaBuilder):
    ''' a concrete builder implementing the buildParts() methods '''

    def buildDough(self):
        self.pizza.setDough('pan baked')

    def buildSauce(self):
        self.pizza.setSauce('hot')

    def buildTopping(self):
        self.pizza.setSauce('pepperoni and salami')

class Waiter(object):
    ''' the Director class defining a template method for the use of a builder object
        i.e. a client class of the builder object, and the construction of the builder object
             is delegated to external code
    '''

    def setPizzaBuilder(self, pizzaBuilder):
        # the builder object is injected via this setter method
        self.pizzaBuilder = pizzaBuilder

    def getPizza(self):
        # use the builder object to get the final result of the built product
        return self.pizzaBuilder.getPizza()

    def constructPizza(self):
        # use the builder object to construct the complex product (as the sequence of construction
        # steps is fixed, this method ensures that the product is always constructed in the
        # same process)
        self.pizzaBuilder.createPizza()
        self.pizzaBuilder.buildDough()
        self.pizzaBuilder.buildSauce()
        self.pizzaBuilder.buildTopping()

# the injector code
waiter = Waiter()
hawaiianPizzaBuilder = HawaiianPizzaBuilder() # construct a builder object
waiter.setPizzaBuilder(hawaiianPizzaBuilder) # inject the builder object into the director object
waiter.constructPizza() # use the builder object to construct the product
pizza = waiter.getPizza() # use the builder object to get the final result of the product
print '(%s, %s, %s)' % (pizza.dough, pizza.sauce, pizza.topping)
spicyPizzaBuilder = SpicyPizzaBuilder()
waiter.setPizzaBuilder(spicyPizzaBuilder)
waiter.constructPizza()
pizza = waiter.getPizza()
print '(%s, %s, %s)' % (pizza.dough, pizza.sauce, pizza.topping)

