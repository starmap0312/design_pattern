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

