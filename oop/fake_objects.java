// mocking is evil
//   the reponsibility of an object might be too complex, which makes mocking difficult
//     i.e. methods return other objects, which also have methods
//          when we use a mock for the object, we need all of its methods return valid objects 
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

// it is difficult to mock such a complex object
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

// the client code which uses a Region object
public class Employee {

    private final String name;
    private final Region region;

    public Employee(String empl, Region dynamo) {
        this.name = empl;
        this.region = dynamo;
    }

    public Integer salary() {      // this is the method that we want to test
        return Integer.parseInt(
            this.region            // the production/fake object need to support these methods/operations
                .table("employees")
                .frame()
                .where("name", this.name)
                .iterator()
                .next()
                .get("salary")
                .getN()
        );
    }
}

// the preparation step for mocking a complex object is difficult
// the unit test code will be much longer than the client class itself
//
// (good design: create fake objects and  and ship them together with client classes)

// create a fake class MkRegion

// the test class utilizes the fake object
public class EmployeeTest {

    public void canFetchSalaryFromDynamoDb() {
        Region region = new MkRegion(  // instantiate the fake object which works on H2Data (in-memory H2 database)
            new H2Data().with("employees", new String[] {"name"}, new String[] {"salary"})
        );
        region.table("employees").put( // create the test data, i.e. a table record
            new Attributes().with("name", "Jeff").with("salary", new AttributeValue().withN(50000))
        );
        Employee emp = new Employee("Jeff", region); // construct the object to be tested with the fake object
        assertThat(emp.salary(), equalTo(50000))     // test it's salary() method
    }
}
