# Data Transfer Object (DTO)
# 1) DTO serves a building block of object-relational mapping (ORM), which is also an anti-pattern
# 2) DTO creates dumb objects which serves as simple data bag and encourages procedural programming
# 3) DTO violates data encapsulation principle, allowing other objects to set/get the data of an object
#    (data within an object should be invisible to other objects and stays within the object the whole time)
#
# OOP principle: encapsulation
# 1) hide data behind objects, i.e. data must not be visible
# 2) objects only have access to data they encapsulate and never to data encapsulated by other objects
#
# (bad design)
#
# Book loadBookById(int id) {              // a procedure to load data from RESTful API
#     JsonObject json = /* Load it from RESTful API */
#     Book book = new Book();                // store data in a dumb object (Data Transfer Object)
#     book.setISBN(json.getString("isbn"));  // book object allows others to set its data
#     book.setTitle(json.getString("title"));
#     book.setAuthor(json.getString("author"));
#     return book;
# }
#   
# Book book = api.loadBookById(123);
#
# void saveNewBook(Book book) {          // data object is transferred to a procedure to be saved in database
#     Statement stmt = connection.prepareStatement("INSERT INTO book VALUES (?, ?, ?)");
#     stmt.setString(1, book.getISBN());   // violates the priciple, data are visible by database object
#     stmt.setString(2, book.getTitle());  // the database object has access to the Book objet
#     stmt.setString(3, book.getAuthor());
#     stmt.execute();
# }
#
# database.saveNewBook(book);
#
# // the Book object is dumb, existing only for transfering data between two pieces of code, two procedures
# // it is a passive data structure
#   
# (good desgin)
#
# class Api {
#
#     Book bookById(int id) {
#         return new JsonBook(   // not yet load data from RESTful API, only declare the access object
#           /* RESTful API access point */
#         );
#     }
# }
#
# Book book = api.bookById(123);
#
#   // Api is responsible for providing you a JsonBook object via its id
#
# class JsonBook {
#
#     void save(Database db) {    // ask the Book object actively save its content to database
#         JsonObject json = /* Load it from RESTful API */    // data are loaded when on demand
#         db.createBook(          // the data stays inside the object and are invisble to outside objects
#             json.getString("isbn"),
#             json.getString("title"),
#             json.getString("author")
#         );
#     }
# }
#
# // JsonBook is responsible for saving its content to database
# //   it knows how to get the json format of its content
# //   its client does not need to know how and when it will be done
# // JsonBook serves as a representative of its content (no need to store them)
# //   it may get them from outside, ex. a RESTful api service
#
# book.save(database);
#
# // the book object is no longer a passive data bag 
# // it provides services (actively saving its content to database)
#   
# (refinement: if createBook() has too many parameters, refine the save() method as follows)
#
# void save(Database db) {
#     JsonObject json = /* Load it from RESTful API */    // data are loaded when on demand
#     db.create()
#       .withISBN(json.getString("isbn"))
#       .withTitle(json.getString("title"))
#       .withAuthor(json.getString("author"))
#       .deploy();
# }
