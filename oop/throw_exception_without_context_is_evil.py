# Exception
# 1) used to simplify our design by moving the entire error handling code away from the logic
# 2) the design is simplified, and we only need to concentrate in one place
#    i.e. the main() method: the entry point of the entire app
# 3) the primary purpose of an exception is to collect as much information as possible about the error
#    float the exception up to the highest level, where the user is capable of doing something about it
# 4) exception chaining: putting our bubble (exception) into a bigger bubble every time we catch it & re-throw
#
# rule of thumbs:
# 1) don't catch an exception without re-throwing it
#    otherwise, you are hiding potentially important information, breaking the chain of trust between objects
# 2) catch exceptions as seldom as possible
# 3)throwing exceptions without proper context is bad
#
# example:
#
# (bad design: catch an exception without re-throwing it)
#
#   final class Wire {
#
#       private final OutputStream stream;
#
#       Wire(final OutputStream stm) {
#           this.stream = stm;
#       }
#
#       public void send(final int data) {
#           try {
#               this.stream.write(x);
#           } catch (IOException ex) { // the object catches the exception without re-throwing it
#               ex.printStackTrace();
#           }
#       }
#   }
#
#   // the client code: does know if an exception happens or not
#   new Wire(stream).send(1);
#
#   // the error information is hidden from the client
#   //   we can't trust the object anymore, as we don't know what's going on when exception happens
#
# (good design: don't catch exceptions unless you want to add more information and re-throw it)
#
#   final class Wire {
#
#       private final OutputStream stream;
#
#       Wire(final OutputStream stm) {
#           this.stream = stm;
#       }
#
#       public void send(final int data) throws IOException {
#           this.stream.write(x);
#       }
#   }
#
#   // the client code: there only one entry-point for handling the exceptions and the client knows about it 
#   try {
#       new Wire(stream).send(1);
#   } catch (IOException ex) {
#       ex.printStackTrace();
#   }
#
# example:
#
# (bad design: throw an exception without context)
#
# ex.
#
#   if (!file.exists()) {
#       throw new IllegalArgumentException("File doesn't exist");
#   }
#
# ex.
#
#   try {
#       Files.delete(file);
#   } catch (IOException ex) {
#       throw new IllegalArgumentException(ex);
#   }
#
# (good design: throw an exception with context/information)
#
#   ex.
#   if (!file.exists()) {
#       throw new IllegalArgumentException(
#           String.format(
#               "User profile file %s doesn't exist",
#               file.getAbsolutePath()
#           )
#       );
#   }
#
#   ex.
#   try {
#       Files.delete(file);
#   } catch (IOException ex) {
#       throw new IllegalArgumentException(
#           String.format(
#           "Can't delete user profile data file %s",
#           file.getAbsolutePath()
#           ),
#           ex
#       );
#   }
#
#   // an exception message must describe the problem and show as much detail as possible
#
# example: Java exception chaining
#
#   try {
#       try {
#           throw new Exception("One");
#       } catch (Exception e) {
#           throw new Exception("Two", e);    ==> add more information and re-throw the exception
#       }
#   } catch (Exception e) {
#       e.printStackTrace(System.out);        ==> print out the stack trace
#   }
