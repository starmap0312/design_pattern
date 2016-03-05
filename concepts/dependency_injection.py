# Dependency Injection
# - a dependency (a service implementation) is an object that can be used by a client
#   the injection is the passing of a dependency (service) to a dependent object (client)
# - the pattern embodies the following principles:
#   a) follows "single responsibility principle" by separating the creation of a client's 
#      dependencies (service objcets) from the client's behaviors
#      (improves code readability: easier to read the Client class)
# - b) follows "dependency inversion principle" by creating an abstraction class, i.e. Service
#      class, for resolving dependencies (the client and service objects are loosely coupled)
#      (improves code reusability: easier to reuse the Client class)
# - c) follows "hollywood principle" (inversion of control) by creating the Injector class that 
#      injects the service object into the client
#      (imporves code testability: able to test the Client class)
# - dependency graph:
#   i.e.                 (HAS_A)          (IS_A)                (HAS_A)
#                Client  ......> Service <------ ServiceExample <...... Injector
#                   ^     uses                                  constructs |
#                   |......................................................| (HAS_A)
#                                           injects
#
# - 4 roles in the above dependency injection framework:
#   a) the service objects to be used (ServiceExample)
#   b) the client object (Client) which depends on the service it uses (Service)
#   c) the injector (Injector), responsible for constructing the service object (ServiceExample)
#      and injecting it into the client (Client)
#   d) the interface (Service) that defines how the client (Client) may use the service 
#      object (ServiceExample)
# - the client does not construct the service itself. instead, it delegates the responsibility
#   to external code (the injector/service provider); this goal is similar to that of using a 
#   factory, but different in that the client is injected into a service object not querying
#   a factory method to get the object
# - the client only needs to know the interface of the service object, i.e. the Service inverface,
#   which specifies how to use the service object; this makes the Client configurable to 
#   different service objects at run-time, through a separate configuration file
#
# - there are 3 ways to implement the pattern:
#   a) constructor-based injection
#   b) setter-based injection
#   c) interface-based injection
#
#   examples:
#   1. the Client without dependency injection:
#     the client constructs and uses the service object all by itself, not following the
#     dependency inversion principle, i.e. higher-level module (Client) depends on lower-level 
#     module (ServiceExample) directly
#
#   public class Client {
#
#       private Service service;
#
#       Client() {
#           this.service = new ServiceExample(); // construct the Service implementation itself
#       }                                        // Client depends on ServiceExample
#
#       public String greet() {
#           return "Hello " + service.getName(); // use the servie object
#       }
#   }
#
#   2. the Client with dependency injection:
#     the client removes all knowledge of the service object, ServiceExample, following the
#     dependency inversion principle, i.e. higher-level module (Client) does not depend on
#     lower-level module (ServiceExample)
#     instead, both Client and ServiceExample depend on an abstract class (Service)
#     in other words, Client class and ServiceExample class are loosely coupled, which increases
#     the re-usability of the Client code (the Client isolates itself from the impact of code 
#     changes that may happen in ServiceExample)
#
#   a) constructor injection
#     the injector may pass a reference to the service object via the client's constructor
#
#   public class Client {
#
#       Client(Service service) {
#           this.service = service;              // Injector should pass in a reference to 
#       }                                        // ServiceExample via the constructor
#
#       public String greet() {
#           return "Hello " + service.getName(); // Client can use the servie object
#       }
#   }
#
#   b) setter injection
#     the injector may pass a reference to the service object via the client's setter method
#
#   public class Client {
#
#       private Service service;
#
#       public void setService(Service service) {
#           this.service = service;              // Injector should pass in a reference to
#       }                                        // ServiceExample via this setter method
#
#       public String greet() {
#           return "Hello " + service.getName(); // Client can use the servie object
#       }
#   }
#
#   c) interface injection
#     an interface of the Client that tells the Injector how it can inject the dependencies
#
#   public interface ClientInterface {
#       public void setService(Service service);
#   } // let the Injector know that the Client has a setService method, using which the Injector
#     // can pass in the service object, i.e. ServiceExample
#
#   public class Client implements ClientInterface {
#
#       private Service service;
#
#       @Override
#       public void setService(Service service) {
#           this.service = service;              // Injector should pass in a reference to
#       }                                        // ServiceExample via this setter method
#
#       public String greet() {
#           return "Hello " + service.getName(); // Client can use the servie object
#       }
#
#   3. the Injector:
#   3.1 assembling in the main method of the injector class
#   // it has a purely construction-only relationship with ServiceExample but mixes construction
#   // and using of client object; this is not common but unavoidable, as a dependency injected
#   // object graph needs at least one (preferably only one) entry point to get the using started
#
#   public class Injector {
#       public static void main(String[] args) {
#           Service service = new ServiceExample(); // construct the service object
#           ClientInterface client = new Client();
#           client.setService(service);             // inject the service object to the
#                                                   // Client via its setter method
#           System.out.println(client.greet());     // use the client object (can be anywhere else)
#       } 
#   }
#
# - dependency graph
#   1. the Client without dependency injection: 
#     Client & ServiceExample are tightly coupled
#
#                 (HAS_A)
#      Client .................> ServiceExample
#              construct & use
#
#   2. the Client with dependency injection:
#     follow the dependency inversion principle: add an abstract class (Service)
#     follow the single responsibility principle: add another class (Injector) responsible for
#     the construction and injection of the service object (ServiceExample)
#
#                         (HAS_A)           (IS_A)                  (HAS_A)
#                Client  ........> Service <------- ServiceExample <........ Injector
#                   ^       uses                                   constructs     |
#                   |.............................................................| (HAS_A)
#                                               injects
#
# - advantages:
#   1. increases the reusability of the client code
#   2. increases the testability of the client code, as the injector can pass in a mock object
#      for unit testing
#      ex. the client uses the database service: the injector can pass in a mock object that
#          that simulates the database functionalities
#   3. increases the configurability of the client, as the injector can read in a separate
#      configuration file and pass different service objects to the client
#      (the client could act on anything that supports the interface that the client expects)
#      ex. in system configuration, a system's configuration details are separated into
#          the configuration files, and the system can be reconfigured without recompilation
#   4. two developers can independently develop the Client and ServiceExample classes, as they
#      are loosely coupled (the changes in either class do not affect the other)
#
# - disadvantages:
#   1. increases the code complexity: as it separates behavior (in client) from construction 
#      (in injector)
#   2. requires more development effort: not as straightfoward as the client directly using 
#      a service object right after it is constructed and where it is constructed

class Service(object):
    # an abstract class: both higher-level module (Client) and lower-level module (ServiceExample)
    # depend on this abstract class

    pass

class ServiceExample(Service):
    # a concrete implementation of the Service class

    def getName(self):
        return "ServiceExample"

class ClientInterface(object):
    # an interface that shows how the Injector class should talk to the Client when injecting
    # dependencies (service objects)

    def setService(self, service):
        raise NotImplementedError

class Client(ClientInterface):
    # a client class that uses the injected service object

    def __init__(self):
        self.service = None

    def setService(self, service):
        self.service = service

    def greet(self):
        return "Hello " + self.service.getName() # use of the service object

class Injector(object):
    # an injector class: the construction of the service object is defined in this class
    # and the service object is injected into a client object here

    def __init__(self):
        self.client = Client()
        self.client.setService(ServiceExample()) # inject the service object into the client

    def greet(self):
        print self.client.greet()                # use the client object (doesn't need to be here)
                                                 # the client object can be used anywhere else
injector = Injector()
injector.greet()
