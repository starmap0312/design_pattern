public interface Request {

    String GET = "GET";
    String POST = "POST";

    // Get destination URI: @return The destination it is currently pointing to
    RequestURI uri();

    // Get request body: @return New alternated request
    RequestBody body();

    // Set method
    // @param method The method to use
    // @return New alternated request
    Request method(String method);

    // Set timeout
    // @param connect The connect timeout to use in ms
    // @param read The read timeout to use in ms
    // @return New alternated request
    Request timeout(int connect, int read);

    // Execute it with a specified HTTP method.
    // @return Response
    // @throws IOException If fails to fetch HTTP request
    Response fetch() throws IOException;
}

final class BaseRequest implements Request {

    private static final String ENCODING = "UTF-8"; // define a constant string for the class
    private final transient byte[] content;

    // Public ctor.
    // @param uri The resource to work with
    // @param method HTTP method
    // @param cnct Connect timeout for http connection
    // @param rdd Read timeout for http connection
    BaseRequest(final String uri, final String method, final byte[] body, final int cnct, final int rdd) {
        URI addr = URI.create(uri);
        if (addr.getPath().isEmpty()) {
            addr = UriBuilder.fromUri(addr).path("/").build();
        }
        this.home = addr.toString();
        this.mtd = method;
        this.content = body.clone();
        this.connect = cnct;
        this.read = rdd;
    }

    public Request method(final String method) { // return New alternated request
        return new BaseRequest(this.home, method, 0, 0);
    }

    public Request timeout(final int cnct, final int rdd) { // return New alternated request
        return new BaseRequest(this.home, this.mtd, cnct, rdd);
    }

    public Response fetch() throws IOException {
        return this.fetchResponse(new ByteArrayInputStream(this.content));
    }

    /*
     * Fetch response from server.
     * @param stream The content to send.
     * @return The obtained response
     * @throws IOException If an IO exception occurs.
     */
    private Response fetchResponse(final InputStream stream) throws IOException {
        final long start = System.currentTimeMillis();
        final Response response = this.wire.send(
            this, this.home, this.mtd,
            this.hdrs, stream, this.connect,
            this.read
        );
        final URI uri = URI.create(this.home);
        return response;
    }

    public Response fetch() throws IOException {
        return this.fetchResponse(new ByteArrayInputStream(this.content));
    }
}


class Wire {

    public Response send(final String home, final String method, final int connect, final int read)
        throws IOException {
        final HttpURLConnection conn = HttpURLConnection.class.cast(new URL(home).openConnection());
        try {
            conn.setConnectTimeout(connect);
            conn.setReadTimeout(read);
            conn.setRequestMethod(method);
            return new DefaultResponse(
                req,
                conn.getResponseCode(),
                conn.getResponseMessage(),
            );
        } catch (final IOException exp) {
            throw new IOException(String.format("Failed %s request to %s", method, home), exp);
        } finally {
            conn.disconnect();
        }
    }
}


// interface
public interface Response {

    // Get back to the request it's related to.
    // @return The request we're in
    Request back();

    // Get status of the response as a positive integer number.
    // @return The status code
    int status();

    // Raw body as a an array of bytes.
    // @return The body, as a UTF-8 string
    byte[] binary();

    // Convert it to another type, by encapsulation.
    // @param type Type to use
    // @param <T> Type to use
    // @return New response
    <T extends Response> T as(Class<T> type);

}

public final class DefaultResponse implements Response {

    public DefaultResponse(final Request request, final int status) {
        this.req = request;
        this.code = status;
    }

    public Request back() {
        return this.req;
    }

    public int status() {
        return this.code;
    }

    public byte[] binary() {
        return this.content.clone();
    }

    public <T extends Response> T as(final Class<T> type) {
        try {
            return type.getDeclaredConstructor(Response.class)
                .newInstance(this);
        } catch (final InstantiationException
            | IllegalAccessException | NoSuchMethodException
            | InvocationTargetException ex) {
            throw new IllegalStateException(ex);
        }
    }
}


public final class JsonResponse extends AbstractResponse {

    // Read body as JSON.
    // @return Json reader
    public JsonReader json() {
        final byte[] body = this.binary();
        final String json;
        try {
            json = new String(body, "UTF-8");
        } catch (final UnsupportedEncodingException ex) {
            throw new IllegalStateException(ex);
        }
        return new JsonResponse.VerboseReader(
            Json.createReader(
                new StringReader(
                    JsonResponse.escape(json)
                )
            ),
            json
        );
    }

}

