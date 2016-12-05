// temporal coupling between method calls
//   sequential method calls must stay in a particular order
//     i.e. there is some hidden information in the code that a programmer has to remember
//   inevitable in imperative programming
//
// example: converting multiple strings into lowercase and adding them to a list in order
//
// (bad design: a procedural design which leads to temporal coupling)

class Foo {

    public List<String> names() { // creating a list of names with lowercases 
        List<String> list = new LinkedList();
        list.add("Jeff".toLowerCase());
        list.add("Walter".toLowerCase());
        return list;
    } // the statements must stay in this order, i.e. coupled together
}

// (refinement: use a static method to avoid code duplication)

class Foo {

    public List<String> names() { 
        List<String> list = new LinkedList();
        Foo.append(list, "Jeff");   // use a static method avoid code duplication 
        Foo.append(list, "Walter"); // use a static method avoid code duplication 
        return list;
    }

    //a static method for converting the string to lowercase and adding to list
    private static void append(List<String> list, String item) { // 
        list.add(item.toLowerCase());
    }
}

// what is the problem?
//
// ex. 10 months later, we may put more code around them

class Foo {

    public List<String> names() {
        List<String> list = new LinkedList();
        // 10 more lines here
        Foo.append(list, "Jeff");   // not certain if the line can be removed, as the lines are coupled together
        Foo.append(list, "Walter"); // the knowledge about the order are hidden inside the body of append method
        // 10 more lines here
        return list;
    }
}
// if we want to remove the line Foo.append(list, "Jeff"), we need to check the body of append() method
// see if it will affect the result returned in the last line

// the code may be further refactored by others as follows

class Foo {

    public List<String> names() {
        List<String> list = new LinkedList();
        if (/* something */) { // not sure if the list can be returned before the two append method calls
            return list;
        }
        // 10 more lines here
        Foo.append(list, "Walter"); // not certain if the order of appending the two words can be changed 
        Foo.append(list, "Jeff");
        // 10 more lines here
        return list;
    }
}

// if we want to return list before the two append() calls, we need to check the body of append() methods
//
// why is it bad?
//   temporal coupling: the lines are coupled together
//   they must stay in this particular order, but the knowledge about that order is hidden
//   it is easy to destroy the order, and our compiler won't be able to detect that 
//
// (good design: let the static method return results, which can become arguments to further calls)

class Foo {

    public List<String> names() {
        // the method contains only one line, thus no line order dependency
        return Foo.with(Foo.with(new LinkedList(), "Jeff"), "Walter");
    }

    // the method converts the string into lowercase, adds the string to the list, and returns the list 
    private static List<String> with(List<String> list, String item) {
        list.add(item.toLowerCase());
        return list;
    }
}

// why is it good?
//   no temporal coupling: an ideal method in OOP havs one single statement, (a return statement)
//
// (better desing: use decorator class)

class MyAddition(ListInterface) {

    MyAddition(List<String> list) { // MyAddition decorates the List<String> class
        this.list = list;
    }

    public List<String> add(String item) {
        list.add(item.toLowerCase());
        return list;
    }
}

// the client code has only one line
MyAddition(MyAddition(new LinkedList()).add("Jeff")).add("Walter");


// another example: adding strings to a list with enough space validation
//
// (bad design: use a static method for list validation)

list = MyAddition(new LinkedList());
list = list.add("Jeff");                     // the lines are coupled together
Foo.checkIfListStillHasSpace(list);   // one needs to check the body of the methods to refactor the code
list = list.add("Walter");
return list;
// the lines are coupled, the order is important

// (good design: let the static method takes list as arugemnt and returns the list after the validation)

list = MyAddition(new LinkedList());
list = list.add("Jeff");
list = Foo.withEnoughSpace(list).add("Walter");  // the last two lines are combined together
return list;

// (better design: use decorator class for validation)
// because static methods are evil, we can replace static methods with composable decorators

list = MyAddition(new LinkedList());
list = list.add("Jeff");
list = WithEnoughSpace(list).add("Walter");
return list
// WithEnoughSpace decorates add() method by validating if there is enough space before adding the string

// the above three lines can be consolidated to one line
return WithEnoughSpace(MyAddition(new LinkedList()).add("Jeff")).add("Walter");

//
// rule of thumbs:
//   a) an ideal method in OOP must has one single return statement
//   b) use composable decorators, not static methods
//      if we have to use static methods, don't make those static methods look like procedures 
//      make sure they always return results, which become arguments to further calls
//
//
// another example: making two consecutive HTTP POST requests, where the second one contains HTTP body
//
// (bad design)

Request request = new Request("http://example.com");
request.method("POST");          // both requests need the POST method setting (mutable object)
String first = request.fetch();  // making the first request
request.body("text=hello");      // the second request has the HTTP body
String second = request.fetch(); // making the second request
// temporal coupling: there is some hidden information the programmer needs to know
//   i.e. the first request should be configured before the second one may happen

Request request = new Request("http://example.com");
// request.method("POST");         // the method configuration of first request is also used for the second one
// String first = request.fetch(); // removing the first request code completely will cause problem
request.body("text=hello");
String second = request.fetch();

// (good design: decouple the two request statements)

final Request request = new Request("");
String first = request.method("POST").fetch();   // can safely remove the first request
String second = request.method("POST").body("text=hello").fetch();
// but there is a code duplication of method("POST")

// (better design: avoid code duplication)

final Request request = new Request("");
final Request post = request.method("POST");     // returns a new immutable Request object
String first = post.fetch();                     // can safely remove the first request
String second = post.body("text=hello").fetch(); // body() returns a new immutable Request object
// immutablity of objects helps avoid temporal coupling

