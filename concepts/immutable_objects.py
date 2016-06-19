#  immutable objects
#
#    an object is immutable if its state can't be modified after it is created
#
#  advantages
#
#    1) immutable objects are simpler to construct, test, and use
#    2) truly immutable objects are always thread-safe
#    3) help to avoid temporal coupling
#    4) their usage is side-effect free (no defensive copies)
#    5) identity mutability problem is avoided
#    6) always have failure atomicity
#    7) much easier to cache
#    8) prevent NULL references
#
#  thread-safe
#
#    1) multiple threads can access the same object at the same time, without clashing with another thread
#    2) no object methods can modify its state, so the object methods can be called in parallel
#       the object methods will work in their own memory space in stack
#
#  avoiding temporal coupling
#
#    temporal coupling: there is some hidden information in the code that a programmer has to remember
#
#    ex.
#
#    (bad design: mutable objects)
#
#    Request request = new Request("http://example.com");
#    request.method("POST");                               // this object state is set for both requests
#    String first = request.fetch();                       // first HTTP request
#    request.body("text=hello");                           // this object state is set for the second request
#    String second = request.fetch();                      // second HTTP request
#
#    // mutable objects create temporal coupling
#    // i.e. if you decide to remove the first HTTP request, we must remember not to remove 
#    //      request.method("POST")
#
#    Request request = new Request("http://example.com");
#    // request.method("POST");                            // may accidentally remove the line
#    // String first = request.fetch();                    // remove the first request
#    request.body("text=hello");
#    String second = request.fetch();
#
#    // the compiler won't complain, and the code just break
#
#    (good design: immutable objects)
#
#    final Request request = new Request("");               // an immutable object
#    String first = request.method("POST").fetch();
#    String second = request.method("POST").body("text=hello").fetch();
#
#    // removing either request won't affect the other, i.e. decoupling
#
#    (futher improvement: get rid of code duplication)
#
#    final Request request = new Request("");
#    final Request post = request.method("POST");           // an immutable object
#    String first = post.fetch();
#    String second = post.body("text=hello").fetch();

