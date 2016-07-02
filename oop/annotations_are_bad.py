# annotations are bad
#
# example: Java @XmlElement
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
#   // the client code: create a marshaller and ask it to convert an instance of class Book into XML
#   final Book book = new Book("0132350882", "Clean Code");
#   final JAXBContext context = JAXBContext.newInstance(Book.class);
#   final Marshaller marshaller = jaxbContext.createMarshaller();
#   marshaller.marshal(book, System.out);
#
# why is it bad?
#   1) it is not the book instance that creates the XML. it's someone else, outside of the class Book
#   2) the control is lost (not inverted, but lost!)
#   3) the object is not in charge any more. it can't be responsible for what's happening to it
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
#   // the decorator adds an additional functionality of printing to the XML
#   class XmlBook implements Book{
#
#       private final Book origin;
#
#       XmlBook(final Book book) {
#           this.origin = book;
#       }
#
#       @Override
#       public String getTitle() {
#           return this.origin.getTitle();
#       }
#
#       public String toXML() { // a new functionality (method)
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

