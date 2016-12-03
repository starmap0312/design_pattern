// - Find Real-world Objects
// 1) identify object and its attributes (characteristics)
// 2) determine its public and private parts (what parts will be visible to other objects)
//    i.e. information hiding: for better encapsulation, modularity, and abstraction
//    identify things likely to change: ex. file format, data type implementation
//      a) hiding source of changes to localize its effects: loose coupling 
//      b) hiding complexity to improve design and code readability: ex. class Id instead of int
// 3) define its public interface
// 4) determine its behavior/method (allowed to do to other objects)
//
// - Form Consistent Abstractions
// handling different details at different levels
//
// - Encapsulate Implementation Details
//
// - Inherit when Inheritance Simplifies the Design
// define a base class that specifies common elements of multiple derived classes
//   it makes code reused but create coupling subclasses
// adhere to the Liskov Substitution Principle (LSP)
//   do not inherit from a base class unless derived class truly "is a" more specific version of base class
//   subclasses must be usable through base class interface without user needs to know the difference
//   ex. base class: Account
//       derived classes: CheckingAccount, SavingsAccount,
// the client code should always program to the base class or interface (not thinking about subclass details)
//
// - Information Hiding
// 1) good hiding can reduce the amount of code affected by a change
// 2) useful at all levels of design:
//    a) named constants instead of literals
//       ex. use a named constant MAX_EMPLOYEES to hide 100
//       ex. use id = NewId() to hide id = ++g_maxId
//    b) creation of data types: improve code design and readability
//       ex. create class ID to hide int
//    c) class design, routine design, and subsystem design
//
// - Identify Areas Likely to Change
// isolate unstable areas so that the effect of a change will be limited to one routine, class, or package
// ex. Status variables: an enumerated type with values: ErrorType_None, ErrorType_Warning, and ErrorType_Fatal
//     use access routines rather than checking the variable directly
//
// - Keep Coupling Loose
// kinds of coupling
// 1) simple-data-parameter coupling (normal and acceptable)
//    Object1 is coupled to Object2 if Object1 passes Object2 only primitive data through a parameter list
// 2) object-parameter coupling (not too good)
//    Object1 is coupled to Object2 if Object1 passes Object3 to Object2
//    this coupling is tighter than Object1 passes Object2 only primitive data types through a parameter list
//      because it requires Object1 to know about Object3 (Object1 is coupled to Object3 as well)
// 3) simple-object coupling (normal and acceptable)
//    Object1 is coupled to Object2 if Object1 instantiates Object2
// 4) semantic coupling (bad)
//    one object makes use not of some syntactic element of another object but of some semantic
//      knowledge of another object's inner workings
//   ex.
//   a) Module1 passes a control flag to Module2 that tells Module2 what to do
//      this requires Module1 to make assumptions about the internal workings of Module2
//      i.e. Module2 needs to know what to do with the control flag
//   b) Module2 uses global data after the global data has been modified by Module1
//      this requires Module2 to assume that Module1 has modified the data Module2 needs
//   c) Module1 passes Object to Module2, and Module1 needs to know Module2 uses only 3 of Object's 7 methods
//      it initializes Object only partially with the specific data those three methods need
//   d) Module1 passes BaseObject to Module2 and Module2 needs to know Module1 is really passing it DerivedObject
//      it casts BaseObject to DerivedObject and calls methods that are specific to DerivedObject
//
// - Build Hierarchies
// a tiered information structure: most general/abstract representation is at the top
//   increasingly detailed, specialized representations are at lower levels
// used for managing complex sets of information
//
// - Assign Responsibilities
//   what each object should be responsible for ~= what information it should hide
