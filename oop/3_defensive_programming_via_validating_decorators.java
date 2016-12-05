// defensive programming via validating decorators
//   used for validating the input parameters of a method
//   benefits: make the classes small and cohesive, and more reusable
//
// example:
//
// (bad design: both the validation and export functionality are written in one class)

class Report {

    void export(File file) {
        if (file == null) {  // first validation: file is NULL
            throw new IllegalArgumentException("File is NULL; can't export.");
        }
        if (file.exists()) { // second validation: file already exists
            throw new IllegalArgumentException("File already exists.");
        }
        // main responsibility of the object: export the report to the file
    }

}

//  (good design: distribute responsibilities to validating decorators)
// the core object will do the reporting, while the decorators will validate parameters

interface Report {

    void export(File file);
}

class DefaultReport implements Report { // default implmentation of Report

    void export(File file) {
        // Export the report to the file
    }
}

// a validating class
class NoNullReport implements Report {

    private final Report origin;

    NoNullReport(Report rep) {
        this.origin = rep;
    }

    void export(File file) {
        if (file == null) {       // validation: file is NULL
            throw new IllegalArgumentException("File is NULL; can't export.");
        }
        this.origin.export(file); // delegates the export to the derocatee
    }
}

// a validating class
class NoWriteOverReport implements Report {

    private final Report origin;

    NoWriteOverReport(Report rep) {
        this.origin = rep;
    }

    void export(File file) {
        if (file.exists()) {      // validation: file already exists
            throw new IllegalArgumentException("File already exists.");
        }
        this.origin.export(file); // delegates the export to the derocatee
    }
}

// the client code that uses decorators
Report report = new NoNullReport(new NoWriteOverReport(new DefaultReport()));
report.export(file);

