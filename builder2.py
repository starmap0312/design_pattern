class Pizza(object):
    # a product

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
    # an abstract builder

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
    # a concreate builder

    def buildDough(self):
        self.pizza.setDough('cross')

    def buildSauce(self):
        self.pizza.setSauce('mild')

    def buildTopping(self):
        self.pizza.setTopping('ham and pineapple')

class SpicyPizzaBuilder(PizzaBuilder):
    # a concreate builder

    def buildDough(self):
        self.pizza.setDough('pan baked')

    def buildSauce(self):
        self.pizza.setSauce('hot')

    def buildTopping(self):
        self.pizza.setSauce('pepperoni and salami')

class Waiter(object):
    # a director, the sequence of construction steps is fixed, so we write 
    # a template to construct the product, this ensures that the product is always constructed
    # based in the same process

    def setPizzaBuilder(self, pizzaBuilder):
        self.pizzaBuilder = pizzaBuilder

    def getPizza(self):
        return self.pizzaBuilder.getPizza()

    def constructPizza(self):
        self.pizzaBuilder.createPizza()
        self.pizzaBuilder.buildDough()
        self.pizzaBuilder.buildSauce()
        self.pizzaBuilder.buildTopping()

waiter = Waiter()
hawaiianPizzaBuilder = HawaiianPizzaBuilder()
waiter.setPizzaBuilder(hawaiianPizzaBuilder)
waiter.constructPizza()
pizza = waiter.getPizza()
print '(%s, %s, %s)' % (pizza.dough, pizza.sauce, pizza.topping)
spicyPizzaBuilder = SpicyPizzaBuilder()
waiter.setPizzaBuilder(spicyPizzaBuilder)
waiter.constructPizza()
pizza = waiter.getPizza()
print '(%s, %s, %s)' % (pizza.dough, pizza.sauce, pizza.topping)

