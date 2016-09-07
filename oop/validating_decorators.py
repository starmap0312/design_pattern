# defensive programming via validating decorators
#   ex. used for validating the input parameters of a method
# benefits: make the classes small and cohesive, and more reusable
#
# example:
#
#  (bad design: both the validation and export functionality are written in one class)
#
#  class Report {
#
#      void export(File file) {
#          if (file == null) {
#              throw new IllegalArgumentException("File is NULL; can't export.");
#          }
#          if (file.exists()) {
#              throw new IllegalArgumentException("File already exists.");
#          }
#          // Export the report to the file
#    }
#
#  }
#  
#  (good desing: use validating decorators)
#  // the core object will do the reporting, while the decorators will validate parameters
#  
#  interface Report {
#
#      void export(File file);
#  }
#
#  // the export functionality is implemented in the decoratee class
#  class DefaultReport implements Report {
#
#      @Override
#      void export(File file) {
#          // Export the report to the file
#      }
#
#  }
#  
#  // a validating class
#  class NoWriteOverReport implements Report {
#
#      private final Report origin;
#
#      NoWriteOverReport(Report rep) {
#          this.origin = rep;
#      }
#
#      @Override
#      void export(File file) {
#          if (file.exists()) {
#              throw new IllegalArgumentException("File already exists.");
#          }
#          this.origin.export(file);
#      }
#  }
#  
#  // the client code that uses decorators
#  Report report = new NoNullReport(new NoWriteOverReport(new DefaultReport()));
#  report.export(file);
#  
#  
