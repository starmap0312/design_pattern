// Object-Oriented GitHub API: jcabi-github
//   GitHub gives access to almost all of its features through RESTful JSON API
//   but its Java SDK has the following issues:
//   1) not really object-oriented
//   2) not based on JSR-353 (JSON Java API)
//   3) provides no mocking instruments
//   4) don't cover the entire API and can't be extended
//
// exmaple: jcabi-github
//
// why is it good?
//
// 1) Object Oriented for Real entities (domain oriented design)

GitHub github = new RtGitHub(/* credentials */);                     // create a GitHub object
Repos repos = github.repos();                                        // get Repos object from GitHub object
Repo repo = repos.get(new Coordinates.Simple("jcabi/jcabi-github")); // get Repo object from Repos object
Issues issues = github.issues();                                     // get Issues object from GitHub object
Issue issue = issues.get(123);                                       // get Issue object from Issues object
User author = new Issue.Smart(issue).author();                       // get User object from Issue.Smart object
System.out.println(author.name());                                   // get the auther name from User object

// note: GitHub (GitHub server), Repos, Repo, Issues, Issue, and User are interfaces
//   classes that implement them are not visible in the library

// 2) Mock Engine: the code is more testable
//    ex. MkGitHub class is a mock version of a GitHub server
//        it behaves almost exactly the same as a real server and is the perfect instrument for unit testing

// the test code: test if we can post a new issue to GitHub and add a message into it
public class FooTest {

    @Test
    public void createsIssueAndPostsMessage() {
        GitHub github = new MkGitHub("jeff");            // create a mocked GitHub server
        github.repos().create(Json.createObjectBuilder().add("name", owner).build()); // create a repo
        new Foo().doTheThing(github);                    // add comments to issue 1
        MatcherAssert.assertThat(
            github.issues().get(1).comments().iterate(), // iterate the comments of issue 1
            Matchers.not(Matchers.emptyIterable())
        );
    }
}
// GitHub object helps to get Repos object, which helps to create a Repo object with the owner name
// GitHub object helps to get Issues object, which helps to get the first issue, which helps to get
//   its comment iterator for testing (expected to be not empty after adding comments)

// 3) Extensible: the code is more extensible
//    jcabi-github is based on JSR-353 and uses jcabi-http for HTTP request processing
//      this combination makes it highly customizable and extensible
//
// ex1. if you want to get the value of hireable attribute of a User
//        but class User.Smart doesn't have a method for it
//        we can use method json() that returns an instance of JsonObject from JSR-353 (Java7) to access it

User user = // get it somewhere
System.out.println(new User.Smart(user).name());       // name() method exists in User.Smart
System.out.println(user.json().getString("hireable")); // there is no hireable() method User.Smart
// instead, we can use method json() that returns an instance of JsonObject from JSR-353 (part of Java7)

// ex2. if you want to use some feature from GitHub that is not covered by the API
//      we can get a Request object from GitHub interface and directly access the HTTP entry point of the server

GitHub github = new RtGitHub(oauthKey);
int found = github.entry()
    .uri().path("/search/repositories").back()  // set the uri path to the request
    .method(Request.GET)                        // set the method to GET
    .as(JsonResponse.class)                     // wrap the response with JsonReponse
    .getJsonObject()                            // get the JsonObject
    .getNumber("total_count")                   // get the value of key "total_count" from the JsonObject
    .intValue();                                // convert the value into a integer

// 4) Immutable
//    all classes are truly immutable and annotated with @Immutable in jcabi-github
