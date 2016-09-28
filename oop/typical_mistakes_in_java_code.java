// Typical Mistakes in Java Code
//
// Class Names
//   Don't Create Objects That End With -ER
//     ex. validators, controllers, managers, etc.
//   utility classes are anti-patterns
//     ex. StringUtils, FileUtils, and IOUtils, etc.
//   the name indicates what they are, not what they do, i.e. problem/domain oriented, not solution oriented
//   never add suffixes or prefixes to distinguish between interfaces and classes
//     ex. IRecord, IfaceEmployee, or RecordInterface, etc.
//   * interface name is the name of real-life entity, while class name explains its implementation details
//   * if there is nothing specific to say about an implementation, name it Default, Simple, etc.
//     ex. class SimpleUser implements User {};
//         class DefaultRecord implements Record {};
//         class Suffixed implements Name {};
//         class Validated implements Content {};
//
// Method Names
//   methods can either return something or return void
//   * if a method returns something, then its name should explain "what" it returns (but never use "get" prefix)
//     ex. boolean isValid(String name);
//         String content();
//         int ageOf(File file);
//   * if a method returns void, then its name should explain "what" it does
//     ex. void save(File file);
//         void process(Work work);
//         void append(File file, String line);
//   there is only one exception: test method names
//
// Test Method Names
//   English sentences without spaces
//         /**
//          * HttpRequest "can" return its content in Unicode.
//          * @throws Exception If test fails
//          */
//     ex. @Test
//         public void returnsItsContentInUnicode() throws Exception {
//
//         }
//         the "can" keyword in the comments is important, always states "somebody can do something"
//         always declare test methods as throwing Exception
//
// Variable Names
//   avoid composite names of variables, including class variables and in-method variables
//     ex. timeOfDay, firstItem, or httpRequest, etc.
//   variable name should avoid ambiguity in its scope of visibility, but not too long if possible
//   * a name should be a noun in singular or plural form, or an appropriate abbreviation
//     ex. List<String> names;
//         void sendThroughProxy(File file, Protocol proto);
//         private File content;
//         public HttpRequest request;
//   if constructor parameter names and in-class propertie names collide, then
//     create abbreviations by removing vowels
//     ex. public class Message {
//
//             private String recipient;
//
//             public Message(String rcpt) {
//
//                 this.recipient = rcpt;
//             }
//         }
//   you can also use an adjective, when there are multiple variables with different characteristics
//     ex. String contact(String left, String right);
//
// Constructors
//  there should be only one primary constructor that stores data in object variables
//  ex. public class Server {
//
//          private String address;
//
//          public Server(String uri) { // primary constructor
//              this.address = uri;
//          }
//
//          public Server(URI uri) { // secondary constructor
//              this(uri.toString());
//          }
//      }
//
// One-time Variables
//   avoid one-time variables as much as possible
//     ex. String name = "data.txt";    // bad design
//         return new File(name);
//
//         return new File("data.txt"); // good design
//
// Redundant Constants
//   * Class constants should be used when you want to share information between class methods and this
//       information is a characteristic of the class
//     ex. class Document {
//
//             private static final String D_LETTER = "D"; // bad practice
//             private static final String EXTENSION = ".doc"; // good practice
//         }
//   Constants should have a meaning in a real world
//     never use constants just for a replacement of string or numeric literals 
//   don't use constants in unit tests to avoid duplicate string/numeric literals in test methods
//
// Test Data Coupling
//   ex. User user = new User("Jeff");
//       (some other code here)
//       MatcherAssert.assertThat(user.name(), Matchers.equalTo("Jeff"));
//   avoid this data coupling by introducing a variable

