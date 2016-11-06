// mocking is evil
// if the class is too complex, mocking is difficult and a waste
//   ex. methods return other objects, which also have methods
//       when we use a mock for the object, we need all of its methods return valid objects 
//
// example: mocking a complex object
//
// (bad design: use mock)
//
// interface of a complex object: it's table() method returns another object

public interface Region {
    Table table(String name);
}

// that object's frame(), put() and region() methods also return other objects

public interface Table {
    Frame frame();
    Item put(Attributes attrs);
    Region region();
}

// it is difficult to mock such a complex object and usually a waste of time
public void testMe() {
    // many more lines here...
    Frame frame = Mockito.mock(Frame.class);      // need to mock Frame object
    Mockito.doReturn(...).when(frame).iterator(); // Frame's iterator() method may return something
    Table table = Mockito.mock(Table.class);      // need to mock Table object
    Mockito.doReturn(frame).when(table).frame();  // Table's frame() method needs to return Frame object
    Region region = Mockito.mock(Region.class);   // need to mock Region object
    Mockito.doReturn(table).when(region).table(Mockito.anyString());
                                                  // Region's table() method needs to return Table object
}

// the client code of Region object
public class Employee {

    private final String name;
    private final Region region;

    public Employee(String empl, Region dynamo) {
        this.name = empl;           // the object's characteristic
        this.region = dynamo;       // a collaborator
    }

    public Integer salary() {       // this is the method that we want to test
        return Integer.parseInt(
            this.region             // the production/fake object need to support these methods/operations
                .table("employees") // return a Table object
                .frame()            // return a Frame object
                .where("name", this.name)
                .iterator()
                .next()
                .get("salary")
                .getN()
        );
    }
}

// mocking a complex object is difficult: the unit test code may be longer than the client class itself
// the solution:
//   create fake classes, ex. MkRegion, and ship them together with real classes
//
// (good design: use fake objects instead and ship them together with client classes)
//
// the testing code with a fake object
public class EmployeeTest {

    public void canFetchSalaryFromDynamoDb() {
        Region region = new MkRegion(  // instantiate fake object which works on H2Data (in-memory H2 database)
            new H2Data().with("employees", new String[] {"name"}, new String[] {"salary"})
        );
        region.table("employees").put( // insert the testing data into the table
            new Attributes().with("name", "Jeff").with("salary", new AttributeValue().withN(50000))
        );
        Employee emp = new Employee("Jeff", region); // instantiate the object to be tested with the fake object
        assertThat(emp.salary(), equalTo(50000))     // test if it's salary() method matches our expectation
    }
}
