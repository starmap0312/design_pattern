// Constructors Must Be Code-Free
//   don't do computations inside a constructor and then encapsulate results
//     the only allowed statement inside a constructor is an assignment
//   it prevents composition of objects and makes them un-extensible
//
// example: an interface that represents a name of a person

interface Name {
    String first();
}

// (bad design: computation inside the constructor)

public final class EnglishName implements Name {

    private final String name;

    public EnglishName(final CharSequence text) {     // constructor contains some computation
        this.name = text.toString().split(" ", 2)[0]; // it splits name into parts and encapsulates them
    }

    @Override
    public String first() { // when we call the first() method, it will return the splitted value
        return this.name;
    }
}

// why is it bad?
//   the object is similar to an imperative utility method
//     in imperative programming, we do all calculations right now and return fully ready results
//     in declarative programming, we instead try to delay calculations for as long as possible
//   we are abusing the new operator and turning it into a static method
//     it does the calculations for us right now
//
// (good design)

public final class EnglishName implements Name {

    private final CharSequence text;

    public EnglishName(final CharSequence txt) {
        this.text = txt;
    }

    @Override
    public String first() {                          // do the computation in the method, not constructor
        return this.text.toString().split("", 2)[0]; // but it has performance issues, as everytime we call
                                                     // first(), the computation is repeated
    }
}

// the client code
final Name name = new EnglishName(new NameInPostgreSQL(/*...*/));

if (/* something goes wrong */) {
    throw new IllegalStateException(
        String.format("Hi, %s, we can't proceed with your application", name.first())
    );
}

// we can resolve the performance issue using decorator classes

public final class CachedName implements Name {

    private final Name origin;

    public CachedName(final Name name) {
        this.origin = name;
    }

    @Override
    @Cacheable(forever = true)     // using the Cacheable annotation from jcabi-aspects
    public String first() {
        return this.origin.first();
    }
}
// note: don't make CachedName mutable and lazily loaded

// the client code
final Name name = new CachedName(
    new EnglishName(
        new NameInPostgreSQL(/*...*/)
    )
);

// we split the object into two parts
//   the first one knows how to get the first name from the English name
//   the second one knows how to cache the results of this calculation in memory

