# responsibilities vs. functions
  functions: implementation detail of the solution space, the computer program
  responsibilities: expectations of the domain, the problem space
  behavior-driven development, not data-driven development (the latter leads to tighter coupling and more classes)

# collaborator
  1) if Object A requires Object B to provide some advertised service, then Object B becomes
       the collaborator of Object A
  2) Object B should NOT be an attribute of Object A, instead Object B:
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
     object discovery process begins with underlining the nouns (names) in a domain or problem description
  2) decompose the problem space into behavioral objects
     how people recognize different objects in their world and, having recognized an object
     what assumptions are made about how to interact with that object and what its responses will be
  3) using metaphor, domain anthropology, to discover objects and their interactions
     domain nouns provide a rich set of potential objects
     the relationships provide a rich set of potential responsibilities of those objects
