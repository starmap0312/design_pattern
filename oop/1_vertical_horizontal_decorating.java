// Decorator pattern
//   one of the best ways to add features to an object without changing its interface
//   make your code highly cohesive and loosely coupled
//
// (Composable Decorators vs. Imperative Utility Methods)
//
// example: from simple to complex, by adding features to a class
//
// an interface: read a text somewhere and return the read String
interface Text {
    String read();
}

// an implementation that reads the text from a "file"
final class TextInFile implements Text {

    private final File source;

    public TextInFile(final File source) {
        this.source = source;
    }

    @Override
    public String read() {
        return new String(
            Files.readAllBytes(), "UTF-8"
        );
    }
}

// a decorator class that removes all unprintable characters from the read String 
final class PrintableText implements Text {

    private final Text source;

    public PrintableText(final Text text) {
        this.source = text;
    }

    @Override
    public String read() {
        return this.source.read().replaceAll("[^\p{Print}]", "");
    }
}
// PrintableText doesn't read the text from the file
//   it doesn't care where the read String is coming from
//   it just delegates the reading to a Text object
//
// the client
final Text text = new PrintableText(
    new TextInFile(new File("/tmp/a.txt"))
);
String content = text.read();

// another decorator class that capitalize all letters
final class AllCapsText implements Text {

    private final Text source;

    public AllCapsText(final Text text) {
        this.source = text;
    }

    @Override
    public String read() {
        return this.source.read().toUpperCase(Locale.ENGLISH);
    }
}

// use them in combination
final Text text = new AllCapsText(
    new TrimmedText(
        new PrintableText(
            new TextInFile(new File("/tmp/a.txt"))
        )
    )
);
String content = text.read();

// lazy execution: until method read() is called, the file is not touched and the processing of
//   the read String is not started
// the client uses a composition of decorators, not an executable procedure
//
// example: turn utility classes into decorators
//
// (bad design: utility class)

// class String from Java defines more than 20 utility methods (should use decorators instead)
final String txt = "hello, world!";
final String[] parts = txt.trim().toUpperCase().split(" ");

// (good design: decorators)

final String[] parts = new String.Split(
    new String.UpperCased(
        new String.Trimmed("hello, world!")
    )
);

// rule of thumb:
// 1) avoid utility methods as much as possible, and use decorators instead
// 2) an ideal interface should contain only methods that you absolutely cannot remove
//    everything else should be done through composable decorators         


// vertical and horizontal decorating
//
// another example:

// 1) vertical decorating
//
// a Numbers object knows how to traverse its numbers in order
interface Numbers {
    Iterable<Integer> iterate(); // the iterate() method returns an iterable object (i.e. object with an iterator() method)
}

// the client code
Numbers numbers = new Sorted(
    new Unique(
        new Odds(
            new Positive(
                new ArrayNumbers(
                    new Integer[] {
                        -1, 78, 4, -34, 98, 4,
                    }
                )
            )
        )
    )
);
// Sorted, Unique, Odds, etc. work as indivisual vertical decorators
//   they takes the Numbers object as an argument of its constructor and decorates its iterate() method

class Positive implements Numbers {

   private final Numbers source;

   public Positive(final Numbers source) {
       this.source = source;
   }

   @Override
   public Iterable<Integer> iterate() {
       List<Integer> rc = new ArrayList<>();
       Iterable<Integer> iterable = this.source.iterate();
       for (Integer num : iterable) {
           if (num > 0) {
               rc.add(num);
           }
       }
       return rc;
   }
}

Iterable<Integer> iterable = numbers.iterate();
// the Numbers object are decorated by overriding its iterate() method 
//   it then returns an iterable object for traversing sorted, odd, and positive integers of the original Numbers object 
//
// 2) horizontal decorating
//
// a Numbers object knows how to traverse its numbers in order
interface Numbers {
    Iterable<Integer> iterate();
}

// a Modifier object knows how to decorate an Iterable<Integer> object 
interface Modifier {
    Iterable<Integer> apply(Iterable<Integer> origin);
}
// the modifier apply the iterable object 

// a decorator class that override Number object's iterate() method by applying a list of modifiers in sequence 
final class HorizontalDecorator implements Numbers {

   private final Numbers source;

   public HorizontalDecorator(final Numbers source, Modifier [] modifiers) {
       this.source = source;
       this.modifiers = modifiers;
   }

   @Override
   public Iterable<Integer> iterate() {
       Iterable<Integer> iterable = this.source.iterate();
       for(modifier : modifiers) {
           iterable = modifier.apply(iterable);
       }
       return iterable;
   }

}

class Positive {

   public Iterable<Integer> apply(Iterable<Integer> itr) {
       List<Integer> rc = new ArrayList<>();
       Iterable<Integer> iterable = itr.iterate();
       for (Integer num : iterable) {
           if (num > 0) {
               rc.add(num);
           }
       }
       return rc;
   }
}

// the client code
Numbers numbers = new HorizontalDecorator(
    new ArrayNumbers(
        new Integer[] {
            -1, 78, 4, -34, 98, 4,
        }
    ),
    new Modifier[] {
        new Positive(),
        new Odds(),
        new Unique(),
        new Sorted()
    }
);
// Sorted, Unique, Odds, etc. work as vertical decorators (modifiers)
//   they takes the Numbers object as an argument of its method and apply its iterate() method's return object
// HorizontalDecorator decorates the iterate() method by applying the vertical decorators (modifiers) in sequence

Iterable<Integer> iterable = numbers.iterate();

// in vertical decorating, the decorator classes Positive, Odds, etc. implement the Numbers interface
//   they override (decorate) the iterate() method
// in horizontal decorating, classes Positive, Odds, etc. convert the iterable object returned by the iterate() method
//   a wrapper class, HorizontalDecorator, applies the apply one by one and returns it in its iterate() method


