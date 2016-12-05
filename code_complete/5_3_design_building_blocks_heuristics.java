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
// class interfaces should provide a consistent abstraction
//
// - Encapsulate Implementation Details
//
// - Inherit when Inheritance Simplifies the Design
// 1) define a base class that specifies common elements of multiple derived classes
//    it makes code reused but create coupling subclasses
// 2) adhere to the Liskov Substitution Principle (LSP)
//    do not inherit from a base class unless derived class truly "is a" more specific version of base class
//    subclasses must be usable through base class interface without user needs to know the difference
//    ex. base class: Account
//        derived classes: CheckingAccount, SavingsAccount,
// 3) the client code should always program to the base class or interface (not thinking about subclass details)
// 4) containment is preferable to inheritance unless you're modeling an IS_A relationship
// 5) inheritance is a useful tool, but it adds complexity
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
// 3) class interface should hide something: a system interface, a design decision, or an implementation detail
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
// 4) semantic coupling (bad: tightly coupled to an object's implementation details)
//    Object1 makes use not of some syntactic element of Object2 but of some semantic knowledge of Object2's
//      inner workings
//   ex.
//   a) Object1 passes a control flag to Object2 that tells Object2 what to do
//      this requires Object1 to make assumptions about the internal workings of Object2
//   b) Object1 uses global data after the global data has been modified by Object2
//      this requires Object1 to assume that Object2 has modified the data Object1 needs
//   c) Object1 passes Object3 to Object2, and Object1 knows that Object2 uses only 3 out of Object3's 7 methods
//      it initializes Object3 only partially with the specific data those 3 methods need
//   d) Object1 accepts a BaseObject as parameter but Object2 is really passing it DerivedObject
//      Object1 knows about it, casting the BaseObject to DerivedObject and calling methods that are specific to DerivedObject
//
// - Build Hierarchies
// a tiered information structure: most general/abstract representation is at the top
//   increasingly detailed, specialized representations are at lower levels
// used for managing complex sets of information
//
// - Assign Responsibilities
//   what each object should be responsible for ~= what information it should hide
//
// - Identify Areas Likely to Change
// 1) identify items that seem likely to change
// 2) separate items that are likely to change
//    put componenets that likely to change at the same time into its own class
// 3) isolate items that seem likely to change
//    design the interclass interfaces to be insensitive to the potential changes
