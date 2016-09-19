# Decorator pattern
#   one of the best ways to add features to an object without changing its interface
#   make your code highly cohesive and loosely coupled
#
# example: from simple to complex, by adding features to a class
#
#   // an interface: read a text somewhere and return the read String
#   interface Text {
#       String read();
#   }
#
#   // an implementation that reads the text from a "file"
#   final class TextInFile implements Text {
#
#       private final File source;
#
#       public TextInFile(final File source) {
#           this.source = source;
#       }
#
#       @Override
#       public String read() {
#           return new String(
#               Files.readAllBytes(), "UTF-8"
#           );
#       }
#   }
#
#   // a decorator class that removes all unprintable characters from the read String 
#   final class PrintableText implements Text {
#
#       private final Text source;
#
#       public PrintableText(final Text text) {
#           this.source = text;
#       }
#
#       @Override
#       public String read() {
#           return this.source.read()
#               .replaceAll("[^\p{Print}]", "");
#       }
#   }
#   // PrintableText doesn't read the text from the file
#   //   it doesn't care where the read String is coming from
#   //   it just delegates the reading to a Text object
#
#   // the client
#   final Text text = new PrintableText(
#       new TextInFile(new File("/tmp/a.txt"))
#   );
#   String content = text.read();
#
#   // another decorator class that capitalize all letters
#   final class AllCapsText implements Text {
#
#       private final Text source;
#
#       public AllCapsText(final Text text) {
#           this.source = text;
#       }
#
#       @Override
#       public String read() {
#           return this.source.read().toUpperCase(Locale.ENGLISH);
#       }
#   }
#
#   // use them in combination
#   final Text text = new AllCapsText(
#       new TrimmedText(
#           new PrintableText(
#               new TextInFile(new File("/tmp/a.txt"))
#           )
#       )
#   );
#   String content = text.read();
#
#   // lazy execution: until method read() is called, the file is not touched and the processing of
#   //   the read String is not started
#   // the client uses a composition of decorators, not an executable procedure
#
# example: turn utility classes into decorators
#
#   (bad design: utility class)
#
#     // class String from Java defines more than 20 utility methods (should use decorators instead)
#     final String txt = "hello, world!";
#     final String[] parts = txt.trim().toUpperCase().split(" ");
#
#   (good design: decorators)
#
#     final String[] parts = new String.Split(
#         new String.UpperCased(
#             new String.Trimmed("hello, world!")
#         )
#     );
#
# rule of thumb:
#   1) avoid utility methods as much as possible, and use decorators instead
#   2) an ideal interface should contain only methods that you absolutely cannot remove
#      everything else should be done through composable decorators         
#
#
# vertical and horizontal decorating
#
# example:
#
# 1) vertical decorating
#
#    // a Numbers object knows how to traverse its numbers in order
#    interface Numbers {
#        Iterable<Integer> iterate();
#    }
#
#    // the client code
#    Numbers numbers = new Sorted(
#        new Unique(
#            new Odds(
#                new Positive(
#                    new ArrayNumbers(
#                        new Integer[] {
#                            -1, 78, 4, -34, 98, 4,
#                        }
#                    )
#                )
#            )
#        )
#    );
#
#    numbers.iterate();
#
# 2) horizontal decorating
#
#    // a Numbers object knows how to traverse its numbers in order
#    interface Numbers {
#        Iterable<Integer> iterate();
#    }
#
#    // a Diff object knows how to decorate an Iterable<Integer> object 
#    interface Diff {
#        Iterable<Integer> apply(Iterable<Integer> origin);
#    }
#
#    // a decorator class that decorates a Number object's method by applying a list of Diff objects in sequence 
#    final class Modified implements Numbers {
#
#       private final File source;
#
#       public Modified(final Numbers source, Diff [] decorators) {
#           this.source = source;
#           this.decorators = decorators;
#       }
#
#       @Override
#       public String iterate() {
#           Iterable<Integer> iterable = this.source.iterate();
#           for(decorator : decorators) {
#               iterable = decorator.apply(iterable);
#           }
#           return iterable;
#       }
#
#    }
#
#    // the client code
#    Numbers numbers = new Modified(
#        new ArrayNumbers(
#            new Integer[] {
#                -1, 78, 4, -34, 98, 4,
#            }
#        ),
#        new Diff[] {
#            new Positive(),
#            new Odds(),
#            new Unique(),
#            new Sorted()
#        }
#    );
#
#    numbers.iterate();
#
# // in vertical decorating, the decorator classes Positive, Odds, etc. implement the Numbers interface
# //   they decorate the original object's iterate() method in their own iterate() method
# // in horizontal decorating, the decorator classes Positive, Odds, etc. implement a different Diff interface
# //   they work together as a composite decorator, i.e. Modified object, to decorate the original object's
# //   iterate() method in the composite decorator's iterate() method 

