// Object-relational mapping (ORM)
// accessing a relational database from an object-oriented language
//    ex. Hibernate (Java), ActiveRecord (Ruby on Rails), Doctrine (PHP), SQLAlchemy (Python)
//
// example:
//
// (bad design: ORM)

public class Post {

    private int id;
    private Date date;
    private String title;

    // CRUD manipulations
    public int getId() {               // Read
        return this.id;
    }

    public Date getDate() {            // Read
        return this.date;
    }

    public Title getTitle() {          // Read
        return this.title;
    }

    public void setDate(Date when) {   // Update
        this.date = when;
    }

    public void setTitle(String txt) { // Update
        this.title = txt;
    }
}

// create a session factory for later Hibernate operation
SessionFactory factory = new AnnotationConfiguration()
    .configure()
    .addAnnotatedClass(Post.class)
    .buildSessionFactory();

// create a session object via the session factory
Session session = factory.openSession();
try {
    Transaction txn = session.beginTransaction();

    // client code of ORM: manipulations of Post objects
    // (Read)
    List posts = session.createQuery("FROM Post").list(); // create the corresponding SQL query
    for (Post post : (List<Post>) posts){                 // each fetched row is an object
        System.out.println("Title: " + post.getTitle());
    }
    // (Update)
    Post post = new Post();                    // create a Post (row) object
    post.setDate(new Date());                  // setter method
    post.setTitle("How to cook an omelette");  // setter method
    session.save(post);                        // save the Post (row) object to database

    txn.commit();
} catch (HibernateException ex) {
    txn.rollback();
} finally {
    session.close();
}


// why is it bad?
// 1) it treats objects as data holders: only getter & setter methods
// 2) instead of encapsulating database interaction inside an object
//    it actually extracts it away, tearing a solid and cohesive living organism (object) apart
//    ex. two entry points
//       a) DTO (data transfer object): keeps the data, ex. Post object
//          it does not encapsulate data but rather expose data
//       b) session factory (ORM engine) deals with the data transfer object and communication with database 
//
//       Client class --> Post class
//                    --> ORM session (JDBC)
//
//       the Client object has to deal with both components (not a single entry point / object)
//
// 3) SQL is not hidden
//    ex. session.createQuery("FROM Post")  ==> in order to get all posts
//
// 4) difficult to test
//    ex. hard to mock an instance of SessionFactory (unit test is not possible)
//        instead, we may need to write integration test, i.e. connect to a test version of database


// (good design: SQL-speaking objects)
//
//     Posts: represents table object
//     Post: represents row object
//
//     Cleint class --> Post class with SQL-speaking ability (JDBC)
//

interface Posts {
    Iterable<Post> iterate();          // provide iterate() service (a composite object)
    Post add(Date date, String title); // provide add() service (add a row object to the database)
}

interface Post {
    int id();
    Date date();
    String title();
}

// client code of SQL-speaking objects
// (Read)
Posts posts = // we'll discuss this right now
for (Post post : posts.iterate()){
    System.out.println("Title: " + post.title());
}

// (Update)
Posts posts = // we'll discuss this right now
posts.add(new Date(), "How to cook an omelette");

// why is it good?
// 1) Posts and Post are true objects: they are in charge of all operations (active objects)
//    ex. Posts can list all post objects and create a new one
// 2) implementation details are hidden, i.e. database interaction (Client does not speak SQL anymore)
//    the client does not know if they talk to database or filesystem 

// implementation of Posts object (table object)
final class PgPosts implements Posts { // "Pg" stands for PostgreSQL

    private final Source dbase;

    public PgPosts(DataSource data) { // constructed on a data source
        this.dbase = data;            // testability: replaced by a test data source when testing
    }

    // (Read)
    public Iterable<Post> iterate() {
        return new JdbcSession(this.dbase)
            .sql("SELECT id FROM post")
            .select(
                new ListOutcome<Post>(
                    new ListOutcome.Mapping<Post>() {
                        @Override
                        public Post map(final ResultSet rset) {
                            return new PgPost(
                                this.dbase,
                                rset.getInteger(1)
                            );
                        }
                    }
                )
            );
    }

    public Post add(Date date, String title) {
        return new PgPost(
            this.dbase,
            new JdbcSession(this.dbase)
                .sql("INSERT INTO post (date, title) VALUES (?, ?)")
                .set(new Utc(date))
                .set(title)
                .insert(new SingleOutcome<Integer>(Integer.class))
       );
    }
}

// implementation of Post object (row object)
final class PgPost implements Post {

    private final Source dbase;
    private final int number;

    public PgPost(DataSource data, int id) { // constructed on a data source and an id
        this.dbase = data;                   // testability: replaced by a test data source when testing
        this.number = id;
    }

    public int id() {
        return this.number;
    }

    public Date date() {
        return new JdbcSession(this.dbase)
            .sql("SELECT date FROM post WHERE id = ?")
            .set(this.number)
            .select(new SingleOutcome<Utc>(Utc.class));
    }

    public String title() {
        return new JdbcSession(this.dbase)
            .sql("SELECT title FROM post WHERE id = ?")
            .set(this.number)
            .select(new SingleOutcome<String>(String.class));
    }
}

// performance problem
// 1) accessing each PgPost's attribute requires a separate DB session
// 2) to improve the performance, we can define a cache decorator class

final class ConstPost implements Post {

    private final Post origin;
    private final Date dte;
    private final String ttl;

    public ConstPost(Post post, Date date, String title) { // pass in the data & title cached data
        this.origin = post;
        this.dte = date;
        this.ttl = title;
    }

    public int id() {                                      // use the origin Post to get the id
        return this.origin.id();
    }

    public Date date() {                                   // return the cached date
        return this.dte;
    }

    public String title() {                                // return the cached title
        return this.ttl;
    }
}

final class ConstPgPosts implements Posts {
    // ...

    public Iterable<Post> iterate() {
        return new JdbcSession(this.dbase)
            .sql("SELECT * FROM post")
            .select(
                new ListOutcome<Post>(
                    new ListOutcome.Mapping<Post>() {
                        @Override
                        public Post map(final ResultSet rset) {
                            return new ConstPost(
                                new PgPost(
                                    ConstPgPosts.this.dbase,
                                    rset.getInteger(1)
                                ),
                                Utc.getTimestamp(rset, 2),
                                rset.getString(3)
                            );
                        }
                    }
                )
            );
    }
}

// transaction problem
// 1) either every object deals with its own transaction and encaplsulate them (nested transaction problem)
// 2) or create a session-wide transaction object that accepts a ad-hoc & annonymous "callable" class

final class Txn {

    private final DataSource dbase;

    public <T> T call(Callable<T> callable) { // the transaction object accepts a callable object in its call() method
        JdbcSession session = new JdbcSession(this.dbase);
        try {
            session.sql("START TRANSACTION").exec();
            T result = callable.call();       // the transaction object wraps the callable object's call() in a transaction block
            session.sql("COMMIT").exec();
            return result;
        } catch (Exception ex) {
            session.sql("ROLLBACK").exec();
            throw ex;
        }
    }
}

new Txn(dbase).call(
    new Callable<Integer>() {                 // create an annonymous callable object for each transaction operations
        @Override
        public Integer call() {
            Posts posts = new PgPosts(dbase);
            Post post = posts.add(new Date(), "How to cook an omelette");
            posts.comments().post("This is my first comment!");
            return post.id();
        }
    }
);
