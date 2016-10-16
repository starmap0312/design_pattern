// Object-Oriented DynamoDB API
//   jcabi-dynamo: a Java Object layer atop the DynamoDB SDK
//     all public entities in jcabi-dynamo are Java interfaces
//     can test and mock the library completely, but using DynamoDB Local and create integration tests is better
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

// why is it good?
//    it employs encapsulation and separates responsibilities of classes
//    Table class (an interface internally implemented by a class) encapsulates information about the table
//    Item class encapsulates item details
//
// we can pass an item as an argument to another method and all DynamoDB related implementation details are
//   hidden from it
//   ex.

void sayHello(Item item) {
    System.out.println("Hello, " + item.get("worker"));
}
// we don't know anything about DynamoDB or how to deal with its RESTful API
// we interact solely with an instance of Item class
//
// ex. remove all workers from the table who work as architects

Region region = // instantiate it with credentials

Iterator<Item> workers = region.table("depts").frame()
    .where("job", Condition.equalTo("architect"));

while (workers.hasNext()) {
    workers.remove();
}
