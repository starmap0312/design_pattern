# Object-relational mapping (ORM)
#  1) creates a "virtual" object database that can be used from within the object-oriented programming language
#  2) convert the object values into groups of simpler values (integer / strings) for storage in the database
#     (i.e. store in tables), and convert them back upon retrieval
#  3) translate the logical representation of the objects into an atomized form stored in the database
#     preserve the objects properties and relationships so that they can be reloaded as objects when needed
#  4) expose some filtering and querying functionality
#     allow subsets of the storage base to be accessed and modified
#  5) alternative
#     use the native procedural languages provided by the database, called from client using SQL statements
#     use Data Access Object (DAO) design pattern to abstract these statements and offer a lightweight
#       object-oriented interface to the application 
#
#  an example:
#
#  (without ORM)
class DBCommand(object):

    def __init__(self, connection, sql):
        self.conn = connection
        self.sql = sql

    def execute(self):
        # query the database using self.conn and sql and get the query result back
        rc = ( { "FirstName": "Jonh", "LastName": "Chen"}, { "FirstName": "Patty", "LastName": "Huang"} )
        return rc

# construct connection object via database API
connection = None
sql = "SELECT * FROM persons WHERE id = 10"
cmd = DBCommand(connection, sql)
rc = cmd.execute()
name = rc[0]["FirstName"]

# (with ORM)

class Person(object):

    @staticmethod
    def get(id):
        return Person()

    def getFirstName(self):
        pass

class Repository(object):

    def getPerson(self, id):
        return Person()

# method 1: methods of storage repository
repository = Repository() # an object that represents the storage repository
person = repository.getPerson(10) 

# method 2: static method of objects
person = Person.get(10)

name = person.getFirstName()

# provide some filtering and querying functionality
# ex.
# person = Person.get(Person.Properties.Id == 10)

# Object-relational mapping (ORM) is bad design
#   good design: SQL-Speaking Objects
#   ex.
#     (Table: Posts)
#     +-----+------------+--------------------------+
#     | id  | date       | title                    |
#     +-----+------------+--------------------------+
#     |   9 | 10/24/2014 | How to cook a sandwich   |
#     |  13 | 11/03/2014 | My favorite movies       |
#     |  27 | 11/17/2014 | How much I love my job   | ==> row: Post
#     +-----+------------+--------------------------+
#
#     class Posts: represents the table
#     class Post:  represents the row
#
#     interface Posts {
#         Iterable<Post> iterate();
#         Post add(Date date, String title);
#     }
#
#     interface Post {
#         int id();
#         Date date();
#         String title();
#     }
#
#     // how to list all posts in the database table
#     Posts posts = new PostgrePosts(dbase);
#     for (Post post : posts.iterate()){
#         System.out.println("Title: " + post.title());
#     }
#
#     // how to create a new post
#     Post post = posts.add(new Date(), "How to cook an omelette");
#     System.out.println("Just added post #" + post.id());
#
#     final class PostgrePosts implements Posts {
#
#         private final Source dbase;
#
#         public PostgrePosts(DataSource data) { // dependency injection by constructor
#             this.dbase = data;
#         }   
#
#         public Iterable<Post> iterate() {
#             return new JdbcSession(this.dbase)
#                 .sql("SELECT id FROM post")
#                 .select(
#                     new ListOutcome<Post>(
#                         new ListOutcome.Mapping<Post>() {
#                             @Override
#                             public Post map(final ResultSet rset) {
#                                 return new PostgrePost(
#                                     this.dbase,
#                                     rset.getInteger(1)
#                                 );
#                             }
#                         }
#                     )
#                 );
#         }
#
#         public Post add(Date date, String title) {
#             return new PostgrePost(
#                 this.dbase,
#                 new JdbcSession(this.dbase)
#                 .sql("INSERT INTO post (date, title) VALUES (?, ?)")
#                 .set(new Utc(date))
#                 .set(title)
#                 .insert(new SingleOutcome<Integer>(Integer.class))
#             );
#         }
#    }
#
#    final class PostgrePost implements Post {
#
#        private final Source dbase;
#        private final int number;
#
#        public PostgrePost(DataSource data, int id) {
#            this.dbase = data;
#            this.number = id;
#        }
#
#        public int id() {
#            return this.number;
#        }
#
#        public Date date() {
#            return new JdbcSession(this.dbase)
#                .sql("SELECT date FROM post WHERE id = ?")
#                .set(this.number)
#                .select(new SingleOutcome<Utc>(Utc.class));
#        }
#
#        public String title() {
#            return new JdbcSession(this.dbase)
#                .sql("SELECT title FROM post WHERE id = ?")
#                .set(this.number)
#                .select(new SingleOutcome<String>(String.class));
#        }
#    }
