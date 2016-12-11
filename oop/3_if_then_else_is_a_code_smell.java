// in most cases, if-then-else (switch statements) must be replaced by decorator or simply another object
//
// example:
//
// (bad design: both the validation & modify functionality are defined in one class: BadTalk)
class BadTalk implements Talk {

    void modify(Collection<Directive> dirs) {
        if (!dirs.isEmpty()) {
            // this object is responsible for two things:
            // 1) check if the dirs is empty
            // 2) apply the modification and save new XML document to DynamoDB table
        }
    }
}

// (good design: extract if-then condition to decorator and delegate modify functionality to the decoratee)
class GoodTalk implements Talk { // works as a validating decorator

    private final Talk origin;

    public GoodTalk(Talk source) {
        this.origin = source;
    }

    void modify(Collection<Directive> dirs) {
        if (!dirs.isEmpty()) {        // this decorator checks if the dirs is empty
            this.origin.modify(dirs); // it delegates the modify functionality to the source object
        }
    }
}

