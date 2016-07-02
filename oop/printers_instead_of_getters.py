# Getters and Setters are bad design
#
#  objects are active components: we shuld not get information or set status to them
#
#  ex.
#    (bad design)
#
#    Dog dog = new Dog();
#    dog.setBall(new Ball());
#    Ball ball = dog.getBall();
#    dog.setWeight("23kg");
#
#    (good design)
#
#    Dog dog = new Dog("23kg");
#    int weight = dog.weight();
#    dog.take(new Ball());
#    Ball ball = dog.give(); // dog object should never return NULL (NULL references are also bad design)
#
#  ex.
#
#  (bad design)
#
#  public class Book { // the objects has two fields
#
#      private final String isbn = "0735619654";
#      private final String title = "Object Thinking";
#
#  }
#  
#  // in order to print the fields in the XML format, we rely on the JAXB
#  import javax.xml.bind.annotation.XmlElement;
#  import javax.xml.bind.annotation.XmlRootElement;
#
#  @XmlRootElement
#  public class Book {
#
#      private final String isbn = "0735619654";
#      private final String title = "Object Thinking";
#
#      @XmlElement
#      public String getIsbn() {  // a getter method
#          return this.isbn;
#      }
#
#      @XmlElement
#      public String getTitle() { // a getter method
#          return this.title;
#      }
#  }
#  // this is an offensive way of treating the object (exposing everything inside to the public)
#  // i.e. anyone can access in many possible ways
#
#  (good design)
#  // why getters exist?
#  // because we don't trust our objects, and only trust the data they store
#  // we don't want this Book object to generate the XML (just want it to give us the data)
#
#  public class Book {
#
#      private final String isbn = "0735619654";
#      private final String title = "Object Thinking";
#
#      public String toXML() {   // a print method, print the XML format for us
#          return String.format(
#              "<book><isbn>%s</isbn><title>%s</title></book>",
#              this.isbn, this.title
#          );
#      }
#  }
#  // the object no longer expose its internals
#  
#  public class Book {
#
#      private final String isbn = "0735619654";
#      private final String title = "Object Thinking";
#
#      public String toJSON() {  // another print method, print the JSON format for us
#          return String.format(
#              "{\"isbn\":\"%s\", \"title\":\"%s\"}",
#              this.isbn, this.title
#          );
#      }
#  }
#
#  // an object with multiple print methods would become a problem
#
#  (good design)
#
#  public class Book {
#
#      private final String isbn = "0735619654";
#      private final String title = "Object Thinking";
#
#      public Media print(Media media) { // one single print method: print to a media
#          return media.with("isbn", this.isbn).with("title", this.title);
#      }
#  }
#  // the book should not have any idea about what is printed
#  
#  class JsonMedia implements Media {
#
#      private final JsonObjectBuilder builder;
#
#      JsonMedia() {
#          this(Json.createObjectBuilder());
#      }
#
#      JsonMedia(JsonObjectBuilder bdr) {
#          this.builder = bdr;
#      }
#
#      @Override
#      public Media with(String name, String value) {
#          return new JsonMedia(this.builder.add(name, value));
#      }
#
#      public JsonObject json() {
#          return this.builder.build();
#      }
#  }
#  
#  // the client code
#  JsonMedia media = new JsonMedia("book");
#  JsonObject json = book.print(media).json();
#  
