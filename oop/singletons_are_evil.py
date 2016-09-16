# singletons
#   1) they are anti-patterns, as they work as global things
#      ex. a database connection pool, a repository, a configuration map, etc. 
#   2) use dependency injections instead
#   
# example: a database connection pool
#
#   (bad design)
#
#   class Database {
#
#       public static Database INSTANCE = new Database();
#       // a singleton: declare as a class's static member
#       //   one and the only one static (global) instance
#
#       private Database() {
#           // create a connection pool
#       }
#
#       public java.sql.Connection connect() {
#           // Get new connection from the pool and return
#       }
#   }
#   
#   // suppose we have to access to the pool in many different places
#   //   we can get a new connection from the sigleton object
#
#   // a JAX-RS client example (it's a simple MVC architecture, where text() method is a controller)
#   @Path("/")
#   class Index {
#
#       @GET
#       public String text() { // a controller method
#
#           java.sql.Connection connection = Database.INSTANCE.connect();
#           // get a new connection from the (global) singleton instance, i.e. Database.INSTANCE
#
#           return new JdbcSession(connection)
#               .sql("SELECT text FROM table")
#               .fetch(new SingleOutcome(String.class));
#       }
#   }
#
#   // we need a singleton instance to be globally available so that any MVC controller 
#   //   have direct access to it
#
#   (good design)
#
#   // use dependency injection instead: get the database connection pool from constructor
#
#
#   class Index {
#
#       private java.sql.Connection conn;
#
#       public Index(Database db) {
#           this.db = db;
#       }
#
#       public String text() { // a controller method
#
#           java.sql.Connection connection = db.connect();
#
#           return new JdbcSession(this.conn)
#               .sql("SELECT text FROM table")
#               .fetch(new SingleOutcome(String.class));
#       }
#   }
#
#   // forget about singletons: turn them into dependencies and pass them from object to object
#   //   ex. pass an instance of Database to all objects that may need it through their constructors
