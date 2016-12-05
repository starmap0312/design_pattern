// interface should be small
//
// ex.
//
// (bad design: an interface with overloading methods)

abstract class InputStream {
    int read();                                       // read a single byte
    int read(byte[] buffer);                          // read an array of bytes
    int read(byte[] buffer, int offset, int length);  // read an array of specified bytes at a specified offset
}

// (good design: an interface with only one method)

interface InputStream {
    int read(byte[] buffer, int offset, int length); // the interface has only one method
}                                                    // responsible for reading bytes from the stream


// if need new funcationality, don't add it to the interface, but create supplementary "smart" class

interface InputStream {

    int read(byte[] buffer, int offset, int length); // the interface has only one method

    class SingleByte { // a supplementary class that works like a adapter: read(byte[], int, int) => read()

        private final InputStream origin;

        public SingleByte(InputStream stream) {
            this.origin = stream;
        }

        public int read() { // define a read() method, with no input parameter, which reads a single byte
            final byte[] buffer = new byte[1];
            final int read = this.origin.read(buffer, 0, 1);
            final int result;
            if (read < 1) {
                result = -1;
            } else {
                result = buffer[0];
            }
            return result;
        }
    }
}

// the client code
final InputStream input = new FileInputStream("/tmp/a.txt");
final byte b = new InputStream.SingleByte(input).read();     // read a single byte from the file input stream

// why is it good?
//   the functionality of reading a single byte is outside of InputStream (it's not its business)
//   i.e. the InputStream doesn't need to know how to manage the data after it is read
//        it is responsible only for its reading, not parsing or manipulating afterwards (more cohesive)
// 
// rule of thumbs:
// 1) interfaces must be small: method overloading in interfaces is a code smell
// 2) an interface with more than three methods is a good candidate for refactoring
