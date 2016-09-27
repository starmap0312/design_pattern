// How Much Your Objects Encapsulate
//   a good object is a representative of a real-life entity
//   what is that real-life entity
//     the answer is given by the list of arguments its constructors accept
//     all arguments passed into constructor and encapsulated by the object
//       identify a real-life entity accessed and managed by the object
//
// example:
//
// the object represents a HTTP web page
new HTTP("http://www.google.com").read();

// the object represents the HTTP Universe
new HTTP().read("http://www.google.com");

// which one is better?
//   it depends, but the smaller the real-life entity it represents, the more cohesive the object is


// situation when an object that represents the HTTP Universe is better
class HTTP {

    public String read(String url) { // the object can read any web page from the entire web
        // read an HTTP web page
    }

    public boolean online() { // the object can check whether the entire web is accessible by it
        // check whether we're online
    }
}

// objects representing the Universe are not good enough
//   because there is only one Universe, so why do we need many representatives (objects) of it
