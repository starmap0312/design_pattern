// fluent interface
//   the entire server interaction fits into one Java statement
//   it is simple, testable and extensible
//   it is immutable: to be able to encapsulate an instance in other immutable classes
//
// example:
//
// ex1. TimeInterval interface
//
// (bad design: a non-fluent interface)

    TimePoint fiveOClock, sixOClock;

    TimeInterval meetingTime = new TimeInterval(fiveOClock, sixOClock);

// (good design: a fluent interface)

    TimeInterval meetingTime = fiveOClock.until(sixOClock);

// ex2.

// (bad design: a non-fluent interface)

    private void makeNormal(Customer customer) {
        Order order = new Order();
        customer.addOrder(order);
        order.addLine(new OrderLine(6, Product.find("TAL")));
        OrderLine line = new OrderLine(5, Product.find("HPK"));
        line.setSkippable(true);
        order.addLine(line);
        order.addLine(new OrderLine(3, Product.find("LGV")));
        order.setRush(true);
    }

// (good design: a fluent interface)

   private void makeFluent(Customer customer) {
        customer.newOrder()
                .with(6, "TAL")
                .with(5, "HPK").skippable()
                .with(3, "LGV")
                .priorityRush();
    }

// coming up with a nice fluent API requires a good bit of thought

// example: jcabi-http, an http client library that implements a fluent interface
//
// ex1. make an HTTP request and expect a successful HTML page in return
String html = new JdkRequest("https://www.google.com")
    .uri().path("/users").queryParam("id", 333).back()
    .method(Request.GET)
    .header("Accept", "text/html")
    .fetch()
    .as(RestResponse.class)
    .assertStatus(HttpURLConnection.HTTP_OK)
    .body();

// ex2. fetch JSON data and retrieve a value 
String rate = new JdkRequest("http://www.getexchangerates.com/api/latest.json")
    .header("Accept", "application/json")
    .fetch()
    .as(JsonResponse.class)                   // fetch() is decorated by JsonResponse
    .json().readArray().getJsonObject(0)      // the decorator adds a json() method which returns a JSON object 
    .getString("EUR");

// ex3. fetch XML data and retrieve a string value from its element
String name = new JdkRequest("http://my-api.example.com")
    .header("Accept", "text/xml")
    .fetch()
    .as(XmlResponse.class)                    // fetch() is decorated by XmlResponse
    .xml().xpath("/root/name/text()").get(0); // the decorator adds an xml() method which returns an XML object

