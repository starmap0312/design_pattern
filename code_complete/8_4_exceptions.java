// exceptions weaken encapsulation
//   it requires the code that calls a routine to know which exceptions might be thrown inside the code called.
//   this increases code complexity
// throw exception at a consistent level of abstraction as routine interface's abstraction
//
// example:
//
// (bad design)
class Employee {

  public TaxId GetTaxId() throws EOFException { // EOFException is not consistent with Employee abstraction
      // ...
  }
}

// (good design)
class Employee {
  public TaxId GetTaxId() throws EmployeeDataNotAvailable { // EmployeeDataNotAvailable is consistent
      //...
  }
}
