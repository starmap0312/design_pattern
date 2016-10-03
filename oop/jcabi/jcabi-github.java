/*
 * Github client, starting point to the entire library.
 *
 * Github github = new RtGithub(oauthKey);
 * Repo repo = github.repos().get(
 *     new Coordinates.Simple("jcabi/jcabi-github")
 * );
 * Issues issues = repo.issues();
 * Issue issue = issues.post("issue title", "issue body")
 *
 * an entry point to the RESTful API
 *
 * Github github = new RtGithub(oauthKey);
 * int found = github.entry()
 *     .uri().path("/search/repositories").back()
 *     .method(Request.GET)
 *     .fetch()
 *     .as(JsonResponse.class)
 *     .getJsonObject()
 *     .getNumber("total_count")
 *     .intValue();
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
    Iterable<Repo> iterate(
        String identifier
    );
}

// interface
public interface Repo extends JsonReadable, JsonPatchable, Comparable<Repo> {

    /*
     * Get its owner.
     * @return Github
     */
    Github github();

    /*
     * Get its coordinates.
     * @return Coordinates
     */
    Coordinates coordinates();

    /*
     * Iterate issues.
     * @return Issues
     */
    Issues issues();

    final class Smart implements Repo {
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

/*
 * <pre> Github github = new RtGithub(oauthKey);
 * Repo repo = github.repos().get(
 *     new Coordinates.Simple("jcabi/jcabi-github")
 * );
 * Issues issues = repo.issues();
 * Issue issue = issues.create("issue title", "issue body");
 * issue.comments().post("issue comment");</pre>
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

    /**
     * Public ctor, with a custom request.
     * @param req Request to start from
     * @since 0.4
     */
    public RtGithub(
        final Request req) {
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
    public RtGithub(
        final String user,
        final String pwd) {
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

    public Iterable<Repo> iterate(
        final String identifier) {
        return new RtPagination<Repo>(
            this.entry.uri().queryParam("since", identifier).back(),
            new RtValuePagination.Mapping<Repo, JsonObject>() {
                @Override
                public Repo map(final JsonObject object) {
                    return RtRepos.this.get(
                        new Coordinates.Simple(object.getString("full_name"))
                    );
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
        this.request = this.entry.uri()
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
