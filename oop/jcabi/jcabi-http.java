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
    private final transient Wire wire;

    // Public ctor.
    // @param uri The resource to work with
    // @param method HTTP method
    // @param cnct Connect timeout for http connection
    BaseRequest(final Wire wre, final String uri, final String method, final byte[] body, final int cnct) {
        this.wire = wre;
        URI addr = URI.create(uri);
        if (addr.getPath().isEmpty()) {
            addr = UriBuilder.fromUri(addr).path("/").build();
        }
        this.home = addr.toString();
        this.mtd = method;
        this.content = body.clone();
        this.connect = cnct;
    }

    public Request method(final String method) { // return New alternated request
        return new BaseRequest(this.wire, this.home, method, 0);
    }

    public Request timeout(final int cnct) { // return New alternated request
        return new BaseRequest(this.wire, this.home, this.mtd, cnct);
    }

    public Response fetch() throws IOException {
        return this.fetchResponse(new ByteArrayInputStream(this.content));
    }

    /*
     * Fetch response from server.
     * @param stream The content to send.
     * @return The obtained response
     */
    private Response fetchResponse(final InputStream stream) throws IOException {
        final long start = System.currentTimeMillis();
        final Response response = this.wire.send(
            this, this.home, this.mtd,
            stream, this.connect
        );
        final URI uri = URI.create(this.home);
        return response;
    }
}

public interface Wire {

    /*
     * Send request and return response.
     * @param req Request
     * @param home URI to fetch
     * @param method HTTP method
     * @param content HTTP body
     * @param connect The connect timeout
     * @return Response obtained
     */
    Response send(Request req, String home, String method, InputStream content, int connect) throws IOException;
}

public class BaseWire implements Wire {

    @Override
    public Response send(final Request req, final String home, final String method,
        final InputStream content, final int connect) throws IOException {

        final CloseableHttpResponse response = HttpClients.createSystem().execute(
            this.httpRequest(home, method, content, connect)
        );

        try {
            return new DefaultResponse(
                req,
                response.getStatusLine().getStatusCode(),
                this.consume(response.getEntity())
            );
        } finally {
            response.close();
        }
    }

    private byte[] consume(final HttpEntity entity) throws IOException {
        final byte[] body;
        if (entity == null) {
            body = new byte[0];
        } else {
            body = EntityUtils.toByteArray(entity);
        }
        return body;
    }
};

public class BaseWireImpl implements Wire {

    @Override
    public Response send(final String home, final String method, final int connect) throws IOException {
        final HttpURLConnection conn = HttpURLConnection.class.cast(new URL(home).openConnection());
        try {
            conn.setConnectTimeout(connect);
            conn.setReadTimeout(read);
            conn.setRequestMethod(method);
            return new DefaultResponse(
                req,
                conn.getResponseCode(),
                conn.getResponseMessage()
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

    public DefaultResponse(final Request request, final int status, final byte[] body) {
        this.req = request;
        this.code = status;
        this.content = body.clone();
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

abstract class AbstractResponse implements Response {

    /*
     * Encapsulated response.
     */
    private final transient Response response;

    /*
     * Ctor.
     * @param resp Response
     */
    AbstractResponse(final Response resp) {
        this.response = resp;
    }

    public final Request back() {
        return this.response.back();
    }

    public final int status() {
        return this.response.status();
    }

    public final byte[] binary() {
        return this.response.binary();
    }

    public final <T extends Response> T as(final Class<T> type) {
        return this.response.as(type);
    }

}

/* This response decorator is able to parse HTTP response body as
 * a JSON document and manipulate with it afterwords
 *
 * String name = new JdkRequest("http://my.example.com")
 *     .header(HttpHeaders.ACCEPT, MediaType.APPLICATION_JSON)
 *     .fetch()
 *     .as(JsonResponse.class)
 *     .json()
 *     .readObject()
 *     .getString("name");
 */
public final class JsonResponse extends AbstractResponse {

    // Read body as JSON.
    // @return Json reader
    public JsonReader json() {
        final byte[] body = this.binary();
        final String json;
        try {
            json = new String(body, "UTF-8");  // read the raw content
        } catch (final UnsupportedEncodingException ex) {
            throw new IllegalStateException(ex);
        }
        return new JsonResponse.VerboseReader( // wrap the parsed content into an JsonReader
            Json.createReader(
                new StringReader(
                    JsonResponse.escape(json)  // do some parsing on the raw content
                )
            ),
            json
        );
    }
    /*
     * Escape control characters in JSON parsing.
     *
     * @param input The input JSON string
     * @return Escaped JSON
     */
    private static String escape(final CharSequence input) {
        final Matcher matcher = JsonResponse.CONTROL.matcher(input);
        final StringBuffer escaped = new StringBuffer(input.length());
        while (matcher.find()) {
            matcher.appendReplacement(
                escaped,
                String.format("\\\\u%04X", (int) matcher.group().charAt(0))
            );
        }
        matcher.appendTail(escaped);
        return escaped.toString();
    }
}

