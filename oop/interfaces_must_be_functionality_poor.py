# interfaces must be functionality poor
#
# example: interface InputStream
#
# (bad design: the interface has many overloaded methods)
#
#   abstract class InputStream {
#       int read();                                      // read a single byte
#       int read(byte[] buffer, int offset, int length); // read arbitrary bytes at a specific place
#       int read(byte[] buffer);                         // read an array of bytes
#   }
#   // the interface expands as the functionalities grow, so every implementation must implement all methods
#   
#   // the client code
#   // FileInputStream is an implementation of InputStream
#   final InputStream input = new FileInputStream("/tmp/a.txt");
#   final byte b = input.read();
#
# (good design: the interface has a single method)
#
#   // if wante extra functionality, create supplementary classes with an additional method (i.e. adapters)
#   // i.e. keep the interface simple, and let adapters extend the functionality
#   interface InputStream {
#
#     int read(byte[] buffer, int offset, int length);
#
#   }
#   
#   // to add a functionality, create a supplementary class that works like an adapter 
#   interface InputStream {
#
#       int read(byte[] buffer, int offset, int length);
#
#       class SingleByte { // the supplmentary class does not have to implement the interface
#
#           private final InputStream origin;
#
#           public SingleByte(InputStream stream) { // it works like an adapter
#               this.origin = stream;
#           }
#
#           // adapt read(byte[], int, int) to method read(), which reads a single byte from the buffer
#           public int read() {
#               final byte[] buffer = new byte[1];
#               final int read = this.origin.read(buffer, 0, 1);
#               final int result;
#               if (read < 1) {
#                   result = -1;
#               } else {
#                   result = buffer[0];
#               }
#               return result;
#           }
#       }
#   }
#   
#   // the client code
#   // FileInputStream is an implementation of InputStream
#   final InputStream input = new FileInputStream("/tmp/a.txt");
#   // the adapted object has an additional read() method to read in one single byte
#   final byte b = new InputStream.SingleByte(input).read();
#   
# why is it good?
# 1) the functionality of reading a single byte is outside of InputStream (it's not its business)
# 2) the stream doesn't need to know how to manage the data after it is read
#    i.e. the stream is responsible for is reading, not parsing or manipulating afterwards
# 
# rule of thumbs:
# 1) interfaces must be small
# 2) method overloading in interfaces is a code smell
# 3) an interface with more than three methods is a good candidate for refactoring

