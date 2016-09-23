// JAXB is an old Java library 
//   marshalling: converts a Java object into an XML document
//   unmarshalling: converts an XML document into a Java object
//   it turns objects into passive data structures
//
// examples:
//
// (bad design)

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

// the class is a passive data holder with getter() methods
@XmlRootElement
public class Book {

    private final String isbn;
    private final String title;

    public Book(final String isbn, final String title) {
        this.isbn = isbn;
        this.title = title;
    }

    @XmlElement
    public String getIsbn() {
        return this.isbn;
    }

    @XmlElement
    public String getTitle() {
        return this.title;
    }

}

// the client code: create a marshaller and ask it to convert an instance of class Book into XML
final Book book = new Book("0132350882", "Clean Code");
final JAXBContext context = JAXBContext.newInstance(Book.class);
final Marshaller marshaller = jaxbContext.createMarshaller();
marshaller.marshal(book, System.out);

// the output
<?xml version="1.0"?>
<book>
  <isbn>0132350882</isbn>
  <title>Clean Code</title>
</book>


// why is it bad?
//   treat an object as a bag of data
//   extract the data and convert it into XML the way JAXB wants
//   the object has no control over this process
//
// (good design)
//
// a class that actively provides converting toXML() service
public class Book {

    private final String isbn;
    private final String title;

    public Book(final String isbn, final String title) {
        this.isbn = isbn;
        this.title = title;
    }

    public String toXML() {
        // create XML document and return
    }
}

// drawbacks: code duplication
//   building an XML document is a rather verbose process in Java
//   every class had to re-implement it in its toXML() method
//   if we to deliver the XML as a String or an InputStream or an instance of org.w3c.dom.Document
//     we need many toXML() methods 
//
// (another good design: Xembly)

import org.xembly.Directive;

public class Book {

    private final String isbn;
    private final String title;

    public Book(final String isbn, final String title) {
        this.isbn = isbn;
        this.title = title;
    }

    public Iterable<Directive> toXembly() { // the method deliver a Xembly Directive objects instead
        return new Directives()
            .add("book")
            .add("isbn").set(this.isbn).up()
            .add("title").set(this.title).up()
            .up();
    }
}

// the client code: Xembler class converts Xembly directives into an XML document
final Book book = new Book("0132350882", "Clean Code");
final String xml = new Xembler(book.toXembly()).xml();

// why is it good?
//   the internals of the object are not exposed via getters
//   the object is fully in charge of the XML marshalling process
