// How Immutability Helps
//
// example: commons-email JAVA library
//
// (bad design: builder pattern)

Email email = new SimpleEmail();

// configure the class through a bunch of setters and then you ask it to send()
email.setHostName("smtp.googlemail.com");
email.setSmtpPort(465);
email.setAuthenticator(new DefaultAuthenticator("user", "pwd"));

email.setFrom("yegor@teamed.io", "Yegor Bugayenko");
email.addTo("dude@jcabi.com");
email.setSubject("how are you?");

email.setMsg("Dude, how are you?");

email.send();

// why is it bad?
//   a monster class, class Email, that can do everything for you
//     ex. sending your MIME message via SMTP
//         creating the message
//         configuring its parameters
//         adding MIME parts to it, etc.
//
// (good design)
//
// use seven objects instantiated via seven new calls
// encapsulate one into another, and then we ask the postman to send() the envelope for us
//
// Postman is responsible for packaging a MIME message
// SMTP is responsible for sending it via SMTP
Postman postman = new Postman.Default(
  new SMTP("smtp.googlemail.com", 465, "user", "pwd")
);

// the client code: use Postman object to send Message object created by Envelope object
Envelope envelope = new Envelope.MIME(                     // responsible for creating a Message object
    new Array<Stamp>(
        new StSender("Yegor Bugayenko <yegor@teamed.io>"), // attach sender to the Message object
        new StRecipient("dude@jcabi.com"),                 // attach recipient to the Message object
        new StSubject("how are you?")                      // attach subject to the Message object
    ),
    new Array<Enclosure>(
        new EnPlain("Dude, how are you?")                  // configure a MIME part to the Message object
    )
);
// Stamps (StSender/StRecipient/StSubject) are responsible for configuring MIME message before delivery
// Enclosure EnPlain is responsible for creating a MIME part for the message we're going to send

postman.send(envelope); // send the Message created by the Envelope object using the SMTP object

// What's Wrong With a Mutable Email?
//   the class so big, so its not cohesive, not readable, not maintainable
//   there is no data hiding or encapsulation: 33 variables are accessible by over 100 methods
//     why need encapsulation:
//       protect one programmer from another, i.e. defensive programming
//       helps us narrow down the scope of the problem
//   unit testing is not possible
//     test is even more complicated than the class itself
//       in order to test a one-line method setCharset(), you may need the entire integration testing
//       if something gets changed in one of the methods, almost every test method will be affected
//   a small, cohesive class is always better than a big one
//
// why the class becomes so big?
//   when we try to add new responsibilities to the class
//   we allow to insert data into mutable objects via configuration methods, i.e. setters
//   mutable classes tend to grow in size and lose cohesiveness
//
// if the class is immutable, you are forced to keep it cohesive, small, solid and robust
//
// (good design details)

interface Postman {

    void send(Envelope env);
}

interface Envelope {

    Message unwrap();
}

import javax.mail.Message;

class Postman.Default implements Postman {

    private final String host;
    private final int port;
    private final String user;
    private final String password;

    void send(Message msg) {
        // create SMTP session
        // create transport
        // transport.connect(this.host, this.port, etc.)
        // transport.send(msg)
        // transport.close();
    }
}
// because Message is difficult to construct, so we delegate the contruction to another class Envelope
//   it requires some manipulations before it can become a nice HTML email
//   class Envelope will build the complex object
//
// a simple implementation of Envelope
class MIME implements Envelope {

    public Message unwrap() { // creates an absolutely empty MIME message and returns it
        return new MimeMessage(Session.getDefaultInstance(new Properties()));
    }
}

// enchance the MIME implementation: adding a subject to it and both To: and From: addresses
class Envelope.MIME implements Envelope {

    private final String subject;
    private final String from;
    private final Array<String> to;

    public MIME(String subj, String sender, Iterable<String> rcpts) {
        this.subject = subj;
        this.from = sender;
        this.to = new Array<String>(rcpts);
    }

    public Message unwrap() { // create and configure MimeMessage
        Message msg = new MimeMessage(Session.getDefaultInstance(new Properties()));
        msg.setSubject(this.subject);
        msg.setFrom(new InternetAddress(this.from));
        for (String email : this.to) {
            msg.setRecipient(Message.RecipientType.TO, new InternetAddress(email));
        }
        return msg;
    }
}
// the class is still too big
// moreover, we may need it to do more things, ex. CC: and BCC: and Reply-To:, etc.
//   this will need to add more parameters to the constructor
//
// introduce another class: Stamps responsible for configuring an object Message (works like adapters/commands)

interface Stamp {

    void attach(Message message);
}

// simplify the MIME class by utilizing the new class
class Envelope.MIME implements Envelope {

    private final Array<Stamp> stamps;

    public MIME(Iterable<Stamp> stmps) { // takes an iterable of Stamp objects: more extensible 
        this.stamps = new Array<Stamp>(stmps);
    }

    public Message unwrap() { // create and configure MimeMessage using the passed-in Stamp objects
        Message msg = new MimeMessage(Session.getDefaultInstance(new Properties()));
        for (Stamp stamp : this.stamps) {
            stamp.attach(msg);
        }
        return msg;
    }
}
// now we can easily add more stamps for the subject, ex. To:, From:, CC:, BCC:, etc., as many as we like
// the class MIME will stay the same: small, cohesive, readable, solid, etc


// due to immutability, we are forced to refactor the code when the class grows, 
//   because we will not be able to pass all arguments through a constructor
