// Flaw #2: Digging into Collaborators
// (Warning Signs)
//   Objects are passed in but never used directly (only used to get access to other objects)
//     should pass in the specific object you need as a parameter, instead of a holder of that object
//   Law of Demeter violation: method call chain walks an object graph with more than one dot (.)
//     avoid reaching into one object, to get another
//   Suspicious names: context, environment, principal, container, or manager
//
// why is it bad?
//   deceitful API: the API lies to you
//     declare in API (i.e. method signature/ object’s constructor) the collaborators you really need
//   makes for brittle code
//     if something needs to change, you have to dig around all these "Middle Men"
//     your code is longer and more confusing
//   hard for testing: complex fixture setup
//     need to create mocks that return mocks in tests
//
// FIXING THE FLAW
//   only talk to your immediate friends
//   inject (pass in) the more specific object that you really need
//   leave the object location and configuration responsibility to the caller
//
// rule of thumbs:
//   Don’t look for things; Ask for things!
//
// example 1: Service Object Digging Around in Value Object
//
// (bad design)

class SalesTaxCalculator {

    TaxTable taxTable;

    SalesTaxCalculator(TaxTable taxTable) {
        this.taxTable = taxTable;
    }

    float computeSalesTax(User user, Invoice invoice) {

        Address address = user.getAddress(); // object user is never used directly
        float amount = invoice.getSubTotal();
        return amount * taxTable.getTaxRate(address);
    }
}

// the test code: hard to test, needing much work for all the objects needed
class SalesTaxCalculatorTest extends TestCase {

    SalesTaxCalculator calc = new SalesTaxCalculator(new TaxTable());
    Address address = new Address("1600 Amphitheatre Parkway...");
    User user = new User(address);
    Invoice invoice = new Invoice(1, new ProductX(95.00));
    assertEquals(0.09, calc.computeSalesTax(user, invoice), 0.05);
}
// it is unclear that all that is needed is an Address and an Invoice: the API lies to you

// (good design)

class SalesTaxCalculator {

    TaxTable taxTable;

    SalesTaxCalculator(TaxTable taxTable) {
        this.taxTable = taxTable;
    }

    float computeSalesTax(Address address, float amount) { // asks for the specific objects it needs
        return amount * taxTable.getTaxRate(address);
    }
}

// the test code: easier to test
class SalesTaxCalculatorTest extends TestCase {

    SalesTaxCalculator calc = new SalesTaxCalculator(new TaxTable());
    Address address = new Address("1600 Amphitheatre Parkway...");
    assertEquals(0.09, calc.computeSalesTax(address, 95.00), 0.05);
}


// problem 2: Service Object Directly Violating Law of Demeter
//
// (bad design)

class LoginPage {

    RPCClient client;
    HttpRequest request;

    LoginPage(RPCClient client, HttpServletRequest request) {
        this.client = client;
        this.request = request;
    }

    boolean login() {
        String cookie = request.getCookie();                   // get another object from the passed-in object
        return client.getAuthenticator().authenticate(cookie); // get another object from the passed-in object
    }
}

// the test code: hard to test, difficult to mock
class LoginPageTest extends TestCase {

    public void testTooComplicatedThanItNeedsToBe() {

        Authenticator authenticator = new FakeAuthenticator();
        IMocksControl control = EasyMock.createControl();
        RPCClient client = control.createMock(RPCClient.class);
        EasyMock.expect(client.getAuthenticator()).andReturn(authenticator);
        HttpServletRequest request = control.createMock(HttpServletRequest.class);
        Cookie[] cookies = new Cookie[]{new Cookie("g", "xyz123")};
        EasyMock.expect(request.getCookies()).andReturn(cookies);
        control.replay();

        LoginPage page = new LoginPage(client, request);

        assertTrue(page.login());
        control.verify();
}
// the cookie is what we need, but we must dig into the request to get it

// (good design)

class LoginPage {

    LoginPage(@Cookie String cookie, Authenticator authenticator) { // pass in more specific objects
        this.cookie = cookie;
        this.authenticator = authenticator;
    }

    boolean login() {
        return authenticator.authenticate(cookie);
    }
}

// the test code: easier to test
class LoginPageTest extends TestCase {

    public void testMuchEasier() {

        Cookie cookie = new Cookie("g", "xyz123");
        Authenticator authenticator = new FakeAuthenticator();
        LoginPage page = new LoginPage(cookie, authenticator);
        assertTrue(page.login());
    }
}

// problem 3: Law of Demeter Violated to Inappropriately make a Service Locator
//
// (bad design)

class UpdateBug {

    Database db;

    UpdateBug(Database db) {
        this.db = db;
    }

    void execute(Bug bug) {
        db.getLock().acquire(); // digging around, violating Law of Demeter
        try {
            db.save(bug);
        } finally {
            db.getLock().release();
        }
    }
}
// db.getLock() is outside the single responsibility of the Database
// the Database is acting as a database, as well as a service locator (helping others to find a lock)

// the test code: hard to test, difficult to mock
class UpdateBugTest extends TestCase {

    public void testThisIsRidiculousHappyPath() {
        Bug bug = new Bug("description");

        IMocksControl control = EasyMock.createControl();
        Database db = control.createMock(Database.class);
        Lock lock = control.createMock(Lock.class);

        EasyMock.expect(db.getLock()).andReturn(lock); // this mock (db) returns another mock
        lock.acquire();
        db.save(bug);
        EasyMock.expect(db.getLock()).andReturn(lock);
        lock.release();
        control.replay();
        // finally, we're done setting up mocks

        UpdateBug updateBug = new UpdateBug(db);
        updateBug.execute(bug);
        control.verify();
    }
}

// (good design)

class UpdateBug {

    Database db;
    Lock lock;

    UpdateBug(Database db, Lock lock) {
        this.db = db;
        this.lock = lock;
    }

    void execute(Bug bug) {
        // as lock is passed in, the db no longer has a getLock method
        lock.acquire();
        try {
            db.save(bug);
        } finally {
            lock.release();
        }
    }
}

// State Based Testing: unit test is easier
//   asserts the state of objects after work is performed on them
//   it is not coupled to the implementation (the result is in the state as expected)
class UpdateBugStateBasedTest extends TestCase {

    public void testThisIsMoreElegantStateBased() {

        Bug bug = new Bug("description");

        InMemoryDatabase db = new InMemoryDatabase(); // use our in memory version instead of a mock
        Lock lock = new Lock();
        UpdateBug updateBug = new UpdateBug(db, lock);

        assertEquals(bug, db.getLastSaved()); // utilize State testing on the in memory db
    }
}

// Behavior Based Testing using mocks
//   uses mock objects to assert about the internal behavior of the System Under Test (SUT)
class UpdateBugMockistTest extends TestCase {

    public void testBehaviorBasedTestingMockStyle() {
        Bug bug = new Bug("description");

        IMocksControl control = EasyMock.createControl();
        Database db = control.createMock(Database.class);
        Lock lock = control.createMock(Lock.class);
        lock.acquire();
        db.save(bug);
        lock.release();
        control.replay();
        // two lines less for setting up mocks.

        UpdateBug updateBug = new UpdateBug(db, lock);
        updateBug.execute(bug);
    
        control.verify();
    }
}
// objects should have one responsibility and not act as a Service Locator for other objects

// problem 4: Object Called “Context” is a Great Big Hint to look for a Violation
//
// (bad design)

class MembershipPlan {

    void processOrder(UserContext userContext) {

        User user = userContext.getUser();
        PlanLevel level = userContext.getLevel();
        Order order = userContext.getOrder();
    }
}
// context objects may sound good in theory
//   i.e. no need to change signatures to change dependencies, can add parameters without changing signatures
//   but they are very hard to test
// API tells you a userContext object is needed, but you have no idea what that actually is 
//   API lies about its dependencies
//   it is hard to refactor the code, as users don’t know what parameters are really needed

// the test code: hard to test
public void testWithContextMakesMeVomit() {

    MembershipPlan plan = new MembershipPlan();
    UserContext userContext = new UserContext();
    userContext.setUser(new User("Kim"));
    PlanLevel level = new PlanLevel(143, "yearly");
    userContext.setLevel(level);
    Order order = new Order("SuperDeluxe", 100, true);
    userContext.setOrder(order);

    plan.processOrder(userContext);
}

// (good design)

class MembershipPlan {

    void processOrder(User user, PlanLevel level, Order order) { 

    }
}

// the test code: easier to test
public void testWithHonestApiDeclaringWhatItNeeds() {

    MembershipPlan plan = new MembershipPlan();
    User user = new User("Kim");
    PlanLevel level = new PlanLevel(143, "yearly");
    Order order = new Order("SuperDeluxe", 100, true);

    plan.processOrder(user, level, order);

}

// rule of thumbs:
//   expose true dependencies
//   it helps you discover how to decompose objects further to make an even better design
//
// WHEN THIS IS NOT A FLAW
//   Domain Specific Languages can violate the Law of Demeter for Ease of Configuration
//   i.e. building up a value object, in a fluent, easily understandable way
//
// example: A DSL may be an acceptable violation

bind(Some.class)
    .annotatedWith(Annotation.class)
    .to(SomeImplementaion.class)
    .in(SomeScope.class);

