# GRASP: General Responsibility Assignment Software Patterns
#  1) Controller:
#  - an object that is responsible for receiving or handling an event
#  - it receives and coordinates an operation, and delegates the work that needs to be done
#    to other objects, instead of doing the work itself
#
#  2) Creator:
#  - a class that is responsible for creating objects, ex. simple factory (i.e. a class with
#    a parameterized creation method), factory method (i.e polymorphic creation via subclassing),
#    or abstract factory (i.e. a group of related factory methods)
#  - a class B should be responsible for creating instances of A if one or more of the following
#    apply:
#      a) instances of B closely use instances of A
#      b) instances of B have the initializing information for instances of A and pass it
#         on creation (ex. dependency injection pattern)
#      c) instances of B contain or compositely aggregate instances of A (ex. strategy pattern)
#      d) instances of B record instances of A
#
#  3) High Cohesion:
#  - the responsibilities of a class, module, or application are strongly related
#  - break a system into subsystems or classes to increase cohesion
#  - keep objects focused, manageable, and understandable (otherwise, they are hard to reuse, 
#    maintain, and comprehend)
#
#  4) Indirection:
#  - delegate the stated task of an object to another helper object, ex. strategy pattern and
#    decorator pattern
#  - create an intermediate object that mediate two classes (the two classes are low coupling)
#    ex. in MVC (model-view-controller), the controller mediate between data (model) and its
#    representation (view) 
#
#  5) Information Expert
#  - determine where to delegate responsibilities, including methods, fields, and so on
#  - place the responsibility on the class with the most information required to fulfill it
#
#  6) Low Coupling
#  - low dependency between classes, i.e. changes in one class have low impact on other classes
#  - higher reuse potential
#
#  7) Polymorphism
#  - the responsibility of defining the variation of behaviors based on class type is located at
#    the class type where the variation happens
#
#  8) Protected Variations
#  - wrap the instability with an interface and use polymorphism, so that objects are protected
#    from the variations of other objects or subsystems (goal: close for modification)
#
#  9) Pure Fabrication
#  - define a made-up class that does not represent a concept in the problem domain; in other
#    words, when an operation does not belong to any object (or information), implement the
#    operation in a made-up class, also called service
#  - such a design is to achieve low coupling, high cohesion, and code reusability
#
