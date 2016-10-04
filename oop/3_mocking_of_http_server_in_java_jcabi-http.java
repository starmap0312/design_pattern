// Mocking of HTTP Server in Java
//   a server component of jcabi-http for mocking http server for unit and integration testing of HTTP clients
//
// example: Jcabi server component

// create an instance of MkContainer, which has methods: next(MkAnswer) and start()
// it works as an HTTP server with a FIFO queue for HTTP answers
// when the queue is empty, all requests causes HTTP responses with internal server error 500
MkContainer container = new MkGrizzlyContainer()
    .next(new MkAnswer.Simple("hello, world!"))  // add answers: a first-in-first-out queue
    .start();
// the server will return "hello, world!" to first request
// all subsequent requests will cause HTTP responses with status "internal server error 500"

try {
    // make an HTTP request to the started server to test if we get the expected response 
    new JdkRequest(container.home())    // home() returns a URL of homepage: server then binds to random TCP port
        .header("User-agent", "Myself")
        .fetch()
        .assertBody(Matchers.containsString("hello"));
} finally { // stop the container safely; otherwise, the container will be killed together with the JVM
    container.stop(); // server stops
}

// test if server side indeed gets the http query: using hamcrest for assertions
MkQuery query = container.take();
MatcherAssert.assertThat(
    query.headers().get("User-agent"), // get all headers of the HTTP request
    Matchers.hasItem("Myself") // assert that "User-Agent" header was there and at least one equal to "Myself"
);
// an instance of MkQuery exposes information about the query made
