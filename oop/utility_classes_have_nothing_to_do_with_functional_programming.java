// Utility Classes Have Nothing to Do With Functional Programming
//   functional programming:
//     declarative: focuses on what the program should accomplish without prescribing how to do it
//       (the client only knows of the interface the object subscribed)
//     a function can be assigned to a variable (bade on lambda calculus)
//   utility class methods:
//     imperative: ex. Math or StringUtils return products ready to be used immediately
//     you can't pass a static method as an argument to another method
//       (they are procedures, i.e. Java statements grouped under a unique name)
//
// why are utility class methods bad?
//   Testability: calls to static methods in utility classes are hard-coded dependencies
//     there is no way to replace them with test-doubles when testing
//     ex. calling FileUtils.readFile() cannot be tested without a real file on disk
//   Efficiency: utility class methods are less efficient
//     ex. StringUtils.split() breaks the string down right now, even if only the first one is required later
//     (declarative programming instead returns a promise and may gain performance based on the usage)
//   Readability: utility classes tend to be huge
//     ex. StringUtils or FileUtils
//
// example:
//
// (bad desgin)

public class Math {

    public static double abs(double a);
}

// the client code
double x = Math.abs(3.1415926d);

// (good design)

