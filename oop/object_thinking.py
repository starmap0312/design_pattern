# responsibilities vs. functions
  1) functions: implementation detail of the solution space, the computer program (traditional thinking)
  2) responsibilities: expectations of the domain, the problem space (object thinking)

# behavior-driven development v.s data-driven development
  the latter leads to tighter coupling and more classes

# collaborator
  1) if Object A requires Object B to provide some advertised service, then Object B becomes
     the collaborator of Object A
  2) Object B should NOT be an attribute of Object A, instead Object B is:
     a parameter supplied to the service method of Object A
     a local variable of the service method of Object A
  3) minimize the number of collaborators, as they introduce coupling of objects

# class
  1) a label for a set of similar objects
  2) an object factory

# requirements of object thinking 
  1) decomposition based on discovering the “natural joints” in the domain (not solution)
  2) responsibility assignment based on expected behavior in the domain (not solution)
  3) aggregation of objects into communities capable of interaction and collective solution of a task  

# domain understanding
  1) include users to communicate their collective understanding of the objects and the domain
     naming things is how domain experts naturally decompose the domain
     object discovery process begins with underlining the nouns (names) in a domain/problem
  2) decompose the problem space into behavioral objects
     how people recognize different objects in their world and, having recognized an object
     what assumptions are made about how to interact with that object and what its responses will be
  3) using metaphor, domain anthropology, to discover objects and their interactions
     domain nouns provide a set of objects
     the relationships provide a set of responsibilities of those objects

# object definition
  1) a short description of the object (in the words of a domain user)
  2) an enumeration of the services it provides, i.e. responsibilities (and other collaborator objects)
  3) a stereotype/pattern: objects that resembles in terms of similarity of services provided
     ex. information holder, structurer, service provider, coordinator, controller, interfacer, and
         collection/container, etc.

# abstraction, generalization, classification, essentialism
  1) abstraction: separating characteristics into the relevant and irrelevant in order to focus on the relevant
     keep things simple by not providing abstractions until the abstractions provide simplicity
  2) generalization: separating characteristics into the shared and not shared
  3) classification: seperation based on similarity to a prototype
  4) essentialism: to identify the characteristic that is essential to be an instance of some class
     finding specific characteristics that make an object an object, ex. remove adjectives and use nouns only

# delegation
  1) if you delegate, delegate: do not try to retain any control over how your delegate does its job
  2) give the delegate object the ability to evaluate its own work and correct its own mistakes
     concentrate on your own responsibility

# responsibility
  1) state responsibilities in an active voice describing the service
     state responsibilities in terms of a service, with an awareness of a possible client for that service
  2) avoid responsibilities that are characteristic specific
     because an object may have many characteristics, ex. report age, report height, report eye color, etc. 
     instead, use an label for the responsibility, ex. describe yourself or identify yourself, and
     give the requester a description object: i.e. a collection of key/value pairs or an object with its
     own behaviors

# required knowledge of a object to perform the advertised service
  1) store that knowledge in an instance variable (attribute of the object)
     this makes the object to be responsible for maintaining the knowledge (use other methods first)
  2) obtain the knowledge from another object (collaborator)
     this creates dependency (should be minimized, so use other methods first)
  3) ask for that knowledge to be provided as an argument to the service method

