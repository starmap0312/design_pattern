# Factory Method (an OK design pattern)
# creational pattern
# class pattern: relationships between classes are established at compile time
# - encapsulate object creation in one method
# - the superclass (interface) defines a method for creating objects, but let subclasses decide
#   which implementation of the objects to be instantiated
# - factory method is not necessary when instances never change
# - the factory method is often used with the template pattern:
#   a) superclass specifies generic the uses of the object and delegates the creation details to 
#      the subclasses
#   b) the superclass does not directly depend on the created objects, i.e. the superclass and 
#      the created objects are "loosely coupled"
#   c) factory method is called within template methods of the superclass, and therefore the
#      client of the created objects is the superclass
#
#                                (HAS_A)
#       Client .....................................> Service
#          ^                                             ^
#          | (IS_A)  constructs via factory method       | (IS_A)
#    ClientExample .................................> ServiceExample
#
# - factory method is similar to abstract factory without emphasis on families
# - often, design starts out using factory method, and evolve toward abstract factory,
#   prototype, or builder patterns, in order to achieve more flexibility
# - factory method vs. template method:
#   factory method: creating objects (construction of objects)
#   template method: implementing an application (a template use of objects)
# - one can also use a "simple factory" to create objects, i.e. define a (static) method that 
#   takes a parameter of type and returns different objects based on the parameter 
#   (advantage: the creation of objects is parameterized, the client depends on a type parameter
#    and could have more descriptive names)
#   (disadvantage: when a new object type is added, the (static) method needs to be modified)

class PizzaStore(object):
    ''' a superclass with factory and template methods '''
    # factory method: object creation defers to subclasses (i.e. via subclassing)
    # template method: generic use of the created object is invariant

    def createPizza(self, a_type):
        # factory method: specific implementation is defined in subclasses
        raise NotImplementedError

    def orderPizza(self, a_type):
        # tempalte method: generic operations on the created objects
        pizza = self.createPizza(a_type)
        assert pizza is not None
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

class NYPizzaStore(PizzaStore):
    ''' a subclass with an implemented factory method '''

    def createPizza(self, a_type):
        # a specific implementation of the factory method
        # a simple factory that returns different types of objects based on the parameter
        ingredientFactory = NYPizzaIngredientFactory()

        pizza = None
        if a_type == 'cheese':
            pizza = CheesePizza(ingredientFactory)
            pizza.setName('NY Style Cheese Pizza')
        elif a_type == 'veggie':
            pizza = VeggiePizza(ingredientFactory)
            pizza.setName('NY Style Veggie Pizza')
        return pizza


class ChicagoPizzaStore(PizzaStore):
    ''' a subclass with an implemented factory method '''

    def createPizza(self, a_type):
        # a specific implementation of the factory method
        ingredientFactory = ChicagoPizzaIngredientFactory()

        pizza = None
        if a_type == 'cheese':
            pizza = CheesePizza(ingredientFactory)
            pizza.setName('Chicago Style Cheese Pizza')
        elif a_type == 'veggie':
            pizza = VeggiePizza(ingredientFactory)
            pizza.setName('Chicago Style Veggie Pizza')
        return pizza

class Pizza(object):
    ''' a client inteface showing how to use the ingredient object, which is created by
        a passed-in ingredient factory '''

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        # use of the ingredient object
        print 'baking %s' % self.name

    def cut(self):
        # use of the ingredient object
        print 'cutting %s' % self.name

    def box(self):
        # use of the ingredient object
        print 'boxing %s' % self.name

    def setName(self, name):
        self.name = name

class CheesePizza(Pizza):
    ''' a client implementation '''

    def __init__(self, ingredientFactory):
        # an ingredient factory is injected via its constructor
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        # construction of the ingredient object
        self.cheese = self.ingredientFactory.createCheese()
        self.veggie = None

class VeggiePizza(Pizza):
    ''' a client implementation '''

    def __init__(self, ingredientFactory):
        # an ingredient factory is injected via its constructor
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        # construction of the ingredient object
        self.cheese = None
        self.veggie = self.ingredientFactory.createVeggie()

# Abstract Factory
# creational pattern: provides a way to decouple a client and the objects it creates
# object pattern: relationships between classes are established at run time via composition
# - decouples the client from the object it creates, insulating the client code from changes
#   i.e. adding new concrete types is done by modifying the client code to use a different
#        abstract factory implementation

class PizzaIngredientFactory(object):
    ''' an abstract factory for a family of ingredient objects
        object creation defers to subclasses (i.e. via subclassing)
    '''

    def createCheese(self):
        raise NotImplementedError

    def createVeggie(self):
        raise NotImplementedError

class NYPizzaIngredientFactory(PizzaIngredientFactory):
    ''' an implementation of the abstract factory '''

    def createCheese(self):
        return ReggianoCheese()

    def createVeggie(self):
        return GarlicVeggie()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    ''' an implementation of the abstract factory '''

    def createCheese(self):
        return MozzarellaCheese()

    def createVeggie(self):
        return MushroomVeggie()

class Cheese(object):
    pass

class ReggianoCheese(Cheese):
    pass

class MozzarellaCheese(Cheese):
    pass

class Veggie(object):
    pass

class GarlicVeggie(Veggie):
    pass

class MushroomVeggie(Veggie):
    pass

nystore = NYPizzaStore()
nystore.orderPizza('cheese')
nystore.orderPizza('veggie')
chicagostore = ChicagoPizzaStore()
chicagostore.orderPizza('cheese')
chicagostore.orderPizza('veggie')
