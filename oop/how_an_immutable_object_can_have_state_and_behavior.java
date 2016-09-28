// How an Immutable Object Can Have State and Behavior
//   we deal with frequently changing objects
//   ex. if a new document frequently changes its title, title is not a state of the document but its behavior
//
// example: object that represents a frequently changing-title document
//
// (bad design: a mutable object)

class Document {

    private int id;            // the state of the object
    private String title;      // the state of the object

    Document(int id) {
        this.id = id;
    }

    public String getTitle() { // get the object's state
        return this.title;
    }

    public String setTitle(String text) { // can change the object's internal state
        this.title = text;
    }

    public String toString() {
        return String.format("doc #%d about '%s'", this.id, this.text);
    }
}

// the client code
Document first = new Document(50);
first.setTitle("How to grill a sandwich");

Document second = new Document(50);
second.setTitle("How to grill a sandwich");

if (first.equals(second)) { // return FALSE even if the two objects have the same state 
    System.out.println(String.format("%s is equal to %s", first, second));
}

// modifying its internal state
first.setTitle("How to cook pasta");

// (good design: immutable objects, i.e. the state of object never changes)

class Document {

    private final int id;
    private final String title;

    Document(int id, String title) {
        this.id = id;
        this.title = title;
    }

    public String title() {
        return this.title;
    }

    public Document withTitle(String title) { // creating another immutable object
        return new Document(this.id, title);
    }

    public String toString() {
        return String.format("doc #%d about '%s'", this.id, this.text);
    }

    @Override
    public boolean equals(Object doc) { // compares documents by ids and titles, as they are object's states
        return doc instanceof Document
            && Document.class.cast(doc).id == this.id
            && Document.class.cast(doc).title.equals(this.title);
    }
}

// the client code
Document first = new Document(50, "How to grill a sandwich");

Document second = new Document(50, "How to grill a sandwich");

if (first.equals(second)) { // return TRUE as the two objects represent the same document
    System.out.println(String.format("%s is equal to %s", first, second));
}

// cannot modify the object's internal state
Document first = new Document(50, "How to grill a sandwich");
// but can create a new object for representing another document
third = first.withTitle("How to cook pasta");

// What About Frequent Changes?

// if document's title frequently changes, then
//   the title should not be part of its state; instead, it should be its behavior

class Document {

    private final int id;         // the object's state
    private final Storage storage;  // the object's collaborator

    Document(int id) {
        this.id = id;
        this.storage = new Storage(); // the collaborator (encapsulated knowledge, hidden from the client)
    }

    public String readTitle() {
        // the object has a collaborator that it can read title from some storage
        return new String(this.storage.read());
    }

    public void saveTitle(String title) {
        // the object has a collaborator that it can save title to some storage
        this.storage.write(text.getBytes());
    }

    public String toString() {
        return String.format("doc #%d about '%s'", this.id, this.title());
    }

    @Override
    public boolean equals(Object doc) {
        return doc instanceof Document
            && Document.class.cast(doc).id == this.id;
    }
}

// the interface: both readTitle() and saveTitle are the object's behaviors
interface Document {

    String readTitle();
    void saveTitle(String text);
}

// the Storage object should be a data animator, not just holding data (because object is alive)
// the Document object needs extra knowledge in order to gain access to the data
//   ex. a database unique key, an HTTP address, a file name, or a storage address
// the Document object is collaborating with other object for accessing the title
//   not using getter/setter methods to change its internal state
