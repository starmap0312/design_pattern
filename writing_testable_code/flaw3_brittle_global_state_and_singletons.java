// Flaw #3: Brittle Global State & Singletons
// (Warning Signs)
//   Adding or using singletons
//     globally visible, introducing coupling
//   Adding or using "static" fields or "static" methods
//     globally visible, introducing coupling
//   Adding or using static initialization blocks
//     static init block gets run ONCE and are non-overridable by tests
//     it may cause some tests to fail, depending on the ordering of the tests
//   Adding or using registries
//   Adding or using service locators
//
// why is it bad?
//   accessing global state statically doesn’t clarify those shared dependencies to users of the 
//     constructors and methods
//   Global State and Singletons make APIs lie about their true dependencies
//   it introduces a certain amount of coupling into a system
//   unexpected state changes may happen in distant locations of the system which we did not tell the object
//   by hard-coding the dependency, we lose the power and flexibility of polymorphism
//     you cannot replace it with a different subtype
//   it prevents tests from being able to run in parallel
//     ideally, when a test completes, all state related to that test should disappear
//
// fixing the problem
//   favor dependency injection of the specific collaborators needed
//     i.e. every object that you need is declared in the API of its constructor
//     this also makes injecting test-doubles possible
//   often we don’t really need singletons (object creation is pretty cheap these days)
//   shared state object can be passed as collaborators to objects that needs it
//   if static object can not be removed, put it into an adapter class/object
//     then turning them from adapters into full fledged collaborators
//     the static access still exists, but it can be faked/mocked when testing
//
// from a behavior point of view, there is no difference between: (both are damaging)
//   a global variable declared directly through a static
//   a variable made global transitively
//
// example 0: a typical singleton implementation of Cache
//
// (bad design)

class Cache {

    static final instance Cache = new Cache(); // globally visible

    Map<String, User> userCache = new HashMap<String, User>(); // not private, so globally visible
    EvictionStrategy eviction = new LruEvictionStrategy();     // not private, so globally visible

    private Cache(){} // private constructor //..
}

// example 1: use of JVM singleton
//
// (bad design)

// definition of a singleton
class LoginService {

    private static LoginService instance;

    private LoginService() {};

    static LoginService getInstance() {
        if (instance == null) {
            instance = new RealLoginService();
        }
        return instance;
    }
}

// the client that uses the singleton
class AdminDashboard {

    boolean isAuthenticatedAdminUser(User user) {
        LoginService loginService = LoginService.getInstance(); // use of a singleton
        return loginService.isAuthenticatedAdmin(user);
    }
}

// the test code: forced to use the RealLoginService() for testing
class AdminDashboardTest extends TestCase {

    public void testForcedToUseRealLoginService() {

         assertTrue(adminDashboard.isAuthenticatedAdminUser(user));
    }
}
// as the dependency is hard-coded, this reduces the flexibility and testability
// tests cannot run in parallel, as they may use the shared global state

// (good design)

class LoginService {

  // removed the static instance
  // removed the private constructor
  // removed the static getInstance()
}

// the client
class AdminDashboard {

    LoginService loginService;

    AdminDashboard(LoginService loginService) { // use dependency injection instead
        this.loginService = loginService;
    }

    boolean isAuthenticatedAdminUser(User user) {
        return loginService.isAuthenticatedAdmin(user);
    }
}

// the test code: easier to test, passing in a test-doube of LoginService
class AdminDashboardTest extends TestCase {

    public void testUsingMockLoginService() {
        AdminDashboard dashboard = new AdminDashboard(new MockLoginService());
    }
}

// WHEN IS GLOBAL STATE OK?
//   when the reference is a constant and the object it points to is either primitive or immutable
//     ex. static final String URL = “http://google.com”;
//     but it is better to still wrap it in a class/object, so that it can be replaced when testing
//       hiding the constant information from the user can help testability
//       the object encapsulating the constant can be injected/replaced
//       the client does not need to know so much about the details
//   when the information only travels one way
//     ex. a Logger is one big singleton
//         the application does not behave differently based on what is or is not enabled in our logger
//         there is no need for the test to replace the Logger with a test-double

