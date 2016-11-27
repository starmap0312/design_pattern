# Inversion of Control
# - hollywood principle:
#   "don't call us, we'll call you"
# - when a client uses a service/resource (ex. database connection)
#   a) without the hollywood principle:
#      the client directly uses the service object and the two are tightly coupled 
#   b) with the hollywood principle:
#      the binding between the client and the service object is established at run-time
# - two classical examples:
#   a) dependency injection pattern
#      the dependences or callbacks can be injected to the client
#   b) service locator pattern
#      there exists a central registry class where the services
#      objects are registered at run-time (service look-up when needed)
# - relies on delegation:
#     an object delegates its stated task to an associated helper object
# - advantages:
#   a) allows the configuration of services/resources (ex. location of database) being 
#      kept in a separate configuration file
#   b) allows replacing the service/resource object easier, ex. by calling a setter
#      method, thus facilitating the unit-testing with a mock object
# - dependency injection vs. service locator:
#   a) dependency injection: set the service object in the Client class
#      the Client class uses the service without knowing which service implementation it is
#   b) service locator: set the service object in the ServiceLocator class, which is a
#      global entry
#      point to get specific service implementations; the client that uses the service objects
#      are somewhere else
#   c) the Client class in dependency injection is NOT a centralized service provider like the
#      ServiceLocator class in service locator
#   d) the service locator is NOT a client: it does not uses the service object but only
#      returns them

