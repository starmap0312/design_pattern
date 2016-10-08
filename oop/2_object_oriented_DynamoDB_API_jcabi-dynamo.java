// Object-Oriented DynamoDB API
//   jcabi-dynamo: a Java Object layer atop the DynamoDB SDK
//
// DynamoDB: a NoSQL database accessible through RESTful JSON API
//   tables: collections of data structures (called items)
//   items: every item has a hash, an optional range, and a number of optional attributes
//
//   ex. table depts
//
//   +------+--------+---------------------------+
//   | dept | worker | Attributes                |
//   +------+--------+---------------------------+
//   | 205  | Jeff   | job="manager", sex="male" |
//   | 205  | Bob    | age=43, city="Chicago"    |
//   | 398  | Alice  | age=27, job="architect"   |
//   +------+--------+---------------------------+
//
// Amazon provides an SDK, designed in a pure procedural style
//
//   ex. add a new item to the table above, i.e. RESTful call putItem

     putItem:
       tableName: depts
       item:
         dept: 435
         worker: "William"
         job: "programmer"

// (bad design: make the call through the AWS Java SDK)

    PutItemRequest request = new PutItemRequest();

    request.setTableName("depts");

    Map<String, AttributeValue> attributes = new HashMap<>();
    attributes.put("dept", new AttributeValue(435));
    attributes.put("worker", new AttributeValue("William"));
    attributes.put("job", new AttributeValue("programmer));

    request.setItem(attributes);

    AmazonDynamoDB aws = // instantiate it with credentials
    try {
        aws.putItem(request);
    } finally {
        aws.shutdown();
    }

// why is it bad?
//   an imperative procedural programming
//
// (good design: jcabi-dynamo)

Region region = // instantiate it with credentials

Table table = region.table("depts");

Item item = table.put(
    new Attributes()
        .with("dept", 435)
        .with("worker", "William")
        .with("job", "programmer")
);
