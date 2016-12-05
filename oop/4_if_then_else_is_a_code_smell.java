// in most cases, if-then-else (switch statements) must be replaced by a decorator or simply another object
//
// example: 
//
// (bad design: both the validation & modify functionality are defined in the BadTalk class)
class BadTalk implements Talk {

    void modify(Collection<Directive> dirs) {
        if (!dirs.isEmpty()) {
            // apply the modification and save the new XML document to the DynamoDB table
        }
    }
}

// (good design: extract validation to decorator and delegate modify functionality to decoratee)
class GoodTalk implements Talk { // works as a validating decorator

    private final Talk origin;

    public GoodTalk(Talk source) {
        this.origin = source;
    }

    void modify(Collection<Directive> dirs) {
        if (!dirs.isEmpty()) {
            this.origin.modify(dirs);
        }
    }
}

