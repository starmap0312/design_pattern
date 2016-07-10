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
#
# example:
#
# (bad design)
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
#           } catch (IOException ex) {
#               ex.printStackTrace();
#           }
#       }
#   }
#
#   // the client code: the error information is hidden from the client (can't trust the send() method anymore)
#   new Wire(stream).send(1);
#
