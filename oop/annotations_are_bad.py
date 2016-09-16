# annotations are bad
#   they encourage us to implement object functionality outside of an object (violate encapsulation principle)
#     we move functionality outside of our objects and put it into containers, or somewhere else
#   they tear objects apart and keeping parts in different places
#     ex. containers, sessions, managers, controllers
#
#
# example: @Inject
#
# (bad design)
#
#   // annotate a property with @Inject
#   import javax.inject.Inject;
#   public class Books {
#
#       @Inject
#       private final DB db;
#
#       // some methods here, which use this.db
#   }
#
#   // have an injector that knows what to inject
#   Injector injector = Guice.createInjector(
#       new AbstractModule() {
#           @Override
#           public void configure() {
#               this.bind(DB.class).toInstance(new Postgres("jdbc:postgresql:5740/main"));
#           }
#       }
#   );
#
#   // make an instance of class Books via the container
#   Books books = injector.getInstance(Books.class);
#
# why is it bad?
#   the class Books has no idea how and who will inject an instance of class DB into it
#     it happens behind the scenes and outside of its control
#     the object can't be responsible for what's happening to it
#
# (good design)
#
#   // dependency injection via constructors
#   class Books {
#
#       private final DB db;
#
#       Books(final DB base) {
#           this.db = base;
#       }
#       // some methods here, which use this.db
#   }
#
#
# example: @XmlElement
#
# (bad design)
#
#   import javax.xml.bind.annotation.XmlElement;
#   import javax.xml.bind.annotation.XmlRootElement;
#
#   @XmlRootElement
#   public class Book {
#
#       private final String title;
#
#       public Book(final String title) {
#           this.title = title;
#       }
#
#       @XmlElement
#       public String getTitle() { // attach the @XmlElement annotation to the getter
#           return this.title;
#       }
#   }
#   
#   // the client code
#   // create a marshaller and ask it to convert an instance of class Book into XML
#   final Book book = new Book("0132350882", "Clean Code");
#   final JAXBContext context = JAXBContext.newInstance(Book.class);
#   final Marshaller marshaller = jaxbContext.createMarshaller();
#   marshaller.marshal(book, System.out);
#
# why is it bad?
#   1) it is not the book instance that creates the XML. it's someone else, outside of the class Book
#   2) the control is lost (not inverted, but lost!)
#   3) the object is not in charge any more: it can't be responsible for what's happening to it
#   
#   
# (good design: use decorators instead)
#
#   // the basic class has no idea about XML
#   class DefaultBook implements Book {
#
#       private final String title;
#
#       DefaultBook(final String title) {
#           this.title = title;
#       }
#
#       @Override
#       public String getTitle() {
#           return this.title;
#       }
#   }
#   
#   // the decorator adds an additional functionality/method of printing title to XML format
#   class XmlBook implements Book {
#
#       private final Book origin;
#
#       XmlBook(final Book book) {
#           this.origin = book;
#       }
#
#       @Override
#       public String getTitle() {  // the decorater does not decorate the method, simply delegate
#           return this.origin.getTitle();
#       }
#
#       public String toXML() {     // a new functionality (method)
#           return String.format(
#               "<book><title>%s</title></book>",
#               this.getTitle()
#           );
#       }
#   }
#   
#   // the client code
#   String xml = new XmlBook(
#       new DefaultBook("Elegant Objects")
#   ).toXML();
#
# why is it good?
#   1) the XML printing functionality is inside XmlBook
#      i.e. the functionality always stays where it belongs (inside the object)
#   2) only the object knows how to print itself to the XML. nobody else
#
# (bad design: use extends)
#   there is a small difference with using inheritance, i.e. extends the DefaultBook
#
#   // XmlBook inherits DefaultBook's getTitle() method and extends an extra funcationailty: toXML()
#   class XmlBook extends DefaultBook {
#
#       public String toXML() {     // a new functionality (method)
#           return String.format(
#               "<book><title>%s</title></book>",
#               this.getTitle()
#           );
#       }
#   }
#
#   // the client code
#   String xml = new XmlBook("Elegant Objects").toXML();
#
# why is it bad?
#   class XmlBook does not code to the interface, but rather a concrete class
#     whatever changes to DefaultBook may affect XmlBook
#   never use extends, use decorator class, no matter it is to add an additional responsibility/method to a class,
#     to decorate/enhance a class's responsibility/method
#
# (another good design: let the class has one more responsibilities)
#
#   // move the toXML() method to the DefaultBook class, the class has two responsibilites
#   class DefaultBook implements Book {
#
#       private final String title;
#
#       DefaultBook(final String title) {
#           this.title = title;
#       }
#
#       public String getTitle() {
#           return this.title;
#       }
#
#       public String toXML() {
#           return String.format(
#               "<book><title>%s</title></book>",
#               this.getTitle()
#           );
#       }
#
#   }
#
# why is it good?
#   the functionality always stays where it belongs (inside the object)
#   only the object knows how to print itself to the XML
#   consider to use decorator class when the functionalities grow
#
#
# example: @RetryOnFailure
#
# (bad design)
#
#   import com.jcabi.aspects.RetryOnFailure;
#
#   // annotates an object's method
#   class Foo {
#
#       @RetryOnFailure
#       public String load(URL url) {
#           return url.openConnection().getContent();
#       }
#   }
#
#   // the annotation technically turns the code into this
#   class Foo {
#
#       public String load(URL url) {
#           while (true) {                 // infinite-loop for the retry functionality
#               try {
#                   return _Foo.load(url);
#               } catch (Exception ex) {
#                   // ignore it
#               }
#           }
#       }
#
#       class _Foo {                       // 
#           public String load(URL url) {
#               return url.openConnection().getContent();
#           }
#       }
#   }
#
# why is it bad?
#   we don't see and don't control the instantiation of that supplementary object
#   we must see how our objects are composed: object composition is hidden somewhere behind the scenes
#
# (good design: use decorator class)
#
#   class FooThatRetries implements Foo {
#
#       private final Foo origin;
#
#       FooThatRetries(Foo foo) {
#           this.origin = foo;
#       }
#
#       public String load(URL url) {
#           return new Retry().eval(
#               new Retry.Algorithm<String>() {
#                   @Override
#                   public String eval() {
#                       return FooThatRetries.this.load(url);
#                   }
#               }
#           );
#       }
#   }
#
#   // the client code
#   Foo foo = new FooThatRetries(new Foo());
#
# why is it good?
#   we can see the entire composition process
