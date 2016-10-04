/*
 * 1) Github client, starting point to the entire library.
 *
 * Github github = new RtGithub(oauthKey);                // get github entry point by an oauthKey
 * Repo repo = github.repos().get(                        // get a repo by specifying user and repo name
 *     new Coordinates.Simple("jcabi/jcabi-github")
 * );
 * Issues issues = repo.issues();
 * Issue issue = issues.post("issue title", "issue body")
 *
 * 2) an entry point to the RESTful API
 *
 * Github github = new RtGithub(oauthKey);
 * int found = github.entry()                             // get the request entry
 *     .uri().path("/search/repositories").back()         // specify the request path
 *     .method(Request.GET)                               // specify the request method
 *     .fetch()                                           // fetch the response
 *     .as(JsonResponse.class)                            // decorates the response as Json format
 *     .getJsonObject()                                   // get the Json object
 *     .getNumber("total_count")                          // get the value by key "total_count"
 *     .intValue();                                       // convert the value into integer
 */

// interface
public interface Github {

    /*
     * RESTful request, an entry point to the Github API.
     * @return Request
     */
    Request entry();

    /*
     * Get repositories.
     * @return Repositories
     */
    Repos repos();

}

// interface
public interface Coordinates extends Comparable<Coordinates> {

    /*
     * Get usr name.
     * @return User name
     */
    String user();

    /*
     * Get rpo name.
     * @return Repo name
     */
    String repo();

    final class Simple implements Coordinates {
        /*
         * User name.
         */
        private final transient String usr;
        /*
         * Repository name.
         */
        private final transient String rpo;
        /*
         * Public ctor.
         * @param user User name
         * @param repo Repository name
         */
        public Simple(final String user, final String repo) {
            this.usr = user;
            this.rpo = repo;
        }
        /*
         * Public ctor.
         * @param mnemo Mnemo name
         */
        public Simple(final String mnemo) {
            final String[] parts = mnemo.split("/", 2);
            if (parts.length != 2) {
                throw new IllegalArgumentException(
                    String.format("invalid coordinates '%s'", mnemo)
                );
            }
            this.usr = parts[0];
            this.rpo = parts[1];
        }
        public String user() {
            return this.usr;
        }
        public String repo() {
            return this.rpo;
        }
}

// interface
public interface Repos {

    /*
     * Get its owner.
     * @return Github
     */
    Github github();

    /*
     * Get repository by name.
     * @param coords Repository name in "user/repo" format
     * @return Repository
     */
    Repo get(Coordinates coords);

    /*
     * Iterate all public repos, starting with the one you've seen already.
     * @param identifier The integer ID of the last Repo that you’ve seen.
     * @return Iterator of repo
     */
    Iterable<Repo> iterate(String identifier);
}

// interface
public interface Repo extends JsonReadable, JsonPatchable, Comparable<Repo> {

    /*
     * Get its owner.
     * @return Github
     */
    Github github();

    /*
     * Get its coordinates: user and repo name
     * @return Coordinates
     */
    Coordinates coordinates();

    /*
     * Iterate issues.
     * @return Issues
     */
    Issues issues();

    final class Smart implements Repo { // a decorator class
        /*
         * Encapsulated Repo.
         */
        private final transient Repo repo;
        /*
         * SmartJson object for convenient JSON parsing.
         */
        private final transient SmartJson jsn;
        /*
         * Public ctor.
         * @param rep Repo
         */
        public Smart(final Repo rep) {
            this.repo = rep;
            this.jsn = new SmartJson(rep);
        }
        /*
         * Get its description.
         * @return Description
         * @throws IOException If there is any I/O problem
         */
        public String description() throws IOException {
            return this.jsn.text("description");
        }
        public Github github() {
            return this.repo.github();
        }
        public Coordinates coordinates() {
            return this.repo.coordinates();
        }
        public Issues issues() {
            return this.repo.issues();
        }
        public JsonObject json() throws IOException {
            return this.repo.json();
        }
    }
}

/*
 * Github github = new RtGithub(oauthKey);
 * Repo repo = github.repos().get(
 *     new Coordinates.Simple("jcabi/jcabi-github")
 * );
 * Issues issues = repo.issues();
 * Issue issue = issues.create("issue title", "issue body");
 * issue.comments().post("issue comment");
 */
public final class RtGithub implements Github {

    /*
     * Default request to start with.
     */
    private static final Request REQUEST =
        new ApacheRequest("https://api.github.com")
            .header(HttpHeaders.USER_AGENT, RtGithub.USER_AGENT)
            .header(HttpHeaders.ACCEPT, MediaType.APPLICATION_JSON)
            .header(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON);

    /*
     * REST request.
     */
    private final transient Request request;

    /*
     * Public ctor, with a custom request.
     * @param req Request to start from
     * @since 0.4
     */
    public RtGithub(final Request req) {
        this.request = req;
    }

    /*
     * Public ctor, for anonymous access to Github.
     * @since 0.4
     */
    public RtGithub() {
        this(RtGithub.REQUEST);
    }

    /*
     * Public ctor, for HTTP Basic Authentication.
     * @param user User name
     * @param pwd Password
     */
    public RtGithub(final String user, final String pwd) {
        this(
            RtGithub.REQUEST.header(
                HttpHeaders.AUTHORIZATION,
                String.format(
                    "Basic %s",
                    DatatypeConverter.printBase64Binary(
                        String.format("%s:%s", user, pwd)
                            .getBytes(Charsets.UTF_8)
                    )
                )
            )
        );
    }

    public Request entry() {
        return this.request;
    }

    public Repos repos() {
        return new RtRepos(this, this.request);
    }
}

final class RtRepos implements Repos {

    /*
     * Github.
     */
    private final transient Github ghub;

    /*
     * RESTful entry.
     */
    private final transient Request entry;

    /*
     * Public ctor.
     * @param github Github
     * @param req Request
     */
    RtRepos(final Github github, final Request req) {
        this.ghub = github;
        this.entry = req;
    }

    public Github github() {
        return this.ghub;
    }

    public Repo get(final Coordinates name) {
        return new RtRepo(this.ghub, this.entry, name);
    }

    public Iterable<Repo> iterate(final String identifier) {
        return new RtPagination<Repo>(
            this.entry.uri().queryParam("since", identifier).back(),
            new RtValuePagination.Mapping<Repo, JsonObject>() {
                @Override
                public Repo map(final JsonObject object) {
                    return RtRepos.this.get(new Coordinates.Simple(object.getString("full_name")));
                }
            }
        );
    }
}

final class RtRepo implements Repo {

    /*
     * Github.
     */
    private final transient Github ghub;

    /*
     * RESTful entry.
     */
    private final transient Request entry;

    /*
     * RESTful request.
     */
    private final transient Request request;

    /*
     * Repository coordinates.
     */
    private final transient Coordinates coords;

    /*
     * Public ctor.
     * @param github Github
     * @param req Request
     * @param crd Coordinate of the repo
     */
    RtRepo(final Github github, final Request req, final Coordinates crd) {
        this.ghub = github;
        this.entry = req;
        this.coords = crd;
        this.request = this.entry.uri()    // set up the request by adding Coordinates: user and repo name
            .path("/repos")
            .path(this.coords.user())
            .path(this.coords.repo())
            .back();
    }

    public Github github() {
        return this.ghub;
    }

    public Coordinates coordinates() {
        return this.coords;
    }

    public Issues issues() {
        return new RtIssues(this.entry, this);
    }

    public JsonObject json() throws IOException {
        return new RtJson(this.request).fetch();
    }
}

// interface
public interface Issues {

    /*
     * Owner of them.
     * @return Repo
     */
    Repo repo();

    /*
     * Get specific issue by number.
     * @param number Issue number
     * @return Issue
     */
    Issue get(int number);

    /*
     * Create new issue.
     * @param title Title
     * @param body Body of it
     * @return Issue just created
     * @throws IOException If there is any I/O problem
     */
    Issue create(String title, String body) throws IOException;

    /*
     * Iterate them all.
     * @param params Iterating parameters, as requested by API
     * @return Iterator of issues
     */
    Iterable<Issue> iterate(Map<String, String> params);
}

/* example: Issue.Smart decorates Issue object to provide information, ex. title(), body(), etc. 
 *
 * Issue.Smart issue = new Issue.Smart(origin);
 * if (issue.isOpen()) {
 *     issue.close();
 * }
 */

// interface
public interface Issue extends Comparable<Issue>, JsonReadable, JsonPatchable {

    /*
     * Issue state.
     */
    String OPEN_STATE = "open", ex. title(), body(), etc.;

    /*
     * Issue state.
     */
    String CLOSED_STATE = "closed";

    /*
     * Repository we're in.
     * @return Repo
     */
    Repo repo();

    /*
     * Get its number.
     * @return Issue number
     */
    int number();

    /*
     * Get all comments of the issue.
     * @return Comments
     * @see <a href="http://developer.github.com/v3/issues/comments/">Issue Comments API</a>
     */
    Comments comments();

    final class Smart implements Issue { // a docorator of Issue object to provide information of the issue
        /*
         * Encapsulated issue.
         */
        private final transient Issue issue;
        /*
         * SmartJson object for convenient JSON parsing.
         */
        private final transient SmartJson jsn;
        /*
         * Public ctor.
         * @param iss Issue
         */
        public Smart(final Issue iss) {
            this.issue = iss;
            this.jsn = new SmartJson(iss);
        }
        /*
         * Open it (make sure it's open).
         * @throws IOException If there is any I/O problem
         */
        public void open() throws IOException {
            this.state(Issue.OPEN_STATE);
        }
        /*
         * Close it (make sure it's closed).
         * @throws IOException If there is any I/O problem
         */
        public void close() throws IOException {
            this.state(Issue.CLOSED_STATE);
        }
        /*
         * Get its title.
         * @return Title of issue
         * @throws IOException If there is any I/O problem
         */
        public String title() throws IOException { // provides information from its json object
            return this.jsn.text("title");
        }

        /*
         * Get its body.
         * @return Body of issue
         * @throws IOException If there is any I/O problem
         */
        public String body() throws IOException {
            return this.jsn.text("body");
        }

        public JsonObject json() throws IOException {
            return this.issue.json();
        }
    }
}

final class RtIssues implements Issues {

    /*
     * API entry point.
     */
    private final transient Request entry;

    /*
     * RESTful request.
     */
    private final transient Request request;

    /*
     * Repository.
     */
    private final transient Repo owner;

    /*
     * Public ctor.
     * @param req Request
     * @param repo Repository
     */
    RtIssues(final Request req, final Repo repo) {
        this.entry = req;
        final Coordinates coords = repo.coordinates();
        this.request = this.entry.uri()
            .path("/repos")
            .path(coords.user())
            .path(coords.repo())
            .path("/issues")
            .back();
        this.owner = repo;
    }

    public Repo repo() {
        return this.owner;
    }

    public Issue get(final int number) {
        return new RtIssue(this.entry, this.owner, number);
    }

    public Iterable<Issue> iterate(
        final Map<String, String> params) {
        return new RtPagination<Issue>(
            this.request.uri().queryParams(params).back(),
            new RtValuePagination.Mapping<Issue, JsonObject>() {
                @Override
                public Issue map(final JsonObject object) {
                    return RtIssues.this.get(object.getInt("number"));
                }
            }
        );
    }
}

final class RtIssue implements Issue {

    /*
     * API entry point.
     */
    private final transient Request entry;

    /*
     * RESTful request.
     */
    private final transient Request request;

    /*
     * Repository we're in.
     */
    private final transient Repo owner;

    /*
     * Issue number.
     */
    private final transient int num;

    /*
     * Public ctor.
     * @param req Request
     * @param repo Repository
     * @param number Number of the get
     */
    RtIssue(final Request req, final Repo repo, final int number) {
        this.entry = req;
        final Coordinates coords = repo.coordinates();
        this.request = this.entry.uri()
            .path("/repos")
            .path(coords.user())
            .path(coords.repo())
            .path("/issues")
            .path(Integer.toString(number))
            .back();
        this.owner = repo;
        this.num = number;
    }

    public Repo repo() {
        return this.owner;
    }

    public int number() {
        return this.num;
    }

    public Comments comments() {
        return new RtComments(this.entry, this);
    }

    public JsonObject json() throws IOException {
        return new RtJson(this.request).fetch();
    }
}
