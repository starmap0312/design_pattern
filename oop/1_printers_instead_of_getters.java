// Getters and Setters are bad design
//
//  1) getters and setters expose object's data
//  2) they make objects passive data hodlers and we get information from or set status to them
//     objects should be active components, with some responsibility
//  3) they encourage procedural programming (we don't try objects, and only trust the data they store)
//
//  ex.
//    (bad design: passive data holders)

Dog dog = new Dog();
dog.setBall(new Ball());
Ball ball = dog.getBall();
dog.setWeight("23kg");

//    (good design: active entities)

Dog dog = new Dog("23kg");
int weight = dog.weight();
dog.take(new Ball());
Ball ball = dog.give(); // dog object should never return NULL (NULL references are also bad design)
//
//  ex.
//
//  (bad design)

public class Book { // the objects has two fields

    private final String isbn = "0735619654";
    private final String title = "Object Thinking";

}

//  // in order to print the fields in the XML format, we rely on the JAXB
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class Book {

    private final String isbn = "0735619654";
    private final String title = "Object Thinking";

    @XmlElement
    public String getIsbn() {  // a getter method
        return this.isbn;
    }

    @XmlElement
    public String getTitle() { // a getter method
        return this.title;
    }
}
//  // this is an offensive way of treating the object (exposing everything inside to the public)
//  // i.e. anyone can access/modity its content/behaviors in many possible ways
//
//  why is it bad?
//   it is procerual thinking, we want control everything
//   we don't want the Book object to generate the XML, and just want it to give us the data
//
//  (good design: let the Book object actively takes the responsibility of generating XML format)
//
public class Book {

    private final String isbn = "0735619654";
    private final String title = "Object Thinking";

    public String toXML() {   // a print method, print the XML format for us
        return String.format(
            "<book><isbn>%s</isbn><title>%s</title></book>",
            this.isbn, this.title
        );
    }
}
//  // the object no longer expose its internals
//  
//  // but if a similar responsibility is needed (the object may be responsible for too many things)
public class Book {

    private final String isbn = "0735619654";
    private final String title = "Object Thinking";

    public String toJSON() {  // another print method, print the JSON format for us
        return String.format(
            "{\"isbn\":\"%s\", \"title\":\"%s\"}",
            this.isbn, this.title
        );
    }
}
//
//  // an object with multiple print methods would become a problem
//
//  (good design: delegate the printer responsibility to other objects, i.e. collaborators)
//
public class Book {

    private final String isbn = "0735619654";
    private final String title = "Object Thinking";

    public Media print(Media media) { // print to a Media object, i.e. creat and return a Media object
        return media.with("isbn", this.isbn).with("title", this.title);
    }
}
//  the book object has no idead what is printed
//  it is only responsible for adding its content to the printer object, and providing it to other objects
//  
//  an object that knows how to add new json (key, value) pairs and is responsible for printing the json format
class JsonMedia implements Media {

    private final JsonObjectBuilder builder;

    JsonMedia(String head) {           // second constructor
        this(Json.createObjectBuilder());
    }

    JsonMedia(JsonObjectBuilder bdr) { // primary constructor
        this.builder = bdr;
    }

    @Override
    public Media with(String key, String value) { // the object provides a way to add content to itself
        return new JsonMedia(this.builder.add(key, value));
    }

    public JsonObject json() { // JsonMedia can provide the json format of its content
        return this.builder.build();
    }
}

// the client wants to print the book object into json format, so it instantiate a JsonMedia object and ask
//   the book object to print to it
JsonMedia media = new JsonMedia("book");
JsonObject json = book.print(media).json();

// the JsonMedia can be replaced by other other objects that also implements Media
// ex. XmlMedia who knows how to add new xml contents via with() and
//     provides xml() for printing the XML format
