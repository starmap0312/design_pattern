// ActiveRecord
// 1) ORM has two parts: data transfer objects (entities) and session/engine object 
//    it encourages us to:
//    a) turn objects into DTOs (passive data holders)
//    b) turn the program into procedural
//
// (bad design: ORM)
//
// client code
book.setTitle("Java in a Nutshell"); // Book object serves as a data holder (DTO)
session.update(book);                // use session object to communicate with the database

// 2) ActiveRecord is even worse: it moves the engine into parent class
//    the object is still a data container, and pretends to be a proper object (active, and not data holder)
//
// (bad design: ActiveRecord)

// client code
book.setTitle("Java in a Nutshell"); // Book object still serves as a data holder (DTO)
book.update();                       // parent class takes care of communication with database

// why is it bad?
// 1) Book object is still a data holder (passive object)
// 2) Book object pretends to be active but knows nothing about SQL (or other persistence mechanisms)

// (good design: SQL-speaking objects)
//
// client code
books.add("Java in a Nutshell");     // Books object (table object) can add a book object given a title

// why is it good?
// 1) Book and Books objects are active objects providing services of Create/Read/Update/Delete operations

