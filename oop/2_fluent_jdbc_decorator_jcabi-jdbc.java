// Fluent JDBC Decorator
// jcabi-jdbc:
//   a library that simplifies interaction with relational databases via JDBC, avoiding the need to use ORM
//   a lightweight wrapper of JDBC
//   convenient to use when you don't need a full-scale ORM, ex. Hibernate
//     ex. want just to select, insert, or update a few rows in a relational database
//   used to insert, update, delete a row, or execute any SQL statement
//   used mainly for single atomic transactions
//
// example: fetch text from a SQL table with jcabi-jdbc

String name = new JdbcSession(source)
    .sql("SELECT name FROM employee WHERE id = ?")
    .set(1234)
    .select(new SingleOutcome<String>(String.class));
// instance of JdbcSession is a "transaction" in a database, instantiated with a single parameter: data source

// obtain the data source from the connection pool, ex. connect to PostgreSQL
@Cacheable(forever = true)                                 // cache Java method results for some time
private static DataSource source() {
    BoneCPDataSource src = new BoneCPDataSource();
    src.setDriverClass("org.postgresql.Driver");
    src.setJdbcUrl("jdbc:postgresql://localhost/db_name");
    src.setUser("jeff");
    src.setPassword("secret");
    return src;
}
// setting the forever attribute to true means that we don't want this method to be called more than once
//   the connection pool to be created just once, and every second call should return its existing instance
//   similar to a Singleton pattern
//
// example: single atomic transaction

new JdbcSession(source)
    .autocommit(false)
    .sql("START TRANSACTION")                   // 1st SQL statement
    .update()
    .sql("DELETE FROM employee WHERE name = ?") // 2nd SQL statement
    .set("Jeff Lebowski")
    .update()
    .sql("INSERT INTO employee VALUES (?)")     // 3rd SQL statement
    .set("Walter Sobchak")
    .insert(Outcome.VOID)
    .commit();
// execute three SQL statements one by one, leaving connection (and transaction) open until commit() is called
