# Decorator pattern
#
#   make your code highly cohesive and loosely coupled
#
# example:
#
#   // an interface for an object that is supposed to read a text somewhere and return it
#   interface Text {
#       String read();
#   }
#
#   // an implementation that reads the text from a "file"
#   final class TextInFile implements Text {
#
#       private final File file;
#
#       public TextInFile(final File src) {
#           this.file = src;
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
#   // the decorator, also implementing Text, removes all unprintable characters from the text
#   final class PrintableText implements Text {
#
#       private final Text origin;
#
#       public PrintableText(final Text text) {
#           this.origin = text;
#       }
#
#       @Override
#       public String read() {
#           return this.origin.read()
#               .replaceAll("[^\p{Print}]", "");
#       }
#   }
#   // PrintableText doesn't read the text from the file
#   // it doesn't care where the text is coming from
#   // it just delegates text reading to the encapsulated instance of Text
#
#   // the client
#   final Text text = new PrintableText(
#       new TextInFile(new File("/tmp/a.txt"))
#   );
#   String content = text.read();
#
#   // another decorator that capitalize all letters
#   final class AllCapsText implements Text {
#
#       private final Text origin;
#
#       public AllCapsText(final Text text) {
#           this.origin = text;
#       }
#
#       @Override
#       public String read() {
#           return this.origin.read().toUpperCase(Locale.ENGLISH);
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
#   // the text is not started
#   // the object text is just a composition of decorators, not an executable procedure
#
#   ex.
#   (bad design)
#     class String from Java defines more than 20 utility methods (should be decorators instead)
#
#     final String txt = "hello, world!";
#     final String[] parts = txt.trim().toUpperCase().split(" ");
#
#   (good design)
#     final String[] parts = new String.Split(
#         new String.UpperCased(
#             new String.Trimmed("hello, world!")
#         )
#     );
#
#  rule of thumb:
#    1) avoid utility methods as much as possible: use decorators instead
#    2) an ideal interface should contain only methods that you absolutely cannot remove
#       everything else should be done through composable decorators         
#
# vertical and horizontal decorating
#
# 1) vertical decorating
#
#    interface Numbers {
#        Iterable<Integer> iterate();
#    }
#
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
#    interface Numbers {
#        Iterable<Integer> iterate();
#    }
#
#    interface Diff {
#        Iterable<Integer> apply(Iterable<Integer> origin);
#    }
#
#    final class Modified implements Numbers {
#
#       private final File file;
#
#       public Modified(final Numbers src, Diff [] app) {
#           this.file = src;
#           this.apps = app;
#       }
#
#       @Override
#       public String iterate() {
#           Iterable<Integer> rc = this.file.iterate();
#           for(app : apps) {
#               rc = app.apply(rc);
#           }
#           return rc;
#       }
#
#    }
#
#    // implements the core functionality of iterating numbers through instances of Positive, Odds, Unique, and Sorted
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
