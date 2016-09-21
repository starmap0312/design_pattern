// JUnit test fixtures are evil
//   it encourages developers to couple test methods
//   
// example:
//
// (bad design: use test fixtures for the preparation of testing)

public final class MetricsTest {

    private File temp;
    private Folder folder;

    @Before
    public void prepare() { // a preparation step that both test methods need (this couples the test methods)
        this.temp = Files.createTempDirectory("test");
        this.folder = new DiscFolder(this.temp);
        this.folder.save("first.txt", "Hello, world!");
        this.folder.save("second.txt", "Goodbye!");
    }

    @After
    public void clean() {
        FileUtils.deleteDirectory(this.temp);
    }

    @Test
    public void calculatesTotalSize() { // a test method for testing Metrics's size() method
        assertEquals(22, new Metrics(this.folder).size());
    }

    @Test
    public void countsWordsInFiles() { // a test method for testing Metrics's wc() method
        assertEquals(4, new Metrics(this.folder).wc());
    }
}

// (better design: isolate the test methods, by using for the preparation of testing)

public final class MetricsTest {

    @Test
    public void calculatesTotalSize() { // a test method for testing Metrics's size() method
        final File dir = Files.createTempDirectory("test-1"); // prepare a tmp folder for testing
        final Folder folder = MetricsTest.folder(             // prepare a tmp file for testing
            dir,
            "first.txt:Hello, world!",
            "second.txt:Goodbye!"
        );
        try {
            assertEquals(22, new Metrics(folder).size());
        } finally {
            FileUtils.deleteDirectory(dir);
        }
   }

   @Test
   public void countsWordsInFiles() { // a test method for testing Metrics's wc() method
       final File dir = Files.createTempDirectory("test-2"); // prepare a tmp folder for testing
       final Folder folder = MetricsTest.folder(             // prepare a tmp file for testing
           dir,
           "alpha.txt:Three words here",
           "beta.txt:two words"
           "gamma.txt:one!"
       );
       try {
           assertEquals(6, new Metrics(folder).wc());
       } finally {
           FileUtils.deleteDirectory(dir);
       }
   }

   private static Folder folder(File dir, String... parts) { // a static utility method used for preparation
       Folder folder = new DiscFolder(dir);
       for (final String part : parts) {
           final String[] pair = part.split(":", 2);
           this.folder.save(pair[0], pair[1]);
       }
       return folder;
   }
} 

// (good design: use a fake object for the preparation of testing)

// a fake object for creating tmp folder and tmp files for testing
public final class FkFolder implements Folder, Closeable {

    private final File dir;
    private final String[] parts;

    public FkFolder(String... prts) {            // second constructor
        this(Files.createTempDirectory("test-1"), parts);
    }

    public FkFolder(File file, String... prts) { // primary constructor
        this.dir = file;
        this.parts = parts;
    }

    @Override
    public Iterable<File> files() {
        final Folder folder = new DiscFolder(this.dir);
        for (final String part : this.parts) {
            final String[] pair = part.split(":", 2);
            folder.save(pair[0], pair[1]);
        }
        return folder.files();
    }

    @Override
    public void close() {
        FileUtils.deleteDirectory(this.dir);
    }
}

// both test methods utilizes the fake object to create tmp folder and tmp files for testing
public final class MetricsTest {

    @Test
    public void calculatesTotalSize() {
        final String[] parts = {
            "first.txt:Hello, world!",
            "second.txt:Goodbye!"
        };
        try (final Folder folder = new FkFolder(parts)) {
            assertEquals(22, new Metrics(folder).size());
        }
    }

    @Test
    public void countsWordsInFiles() {
        final String[] parts = {
            "alpha.txt:Three words here",
            "beta.txt:two words"
            "gamma.txt:one!"
        };
        try (final Folder folder = new FkFolder(parts)) {
            assertEquals(6, new Metrics(folder).wc());
        }
    }
}

// fake objects that are shipped together with production code
//   all test methods are decoupled
//   the fake object can be reused for new tests

