// mocking http server for unit and integration testing of your HTTP clients
//
// example: Jcabi server component

// create an instance of MkContainer, which has methods: next(MkAnswer) and start()
// it works as an HTTP server with a FIFO queue for HTTP answers
// when the queue is empty, all requests causes HTTP responses with internal server error 500
MkContainer container = new MkGrizzlyContainer()
    .next(new MkAnswer.Simple("hello, world!"))
    .start();

try {
    // home() returns a URL of its homepage, the server then binds itself to a randomly allocated TCP port
    // make an HTTP request to the started server to test if we get the expected response 
    new JdkRequest(container.home())
        .header("User-agent", "Myself")
        .fetch()
        .assertBody(Matchers.containsString("hello"));
} finally {
    // server starts on start() call and stops on stop()
    container.stop();
}

// test if the server indeed get the http query
MkQuery query = container.take();
MatcherAssert.assertThat(
    query.headers().get("User-agent"),
    Matchers.hasItem("Myself")
);
