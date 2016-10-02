// immutable objects
//   an object is immutable if its state can't be modified after it is created
//
// advantages
// 1) simpler to construct, test, and use
// 2) thread-safe
// 3) avoid temporal coupling
// 4) avoid side-effect free (no defensive copies)
// 5) avoid identity mutability problem
// 6) have failure atomicity
// 7) easier to cache
// 8) prevent NULL references
//
// in details:

// 2) thread-safe
//    1) multiple threads can access the same object at the same time, without clashing with another thread
//    2) no object methods can modify its state, so the object methods can be called in parallel
//       the object methods will work in their own memory space in stack

// 3) avoid temporal coupling
//    temporal coupling: there is some hidden information in the code that a programmer has to remember

// example:

// (bad design: mutable objects)

Request request = new Request("http://example.com");
request.method("POST");                               // this object state is set for both requests
String first = request.fetch();                       // first HTTP request
request.body("text=hello");                           // this object state is set for the second request
String second = request.fetch();                      // second HTTP request

// mutable objects create temporal coupling
// i.e. if you decide to remove the first HTTP request, we must remember not to remove 
//      request.method("POST")

Request request = new Request("http://example.com");
// request.method("POST");                                 // to remove the first request, we may remove
// String first = request.fetch();                         // two lines, which affects the second request
request.body("text=hello");
String second = request.fetch();

// the compiler won't complain, and the code just break

// (good design: immutable objects)

final Request request = new Request("http://example.com"); // an immutable object
String first = request.method("POST").fetch();             // first and second requests use separate objects
String second = request.method("POST").body("text=hello").fetch();

// removing either request won't affect the other, i.e. decoupling

// (futher improvement: get rid of code duplication)

final Request request = new Request("http://example.com"); // an immutable object
final Request post = request.method("POST");               // method() returns an immutable object
String first = post.fetch();                               // remove either request won't affect the other
String second = post.body("text=hello").fetch();

// 4) avoid side-effect free (no defensive copies)
//
// (bad design)

public String post(Request request) {
    request.method("POST");                 // the method changes the request object state (side effect)
    return request.fetch();
}

// the client code
Request request = new Request("http://example.com");
request.method("GET");
String first = this.post(request);          // calling post method has side effect
String second = request.fetch();

// (good design)

public String post(Request request) {       // the method should not change the request object state
return request.method("POST").fetch();      // method() returns an immutable object
}

// the client code
Request request = new Request("http://example.com").method("GET"); // an immutable object
String first = this.post(request);                                 // first request
String second = request.fetch();                                   // second request
/
// 5) avoid identity mutability problem
//
// example: 
//
// a common object identity check, by overloading the implementation of equals() and hashCode() methods
Date first = new Date(1L);
Date second = new Date(1L);
assert first.equals(second); // true, as the two objects have the same state

// what if the object is mutable
Date first = new Date(1L);
Date second = new Date(1L);
first.setTime(2L);           // the state of the first object is changed
assert first.equals(second); // should be false, as the two objects no longer have the same state

// what is the problem
Map<Date, String> map = new HashMap<>();
Date date = new Date();
map.put(date, "hello, world!"); // the object is added to the Map
date.setTime(12345L);           // the state of the object is changed
assert map.containsKey(date);   // cannot find the mutated object in the Map

// when we add an object to the map, its hashCode() returns one value
// the value is used by HashMap to place the entry into the internal hash table
// when we call containsKey() hash code of the object is different (because of its internal state) and
// HashMap can't find it in the internal hash table

// 6) have failure atomicity
 
// (bad design)

public class Stack {

    private int size;              // a mutalbe state
    private String[] items;

    public void push(String item) {
        size++;
        if (size > items.length) { // may throw Exception at run time if overflows
            throw new RuntimeException("stack overflow");
        }
        items[size] = item;
    }
}
// a mutable object will be left in a broken state if overflows
//
// failure atomicity: immutability prevents the problem
//   an immutable object will never be left in a broken state because its state is specified only in
//     its constructor
//   the constructor will either fail, rejecting object instantiation, or succeed, making a valid solid
//     immutable object, which never changes its encapsulated state

