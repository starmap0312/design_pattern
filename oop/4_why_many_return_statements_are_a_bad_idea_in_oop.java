// in a pure object-oriented world, a method must have a single return statement 
//
// example:
//
// (bad design: a method with two return statements)

public int max(int a, int b) {
    if (a > b) {
        return a;                // <== first return statement
    }
    return b;                    // <== second return statement
}

// (refinement: modify the code to have only one return statement)
//
// more verbose, less readable, and slower

public int max(int a, int b) {
    int m;
    if (a > b) {
        m = a;
    } else {
        m = b;
    }
    return m;                  //  <== only one return statement
}

// (good design: pure oop design)
// use objects of class If and GreaterThan

public int max(int a, int b) {
    return new If(new GreaterThan(a, b), a, b);
}

