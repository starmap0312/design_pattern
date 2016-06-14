#  utility classes are evil
#    1) not proper objects
#    2) inherited from procedural programming (a functional decomposition paradigm)
#
#  ex. (bad design)
#
#      // a class without any state and prvoiding common utility code
#      public class NumberUtils {
#
#          public static int max(int a, int b) {
#              return a > b ? a : b;
#          }
#
#      }
#
#      int max = NumberUtils.max(10, 5);
#
#      (good design)
#      // 1) instantiate and compose objects: let them manage data when and how they desire
#      // 2) instead of calling supplementary static functions, we should create objects that are capable of
#      //    exposing the behavior we are seeking
#
#      public class Max implements Number {
#
#          private final int a;
#          private final int b;
#
#          public Max(int x, int y) {
#              this.a = x;
#              this.b = y;
#          }
#
#          @Override
#          public int intValue() {
#              return this.a > this.b ? this.a : this.b;
#          }
#      }
#
#      int max = new Max(10, 5).intValue();
#
#  ex. (procedural programming)
#
#      // define a procedure of execution
#      // read a text file, split it into lines, trim every line and then save the results in another file
#      void transform(File in, File out) {
#          Collection<String> src = FileUtils.readLines(in, "UTF-8");
#          Collection<String> dest = new ArrayList<>(src.size());
#          for (String line : src) {
#              dest.add(line.trim());
#          }
#          FileUtils.writeLines(out, dest, "UTF-8");
#      }
#
#      (object-oriented programming)
#
#      void transform(File in, File out) {
#          Collection<String> src = new Trimmed(
#              new FileLines(new UnicodeFile(in))
#          );
#          Collection<String> dest = new FileLines(
#              new UnicodeFile(out)
#          );
#          dest.addAll(src);
#      }
#      // 1) FileLines implements Collection<String> and encapsulates all file reading and writing operations
#      // 2) an instance of FileLines behaves exactly as a collection of strings and hides all I/O operations
#      // 3) when we iterate it: a file is being read
#      //    when we addAll() to it: a file is being written
#      // 4) Trimmed (Decorator pattern) also implements Collection<String> and encapsulates a collection of
#      //    strings: every time the next line is retrieved, it gets trimmed
#      // 5) Trimmed, FileLines, and UnicodeFile: each of them is responsible for its own single feature
#      //    following perfectly the single responsibility principle
#      // 6) it is much easier to develop, maintain and unit-test class FileLines rather than using a readLines()
#      //    method in a 80+ methods and 3000 lines utility class FileUtils
#      // 7) an object-oriented approach enables lazy execution: the in file is not read until its data is
#      //    required: if we fail to open out due to some I/O error, the first file won't even be touched
#      //    the whole task starts only after we call addAll()
#      // 8) we instantiate and compose smaller objects into bigger ones: this object composition is rather
#      //    cheap for the CPU since it doesn't cause any data transformations
#      // 9) in an object-oriented world, there is no data: there are only objects and their behavior
