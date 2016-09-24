// Flaw #1: Constructor does Real Work
//   many designs are full of objects that instantiate other objects or retrieve objects from globally
//     accessible locations: they lead to highly coupled designs that are difficult to test
//
// (Warning Signs)
//   new keyword in a constructor or at field declaration
//     inflexible design: there is only one way to configure the class
//     this also shuts off the ability to inject test collaborators when testing
//       you are forced to use any heavyweight object instantiated in constructor
//   static method calls in a constructor or at field declaration
//     static calls are non-mockable, and non-injectable
//   control flow (conditional or looping logic) in a constructor
//     you have to successfully navigate the logic every time you instantiate the object
//   code does complex object graph construction inside a constructor rather than using a factory or
//   builder adding or using an initialization block
//     move the responsibility to other objects: ex. extract a builder, factory or provider, and pass
//     these collaborators to your constructor
//     do not create collaborators in your constructor, but pass them in (Don’t look for things! Ask for things!)
//   doing much work in a constructor
//     ex. anything more than field assignment in constructors
//     it violates the Single Responsibility Principle
//     if collaborators access external resources (e.g. files, network services, or databases), subtle
//       changes in collaborators may need to be reflected in the constructor, but constructor is
//       difficult to test
//   object not fully initialized
//     i.e. there is initialization that needs to happen with the objects that get passed in
//     delegate to another object who’s single responsibility is to configure the parameters for this object 
//     creating and configuring the collaborator is a different responsibility
//       pass in the created/configured collaborator to the constructor instead
//   object not fully initialized after the constructor finishes (watch out for initialize methods)
//
// note: constructing value objects may be acceptable in many cases
//   ex. LinkedList; HashMap, User, EmailAddress, CreditCard
//   they are trivial to construct, state focused, and do not refer to any service object
//
// rule of thumbs:
//   always think about how hard it will be to test the object while you are writing it
//     (need to easily construct the class with test-double collaborators)
//   do not create collaborators in your constructor, but pass them in
//
// example 1: instantiate collaborators at field declaration or class constructor
//
// (bad design)

class House {

    Kitchen kitchen = new Kitchen();  // instantiate a collaborator at field declaration
    Bedroom bedroom;

    House() {
        bedroom = new Bedroom();      // instantiate a collaborator at class constructor
    } 
}

// test code
class HouseTest extends TestCase {

    public void testThisIsReallyHard() {
        House house = new House();    // stuck with those Kitchen and Bedroom objects
    }
}

// (good design)

class House {

    Kitchen kitchen;
    Bedroom bedroom;

    House(Kitchen k, Bedroom b) {       // dependency injection, pass in as parameters into constructor
        kitchen = k;
        bedroom = b;
    }
}

// test code
class HouseTest extends TestCase {

    public void testThisIsEasyAndFlexible() {

        // use test doubles that are lighter weight
        House house = new House(new DummyKitchen(), new DummyBedroom());

    }
}

// example 2: configure collaborators at class constructor 
//
// (bad design)

class Garden {

    Garden(Gardener joe) {
        joe = joe.withWorkday(new TwelveHourWorkday());
        joe = joe.withBoots(new BootsWithMassiveStaticInitBlock());
        this.joe = joe;
    }
}

// the test code
class GardenTest extends TestCase {

    public void testMustUseFullFledgedGardener() {

        Gardener gardener = new Gardener();
        Garden garden = new Garden(gardener);

        assertTrue(gardener.isWorking());
    }
}

// (good design)

class Garden {

    Gardener joe;

    Garden(Gardener joe) {
        this.joe = joe;
    }
}

// the test code
class GardenTest extends TestCase {

    public void testUsesGardenerWithDummies() {

        Gardener gardener = new Gardener()
            .withWorkday(new OneMinuteWorkday())
            .withBoots(null);
        Garden garden = new Garden(gardener);
        assertTrue(gardener.isWorking());
    }
}

// example 3: violates the Law of Demeter
//
// (bad design)

class AccountView {

    User user;

    AccountView() {
        user = RPCClient.getInstance().getUser(); // creating excessive dependencies
    }
}
// cannot easily intercept the call RPCClient.getInstance() to return a mock RPCClient for testing

// the test code: hard to test because needs real RPCClient
class ACcountViewTest extends TestCase {

    public void testUnfortunatelyWithRealRPC() {

        AccountView view = new AccountView();

    }
}

// (good design)

class AccountView {

    User user;

    AccountView(User user) { // the class only wants the User
        this.user = user;
    }
}

// the test code: easy to test with test-double
class AccountViewTest extends TestCase {

    public void testLightweightAndFlexible() {

        User user = new DummyUser();
        AccountView view = new AccountView(user);

    }
}

// example 4: creating unneeded third party objects in constructor
//
// (bad design)

class Car {

    Engine engine;

    Car(File file) {
        String model = readEngineModel(file);
        engine = new EngineFactory().create(model); // depends on a third-party object
    }
}
// depends on non-injectable and non-overridable creation third-part objects

// the test code
class CarTest extends TestCase {

    public void testNoSeamForFakeEngine() {
        File file = new File("engine.config");      // ties to the slow file system
        Car car = new Car(file);
  }
}

// (good design)

class Car {

    Engine engine;

    Car(Engine engine) { // pass in precisely what it needs, delegate the construction to other objects
        this.engine = engine;
    }
}

// the test code
class CarTest extends TestCase {

    public void testShowsWeHaveCleanDesign() {

        Engine fakeEngine = new FakeEngine();
        Car car = new Car(fakeEngine); // testing is easier
    }
}

// example 5: directly reading flag values in constructor
//
// (bad design)
class PingServer {

    Socket socket;

    PingServer() { //  the API is lying to you, pretending it is easy to create
        socket = new Socket(FLAG_PORT.get());
    }
}

// the test code
class PingServerTest extends TestCase {

    public void testWithDefaultPort() {
        PingServer server = new PingServer();
    }
}

// (good design)
class PingServer {

    Socket socket;

    PingServer(Socket socket) { // pass in the socket that is ultimately needed (or at least a port number)
        this.socket = socket;
    }
}

// the test code
class PingServerTest extends TestCase {

    public void testWithNewPort() {
        int customPort = 1234;
        Socket socket = new Socket(customPort);
        PingServer server = new PingServer(socket); // test is easier as we can use a mock socket
  }
}
