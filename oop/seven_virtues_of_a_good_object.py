# Seven Virtues of a Good Object:
#
#  1) exists in real life: the object is its representative in a program
#     a) good objects:
#        ex. an employee, a department, an HTTP request, a table in MySQL, a row in MySQL, 
#            a line in a file, or a file itself
#     b) not good objects:
#        ex. a controller, a parser, a filter, a validator, a service locator, a singleton, or
#            a factory
#     c) improvement:
#        ex. class XMLparser => class parseableXML: a representative of an actual XML document
#
#  2) works by contracts: expect an object to do what the contract says
#                         i.e. focus on the contract the object obeys, not its origin class
#     ex. a contract that promises to give the binary content of an image
#
#         interface Binary {
#             byte[] read();
#         }
#
#         any object from any class that implements interface Binary can work for me
#     
#     rule of thumb: every public method in a good object should implement an interface
#     a) an object working without a contract is impossible to mock in a unit test
#     b) a contract-less object is impossible to extend via decoration
#
#  3) is unique: should always encapsulate something, ex. id, in order to be unique
#     if there is nothing to encapsulate, an object may have identical clones (bad) 
#
#     ex. a bad object
#
#         class HTTPStatus implements Status {
#
#             private URL page = new URL("http://www.google.com");
#
#             @Override
#             public int read() throws IOException {
#                 return HttpURLConnection.class.cast(
#                     this.page.openConnection()
#                 ).getResponseCode();
#             }
#         }
#
#         // not unique, all of them are equal to each other
#         first = new HTTPStatus();
#         second = new HTTPStatus();
#         assert first.equals(second);
#
#     not good objects:
#       utility classes, which have only static methods, are not good design
#
#  4) is immutable: should never change his encapsulated state
#     an object is a representative of a real-life entity: this entity should stay the same
#       through the entire life of the object
#     a good immutable object is very dynamic but never changes his internal state
#
#     ex. a good object
#
#         @Immutable
#         final class HTTPStatus implements Status {
#
#             private URL page;
#
#             public HTTPStatus(URL url) {
#                 this.page = url;
#             }
#
#             @Override
#             public int read() throws IOException {
#                 return HttpURLConnection.class.cast(
#                     this.page.openConnection()
#                 ).getResponseCode();
#             }
#         }
#
#         // the object is immutable but read() may return different values
#         // it points to a certain web page and will never point anywhere else
#
#     why immutable is good?
#     a) immutable objects are simpler to construct, test, and use
#     b) truly immutable objects are always thread-safe
#     c) help avoid temporal coupling
#     d) their usage is side-effect free (no defensive copies)
#     e) always have failure atomicity
#     f) much easier to cache
#     g) prevent NULL references
#     h) immutable objects force you to make more cohesive, solid, and understandable designs
#
#     no setters: this may change his state, i.e. no setURL()
#
#  5) doesn't have anything static
#     a static method implements a behavior of a class, not an object
#
#     ex. a good object
#
#         final class File implements Measurable {
#             @Override
#             public int size() {
#                // calculate the size of the file and return
#             }
#         }
#         // the contract Measurable ensures that the object implements size()
#
#         a bad object
#
#         class File {
#             public static int size(String file) {
#                 // calculate the size of the file and return
#             }
#         }
#
#         why it is bad design:
#         a) static methods turn object-oriented programming into class-oriented programming
#            the method, size(), exposes the behavior of the class, not of his objects
#         b) makes decomposition difficult
#            i)  class and the static methods are like global variables
#                whereas, objects are like local variables (in the scope of a method)
#            ii) scope decomposition is difficult
#                an object inside a method is dedicated to the specific task and isolated from all other objects
#                static methods of class cannot isolate its interaction with others
#         c) public static methods:
#            i)  impossible to mock them
#            ii) not thread-safe: they work with static variables, which are accessible from all threads
#
#  6) the name of an object is not a job (task) title
#     give the objects real, meaningful names instead of job titles
#     the name should tell us what it is, not what it does (just like we name objects in real life)
#     ex.
#       good           bad
#       -------------------------------
#       book    vs.    page aggregator
#       cup     vs.    water holder
#       T-shirt vs.    body dresser
#
#     rule of thumb: do not name objects that end with -er (exception: printer, computer, etc.)
#
#     a) good objects: the names should tell us who their owners are
#        ex. an apple, a file, a series of HTTP requests, a socket, an XML document, a list of users,
#            a regular expression, an integer, a PostgreSQL table, etc.
#     b) bad objects: the names should NOT tell what their owners do
#        ex. a file reader, a text parser, a URL validator, an XML printer, a service locator, a singleton,
#            a script runner, or a Java programmer
#     c) improvement:
#        (bad name)
#        class FileReader
#
#        we already have file representative, but we don't know how to read the content of the file
#
#        (good name)
#        class File: a representative of a real-world file on disk
#        class FileWithData (class DataFile): a file that has data that can be read
#
#  7) class is either final or abstract
#     final class: cannot be extended via inheritance
#                  i.e. a final class is a black box that cannot be modified by any means
#     abstract class: cannot be instanciated, i.e. cannot have objects
#
#     a) the only way to extend a final class is through decoration of his objects 
#        ex. if we want to extend the read() method of class HTTPStatus to throw an exception if 
#              the HTTP status is over 400
#            if we inherit the HTTPStatus class, we risk breaking the logic of the entire parent class by
#              overriding one of his method
#              i.e. we are literally injecting a new "piece of implementation" right into the class
#
#        solution: Decorator Pattern
#
#          // treat it like a black box and decorate it with your own implementation
#
#          final class OnlyValidStatus implements Status {
#
#              private final Status origin;
#
#              public OnlyValidStatus(Status status) {
#                  this.origin = status;
#              }
#
#              @Override
#              public int read() throws IOException {
#                  int code = this.origin.read();
#                  if (code > 400) {
#                      throw new RuntimException("unsuccessful HTTP code");
#                  }
#                  return code;
#              }
#          }
#
#        rule of thumb: a class without final is a bad design
#
#      b) an abstract class is the exact opposite case: it is incomplete and cannot instantiate any objects
#         we have to inject our custom implementation logic into it, but only into the places that it allows
#         i.e. the abstract methods
#
#         ex. 
#
#           abstract class ValidatedHTTPStatus implements Status {
#
#               @Override
#               public final int read() throws IOException {
#                   int code = this.origin.read();
#                   if (!this.isValid()) {
#                       throw new RuntimException("unsuccessful HTTP code");
#                   }
#                   return code;
#               }
#
#               protected abstract boolean isValid();
#           }
#
#           // the class does not know how exactly to validate the HTTP code, and it expects us to inject that
#           // logic through inheritance and through overloading the method isValid()
#
#      rule of thumb: a class should either be final or abstract (nothing in between)
