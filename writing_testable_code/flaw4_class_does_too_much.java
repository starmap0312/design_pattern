// Flaw #4: Class Does Too Much
// (Warning Signs)
//   Summing up what the class does includes the word "and"
//     violates the single responsibility principle
//     ex. construction of collaborators is one of the class's responsibility
//         (use dependency injection to pass in pre-configured objects)
//     ex. managers/ controller / utility / context / god classes, etc. are bad
//     ex. classes with many fields / methods
//   Class would be challenging for new team members to read and quickly "get it"
//     when objects have a clear responsibility and naming, it is easy to keep them focused
//   Class has fields that are only used in some methods
//     try to distinguish the responsibilities of methods of using and not using the fields
//     i.e. create separate classes for methods using and not using the fields
//   Class has static methods that only operate on parameters
//     try to create an object that does the operations of these static methods
//   Class with many collaborators
//     ex. passed in, constructed inside the class, accessed through statics
//   Class that mediates the interactions between objects 
//     objects should talk to each other directly
//
// why is it bad?
//   interactions between responsibilities are buried within the class (code are tightly coupled)
//     it is difficult to alter one responsibility at a time
//     it is hard to test and debug
//   it is hard to give a name to describe what the class does
//
// how to fix the problem?
//   identify the individual responsibilities
//     delegate the responsibility to other objects using decorator, strategy, etc.
//   hidden interactions between public APIs could be addressed better through composition
//     i.e. the class encapsulats the interaction between responsibilities
//     composition provides better flexibility (you can replace with subtypes of collaborators via composition)
