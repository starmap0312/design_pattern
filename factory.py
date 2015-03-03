# Factory Method
# creational pattern: provides a way to decouple a client from the objects it creates
# class pattern: relationships between classes are established at compile time
# - an interface for creating objects, but let subclasses decide which to instantiate
# - superclass specifies generic behaviors and delegates the creation details to subclasses
# - often, design starts out using factory method, and evolve toward abstract factory,
#   prototype, or builder patterns, in order to achieve more flexibility
# - factory method -> creating objects vs. template method -> implementing an algorithm
# - factory method is not necessary when instances never change
# - factory method is similar to abstract factory without emphasis on families
# - an increasingly popular defintion of factory method is to declared it as static method in
#   the superclass, and it creates an instance of a subclass based on polymorphic creation (the 
#   parameter of the method),
#   it has the advantage of reusing existing objects, and can have more descriptive names, but
#   the disadvantage is that when a new type is added, you have to modify the static method
# - factory methods are usually called within template methods
# - factory methods encapsulate object creation and allows an object to be requested without
#   inextricable coupling to the act of creation

class PizzaStore(object):
    # factory method: a specialization of template method, product creation defers to subclasses
    # and an operation on the product is invariant and defined in superclass

    def createPizza(self, a_type):
        # factory method that create products and is implemented in subclasses
        raise NotImplementedError

    def orderPizza(self, a_type):
        # an operation on products
        pizza = self.createPizza(a_type)
        assert pizza is not None
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

class NYPizzaStore(PizzaStore):

    def createPizza(self, a_type):

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

    def createPizza(self, a_type):

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

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print 'baking %s' % self.name

    def cut(self):
        print 'cutting %s' % self.name

    def box(self):
        print 'boxing %s' % self.name

    def setName(self, name):
        self.name = name

class CheesePizza(Pizza):

    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        self.cheese = self.ingredientFactory.createCheese()
        self.veggie = None

class VeggiePizza(Pizza):

    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        self.cheese = None
        self.veggie = self.ingredientFactory.createVeggie()

# Abstract Factory
# creational pattern: provides a way to decouple a client and the objects it creates
# object pattern: relationships between classes are established at run time via composition
# - the client retire all references to 'new', and use the factory method of the factory
#   object to create products instead
# - decouples the client from the object it creates, insulating the client code from changes
# - adding new concrete types is done by modifying the client code to use a different factory,
#   which is typically one line in a file

class PizzaIngredientFactory(object):

    def createCheese(self):
        raise NotImplementedError

    def createVeggie(self):
        raise NotImplementedError

class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def createCheese(self):
        return ReggianoCheese()

    def createVeggie(self):
        return GarlicVeggie()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

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
