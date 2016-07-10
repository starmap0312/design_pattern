# OOP principle: encapsulation
# 1) hide data behind objects, i.e. data must not be visible
# 2) objects only have access to data they encapsulate and never to data encapsulated by other objects
#
# example: Data Transfer Object
#
# (bad design)
#
#   Book loadBookById(int id) {              // a procedure to load data from RESTful API
#     JsonObject json = /* Load it from RESTful API */
#     Book book = new Book();                // store data in a Data Transfer Object, .i.e Book object
#     book.setISBN(json.getString("isbn"));
#     book.setTitle(json.getString("title"));
#     book.setAuthor(json.getString("author"));
#     return book;
#   }
#   
#   Book book = api.loadBookById(123);
#
#   void saveNewBook(Book book) {            // a procedure to save data to database
#     Statement stmt = connection.prepareStatement(
#       "INSERT INTO book VALUES (?, ?, ?)"
#     );
#     stmt.setString(1, book.getISBN());     // violates the priciple, data are visible by database object
#     stmt.setString(2, book.getTitle());    // the database object has access to the Book objet
#     stmt.setString(3, book.getAuthor());
#     stmt.execute();
#   }
#
#   database.saveNewBook(book);
#
#   // the Book object is dumb, as it only transfers data between two pieces of code, two procedures
#   // it is simply a passive data structure
#   
# (good desgin)
#
#   Book bookById(int id) {
#     return new JsonBook(                // not yet load data from RESTful API, but declare the access object
#       /* RESTful API access point */
#     );
#   }
#   
#   Book book = api.bookById(123);
#
#   void save(Database db) {              // the Book object actively save its content to database
#     JsonObject json = /* Load it from RESTful API */    // actually load data when demanded
#     db.createBook(
#       json.getString("isbn"),
#       json.getString("title"),
#       json.getString("author")
#     );
#   }
#
#   book.save(database);
#   
# (an alternative of the save() method)
#
#   void save(Database db) {
#     db.create()
#       .withISBN(json.getString("isbn"))
#       .withTitle(json.getString("title"))
#       .withAuthor(json.getString("author"))
#       .deploy();
#   }
#   
