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
#       public static Database INSTANCE = new Database(); // a singleton: one and the only one static (global) instance
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
#   // suppose that we have to access to the pool in many different places, we can get a new connection from the sigleton object
#
#   @Path("/")
#   class Index {
#
#       @GET
#       public String text() { // a controller method
#           java.sql.Connection connection = Database.INSTANCE.connect(); // get a new connection from the singleton instance
#           return new JdbcSession(connection)
#               .sql("SELECT text FROM table")
#               .fetch(new SingleOutcome(String.class))
#       }
#   }
#
#   // we need a singleton instance to be globally available so that any MVC controller can have direct access to it
#
#   (good design)
#
#   // use dependency injection instead
#   //   let class Index get the database connection pool via its constructor
#
#
#   class Index {
#
#       private java.sql.Connection conn;
#
#       public Index(java.sql.Connection connection) {
#           this.conn = connection;
#       }
#
#       public String text() { // a controller method
#           return new JdbcSession(this.conn)
#               .sql("SELECT text FROM table")
#               .fetch(new SingleOutcome(String.class))
#       }
#   }
#
#   // pass an instance of Database to all objects that may need it through their constructors
#   // i.e. forget about singletons; turn them into dependencies and pass them from object to object through the operator new

