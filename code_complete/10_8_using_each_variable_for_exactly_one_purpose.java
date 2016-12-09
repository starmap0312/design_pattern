// principles
// 1) each object has one and only one purpose

// ex. (bad design: one object with two purposes)
// Compute roots of a quadratic equation
temp = Sqrt( b*b - 4*a*c );
root[O] = ( -b + temp ) / ( 2 * a );
root[1] = ( -b - temp ) / ( 2 * a );
// swap the roots
temp = root[0];
root[0] = root[1];
root[1] = temp;

// ex. (good design: use one object)
// Compute roots of a quadratic equation.
// This code assumes that (b*b-4*a*c) is positive.
discriminant = Sqrt( b*b - 4*a*c );
root[0] = ( -b + discriminant ) / ( 2 * a );
root[1] = ( -b - discriminant ) / ( 2 * a );
// swap the roots
oldRoot = root[0];
root[0] = root[1];
root[1] = oldRoot;

// 2) Principle of Proximity
//    a) declare object close to where it's first used
//    b) initialize object when it's declared, or at least close to where it's first used
//    c) no uninitialized objects

// ex. C++ Example of Initialization at Declaration Time
float studentGrades[MAX_STUDENTS] = { 0.0 };

// ex. Java Example of Good Initialization

int accountIndex = 0;
// code using accountIndex
double total = 0.0;
// code using total
boolean done = false;
// while-loop using done
while (!done) {
    // ...
    if (...) done = true;
}

// 3) objects should have the smallest scope/visibility
//    a) minimize the scope of each object (short live time) 
//       ex. inside a block, new an object in C++ (live until delete), static object in C++ (life of program)
//           forever (external resource: database, file, etc.)
//       global object is more flexible, but increases complexity and managing difficulty 
//    b) keep object local to a routine or class
//       i.e. a block < a routine < a class < whole program (bad: global object)
//    easier to refactor/manage code, increase readability, avoid coupling, hide information
// 4) keep references to objects close together: improve readability

int receiptIndex = 0;
float dailyReceipts = TodaysReceipts();
double totalReceipts = TotalReceipts( dailyReceipts );
