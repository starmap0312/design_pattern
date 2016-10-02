// Object-Oriented Java Adapter of Amazon S3 SDK
//   Amazon S3: a storage for binary objects (files) with unique names, accessible through HTTP or RESTful API
//     to use S3, you create a "bucket" with a unique name, upload your "object" into the bucket through
//       the web interface or RESTful API, and then download it again through HTTP or the API
//
// example: Amazon S3 Java SDK
//
// (bad design: purely imperative and procedural)

AWSCredentials creds = new BasicAWSCredentials(key, secret); // create Amazon credential with key & secret
AmazonS3 aws = new AmazonS3Client(creds);                    // instantiate a S3 client
S3Object obj = aws.getObject(                                // imperative, get the S3Object immediately
  new GetObjectRequest("test-1", "doc.txt")                  //   via a request object using the client
);
InputStream input = obj.getObjectContent();                  // access the content stream of the S3Object 
String content = IOUtils.toString(input, "UTF-8");           // convert the content stream to a String
input.close();
// the design is rather imperative and solution-oriented

// (good design: jcabi-s3, a small object-oriented adapter of Amazon SDK)

Region region = new Region.Simple(key, secret);              // create Region object with key & secret
Bucket bucket = region.bucket("test-1");                     // instantiate a Bucket object with a name
Ocket ocket = bucket.ocket("doc.txt");                       // instantiate a Ocket object with a name
String content = new Ocket.Text(ocket).read();               // access the content string of the Ocket object 
// all classes in this design represent real-world domain entities
//   Region object helps to fetch Bucket object
//   Bucket object helps to fetch Ocket object
//   Ocket.Text object helps to read its text content
 
// why is it good?
// 1) S3 Object is an Object in Java
//    it is not a collection of procedures to be called in order to get its properties (like AWS SDK)
//      rather, it is a Java object with certain behaviors, called "ockets"
//        i.e. a Java object which encapsulates all AWS interaction details
//      it is declarative, so you can pass an Ocket object to another class, instead of passing it
//        your AWS credentials, bucket name, and object name for it to create a S3Object implementation
//      
//    Ocket is an interface, that exposes the behavior of a real AWS S3 object: read(), write(), check existence
//    Ocket.Text is a convenient decorator that simplifies working with binary objects

Ocket.Text ocket = new Ocket.Text(ocket);

if (ocket.exists()) {               // check the existence of ocket object
    System.out.print(ocket.read()); // read the text string of ocket object
} else {
    ocket.write("Hello, world!");   // write a text string to ocket object
}

// 2) Extendability Through Decoration: improves extendability
//    jcabi-s3 exposes all entities as interfaces, so it is easy to extend through decoration
//    ex. retry S3 object read operations a few times before giving up and throwing an IOException
//
// a decorator class that also implements Ocket
public RetryingOcket implements Ocket {

    private final Ocket origin;

    public RetryingOcket(Ocket ocket) {
        this.origin = ocket;
    }

    @Override
    public void read(OutputStream stream) throws IOException { // decorates the read() method by retrying 3 times
        int attempt = 0;
        while (true) {
            try {
                this.origin.read(stream);
            } catch (IOException ex) {
                if (attempt++ > 3) { // throw an Exception if fail 3 times
                    throw ex;
                }
            }
        }
  }
  // can also decoreate other methods: write(), exist(), etc.
}

// the client code: foo.process() won't see a difference, since it is the same Ocket interface it is expecting
foo.process(new RetryingOcket(ocket)); // new a RetryingOcket object that wraps an Ocket object

// 3) Easy Mocking: improves testability
//    because all entities in jcabi-s3 are interfaces, they are very easy to mock
//    ex. a client class that expects an S3 object, reads its data and calculates the MD5 hash

import com.jcabi.s3.Ocket;
import org.apache.commons.codec.digest.DigestUtils;

public class S3Md5Hash {

    private final Ocket ocket;

    public S3Md5Hash(Ocket okt) {
        this.ocket = okt;
    }

    public hash() throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        this.ocket.read(baos); // read the ocket content to a ByteArrayStream
        return DigestUtils.md5hex(baos.toByteArray()); // compute the MD5 hash of the ByteArray
    }
}

// the test code: using JUnit and Mockito for the test
import com.jcabi.s3.Ocket;
import org.junit.Test;

public class S3Md5HashTest {

    @Test
    public void generatesHash() {
        Ocket ocket = Mockito.mock(Ocket.class); // mock the Ocket interface
        Mockito.doAnswer(
            new Answer<Void>() {
                public Void answer(final InvocationOnMock inv) throws IOException {
                    OutputStream.class.cast(inv.getArguments()[0]).write(' ');
                }
            }
        ).when(ocket).read(Mockito.any(OutputStream.class));
        String hash = new S5Md5Hash(ocket); // test the functionality of hash() method of class S5Md5Hash
        Assert.assertEquals(hash, "7215ee9c7d9dc229d2921a40e899ec5f"); // it should compute the MD5 hash of ' '
    }
}

// 4) Immutability
//    all classes in jcabi-s3 are annotated with @Immutable and are truly immutable

