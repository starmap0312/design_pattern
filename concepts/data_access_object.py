# Data Access Object (DAO)
# 1) an object that provides an abstract interface to database or other persistence mechanism
# 2) by mapping application calls to the persistence layer, DAO provides some specific data operations
#    without exposing details of the database
# 3) single responsibility principle
#    separate what data accesses the application needs, in terms of domain-specific objects and data types, 
#      from how these needs can be implemented with a specific DBMS, database schema, etc.
#    i.e. separate the public interface of the DAO from the implementation of the DAO
# 4) advantages
#    a) separation of responsibilities 
#       i.e. DAO interface and DAO implementation: both can evolve frequently and independently
#
#                    (uses)              (retrieved from)
#            Clients -----> Model object <--------------> DAO interface
#                                                               |           (store/retrieve)
#                                                        DAO implementation <--------------> database
#
#       Model object: an object with getter/setter methods to store data retrieved using DAO
#
#       changing business logic (DAO client) can rely on the same DAO interface
#       changing persistence logic (database) do not affect DAO clients as long as DAO implementation are correct
#    b) Information hiding: all details of storage are hidden from the rest of the application
#    c) facilitate unit testing the code
#       substitute DAO with a test double in the test, making the tests non-dependent on the persistence layer
# 5) disadvantages
#    a) code duplication
#    b) abstraction inversion
#    c) high cost database access
#       ex. trigger multiple database queries that could be returned in a single SQL operation
