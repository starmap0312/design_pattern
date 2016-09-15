# immutablity: does not allow any modifications to the encapsulated entity
  different levels of immutablity: objects are immutable but their behaviors differ

  1) constant: always returns the same
     ex.
     class Book {

         private final String ttl;

         Book rename(String title) {
             return new Book(title);
         }

         String title() {
             return this.ttl;
         }
     }

     ttl is final, and title() always return the same value, i.e. a pure function

  2) not a constant: returns different values if called multiple times 
     ex.
     class Book {

         private final String ttl;

         Book rename(String title) {
             return new Book(title);
         }

         String title() {
             return String.format("%s (as of %tR)", this.ttl, new Date());
         }
     }

  3) represented mutability: not constnat, i.e. may return different values
                             moreover, the represented entity (the file) is not a constant
     ex.
     class Book {

         private final Path path;

         Book rename(String title) {
             Files.write(this.path, title.getBytes(), StandardOpenOption.CREATE);
             return this;
         }

         String title() {
             return new String(Files.readAllBytes(this.path));
         }
     }

