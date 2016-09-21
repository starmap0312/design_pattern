// primary and secondary constructors
// 1) primary constructor: the one that constructs an object and encapsulates other objects inside it
// 2) secondary constructor: a preparation step before calling a primary constructor
//
// example
//
// (good design)

final class Cash {

    private final int cents;
    private final String currency;

    public Cash() { // a secondary constructor
        this(0);
    }

    public Cash(int cts) { // another secondary constructor
        this(cts, "USD");
    }

    public Cash(int cts, String crn) { // only one primary constructor
        this.cents = cts;
        this.currency = crn;
    }

  // methods here
}

// rule of thumb:
//   only one primary constructor, which should be declared after all secondary ones
//     all classes should have a single entry point (point of construction), i.e. one primary constructor
//     this helps eliminate code duplication
//
// (bad design)

final class Cash {

    private final int cents;
    private final String currency;

    public Cash() { // primary
        this.cents = 0;
        this.currency = "USD";
    }

    public Cash(int cts) { // primary
        this.cents = cts;
        this.currency = "USD";
    }

    public Cash(int cts, String crn) { // primary
        this.cents = cts;
        this.currency = crn;
    }
    // methods here
}

// in python, you cannot define multiple constructors
// however, you can define a default value if one is not passed
//
// example:
//
// def __init__(self, cents=0, currency="USD"):
//     self.cents = cents
//     self.currency = currency

