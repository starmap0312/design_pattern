// use assertions to document assumptions made in the code and to flush out unexpected conditions
// ex.
//    an input parameter's value falls within its expected range
//    a file or stream is open (or closed) when a routine begins executing
//    the value of an input-only variable is not changed by a routine
//    a pointer is non-null
//    a table has been initialized to contain real values
// an assertion usually takes two arguments:
//   1) a boolean expression that describes the assumption supposed to be true
//   2) a message to display if it isn't
// guidelines for using assertions
//   error-handling vs. assertions
//   1) use error-handling code for conditions you expect to occur
//      checks for off-nominal circumstances that might not occur very often, but that have been
//        anticipated by the programmer and and need to be handled by the production code
//      checks for bad input data
//      enable the program to respond to the error gracefully
//   2) use assertions for conditions that should never occur
//      checks for bugs in the code: need to change the code and release a new version
//      think of assertions as executable documentation: you can't rely on them to make the code work, but
//        they can document assumptions more actively than comments can
//      use assertions to document and verify preconditions and postconditions
// design by contract:
//   1) preconditions are the client code's obligations to the code it calls
//   2) postconditions are the routine's or class's obligations to the code that uses it
 
// exmaple: C++ Assertion Macro
//
// #define ASSERT( condition, message ) {                         \
//     if ( !(condition) ) {                                      \
//         LogError( "Assertion failed: ", #condition, message ); \
//         exit( EXIT_FAILURE );                                  \
//     }                                                          \
// }
//
// example:
//
// (bad design: executable code in assertions)
Debug.Assert( PerformAction() ) "Couldn't perform action"
// dangerous use: compiler will eliminate the code when you turn off the assertions

// (good design)
actionPerformed = PerformAction()
Debug.Assert( actionPerformed ) "Couldn't perform action"

// example: routine's design is based on the assumption that values will be within valid ranges
Private Function Velocity (
    ByVal latitude As Single,
    ByVal longitude As Single,
    ByVal elevation As Single
    ) As Single

    // pre-conditions
    // option 1: assertions
    Debug.Assert ( -90 <= latitude And latitude <= 90 )
    Debug.Assert ( 0 <= longitude And longitude < 360 )
    Debug.Assert ( -500 <= elevation And elevation <= 75000 )

    // option 2: error-handling code
    // (values not within its valid range will be changed to the closest legal value)
    If ( latitude < -90 ) Then
        latitude = -90
    ElseIf ( latitude > 90 ) Then
        latitude = 90
    End If
    If ( longitude < 0 ) Then
        longitude = 0
    ElseIf ( longitude > 360 ) Then
    // ...

    // post-conditions: assertions
    Postconditions Debug.Assert ( 0 <= returnVelocity And returnVelocity <= 600 )
    return value
    Velocity = returnVelocity
End Function

