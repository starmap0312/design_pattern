// - Find Real-world Objects
// 1) identify object and its attributes (characteristics)
// 2) determine its public and private parts (waht parts will be visible to other objects)
//    information hiding: for encapsulation, modularity, and abstraction
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
// - Inherit When Inheritance Simplifies The Design
// define a base class that specifies common elements of multiple derived classes
//   it makes code reused but create coupling subclasses
// adhere to the Liskov Substitution Principle (LSP)
//   do not inherit from a base class unless derived class truly "is a" more specific version of base class
//   subclasses must be usable through base class interface without user needs to know the difference
//   ex. base class: Account, and derived classes: CheckingAccount, SavingsAccount,
// the client code should always program to the base class or interface (not thinking about subclass details)
//
// - Information Hiding
// 1) good hiding can reduce the amount of code affected by a change
// 2) useful at all levels of design:
//    a) named constants instead of literals
//       ex. use a named constant MAX_EMPLOYEES to hide 100
//       ex. use id = NewId() to hide id = ++g_maxId
//    b) creation of data types: improve code design and readability
//       ex. use a new class type ID to hide int
//    c) class design, routine design, and subsystem design
//
// - Identify Areas Likely to Change
// isolate unstable areas so that the effect of a change will be limited to one routine, class, or package
// 1) Status variables
//    ex. an enumerated type with values: ErrorType_None, ErrorType_Warning, and ErrorType_Fatal
//    use access routines rather than checking the variable directly
//
// - Keep Coupling Loose
// kinds of coupling
// 1) simple-data-parameter coupling (normal and acceptable)
//    two modules are coupled if all data passed between them are primitive and through parameter lists
// 2) simple-object coupling (normal and acceptable)
//    a module is coupled to an object if it instantiates that object
// 3) object-parameter coupling (not good)
//    two modules are coupled if Object1 requires Object2 to pass it an Object3
//    this coupling is tighter than Object1 requiring Object2 to pass it only primitive data types
//      because it requires Object2 to know about Object3
// 4) semantic coupling (bad)
//    one module makes use not of some syntactic element of another module but of some semantic
//      knowledge of another module's inner workings (not good)
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
