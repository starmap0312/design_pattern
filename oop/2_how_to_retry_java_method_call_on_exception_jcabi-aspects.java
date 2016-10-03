// How to Retry Java Method Call on Exception
//   jcabi-aspects:
//     retry a method a few times before throwing an exception
//     works with binary weaving, which integrates AspectJ with the code
//     use cases:
//       ex. Executing JDBC SELECT statements (execute Database commands)
//       ex. Loading data from HTTP, S3, FTP, etc resources (fetch webpage, download file, etc.)
//       ex. Uploading data over the network                (upload data)
//       ex. Fetching data through RESTful stateless API-s  (fetch data from web API)
//
// example: downloading the following web page

@RetryOnFailure(attempts = 3, delay = 10, unit = TimeUnit.SECONDS)
public String load(URL url) {
  return url.openConnection().getContent();
}

// what is happening behind the scene (pseudo-code)
while (attempts++ < 3) { // retry at most 3 times
    try {
        return original_load(url);
    } catch (Throwable ex) {
        log("we failed, will try again in 10 seconds");
        sleep(10);       // delay 10 seconds if method fails
    }
}
