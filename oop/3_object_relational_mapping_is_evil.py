# Object-relational mapping (ORM)
# accessing a relational database from an object-oriented language
#    ex. Hibernate (Java), ActiveRecord (Ruby on Rails), Doctrine (PHP), SQLAlchemy (Python)
#
# example:
#
#   Post post = new Post();
#   post.setDate(new Date());
#   post.setTitle("How to cook an omelette");
#   session.save(post);
#
# why is it bad?
# 1) instead of encapsulating database interaction inside an object
#    it actually extracts it away, tearing a solid and cohesive living organism (object) apart
#    ex.
#       Post object keeps the data
#       the ORM engine (session factory) knows how to deal with the object data and transfer it to database 
#
#       Client class --> Post class
#                    --> ORM session (JDBC)
#
#       the Client object has to deal with two components (the Client should have a single entry point / object)
# 2) SQL is not hidden
#    ex.
#      session.createQuery("FROM Post")  ==> in order to get all posts
# 3) difficult to test
#    the Client object needs an instance of SessionFactory, which is hard to mock
#    can only write a integration test, in which we connect to a test version of database, and tested against
#    the test database instance (a bad design, unit test is not possible)
#
# better design: SQL-speaking objects
#
#   we define two real-world entities (objects): database table and table row, both can speak SQL
#
#     Cleint class --> Post class with SQL-speaking ability (JDBC)
#
#   ex.
#
#     interface Posts {
#         Iterable<Post> iterate();          // provide iterate() service (a composite object)
#         Post add(Date date, String title); // provide add() service (add a row object to the database)
#     }
#
#     interface Post {
#         int id();
#         Date date();
#         String title();
#     }
#
#     // the client code
#     Posts posts = // we'll discuss this right now
#     for (Post post : posts.iterate()){
#         System.out.println("Title: " + post.title());
#     }
#
#     Posts posts = // we'll discuss this right now
#     posts.add(new Date(), "How to cook an omelette");
#
#     // the two objects provide active services and hide their implementation details (ex. database interaction)
#     // the client does not know if they talk to database or keep their data in files
