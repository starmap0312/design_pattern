# ActiveRecord
# 1) ORM encourages us to turn objects into DTOs (passive data holders) and turn the program into procedural
#    ORM has two parts: data objects (entities) and session/engine object 
#    ex.
#      book.setTitle("Java in a Nutshell"); // book serves as a data holder
#      session.update(book);                // session communicates with the database
# 2) ActiveRecord is even worse, as it moves the engine into parent class
#    the object is still a data container, but pretends to be a proper object (active, and not data holder)
#    ex.
#      book.setTitle("Java in a Nutshell"); // book also serves as a data holder
#      book.update();                       // the parent class takes care of the communication with database
