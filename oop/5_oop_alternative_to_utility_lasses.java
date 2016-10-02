// OOP Alternative to Utility Classes
//   utility classes are not proper objects
//   ex. StringUtils, IOUtils, FileUtils (Apache Commons)
//       Iterables, Iterators (Guava)
//       Files (JDK7)
//   inherited from procedural programming (a functional decomposition paradigm)
//
// example: a utility method max() for selecting the maximum value of two
//
// (bad design: procedural programming)

// a class without any state and prvoiding common utility code

public class NumberUtils {
    public static int max(int a, int b) {
        return a > b ? a : b;
    }
}

// the client code
int max = NumberUtils.max(10, 5);

// (good design: object-oriented programming)
// 1) instantiate and compose objects: let them manage data when and how they desire
// 2) instead of calling supplementary static functions, we should create objects that are capable of
//    exposing the behavior we are seeking
//    ex. create Max objects responsible for selecting maximum value of its two values

public class Max implements Number {

    private final int a;
    private final int b;

    public Max(int x, int y) {
        this.a = x;
        this.b = y;
    }

    @Override
    public int intValue() { // the intValue() method provides the maximum value of its two numbers
        return this.a > this.b ? this.a : this.b;
    }
}

// the client code
int max = new Max(10, 5).intValue();

// example: a utility method transform() for reading a text file, trimming every line, and saving in another file
//
// (bad design: procedural programming)

// define a procedure of execution
void transform(File in, File out) {
    Collection<String> src = FileUtils.readLines(in, "UTF-8"); // read lines from a file
    Collection<String> dest = new ArrayList<>(src.size());
    for (String line : src) {                                  // trim every line, saving in a collection
        dest.add(line.trim());
    }
    FileUtils.writeLines(out, dest, "UTF-8");                  // save the collection in another file 
}
// the method is responsbile for too many things
// it is hard to test the method (we need to prepare a real file if want to test the method)

// (good design: object-oriented programming)

void transform(File in, File out) {
    Collection<String> src = new Trimmed(new FileLines(new UnicodeFile(in)));
    Collection<String> dest = new FileLines(new UnicodeFile(out));
    dest.addAll(src);
}

// 1) class FileLines implements Collection<String>:
//      encapsulates all file reading and writing operations
//      i.e. behaves exactly as a collection of strings and hides all I/O operations
//           when we iterate() it, a file is being read
//           when we addAll() to it, a file is being written
// 2) class Trimmed implements Collection<String>:
//      every time the next line is retrieved, it gets trimmed
//      works as a decorator class
// 3) class UnicodeFile implements FILE:
//      reads and writes files as unicode encoding
// 4) advantages:
//      every class has only one responsibility, following the single responsibility principle
//      easier to develop, maintain and unit-test classes
//      declarative: enables lazy execution, i.e. the file is not read until its data is required
//        the whole task starts only after we call addAll()

// another example: a utility method readWords() for reading words from a file
//
// (bad design)

class FileUtils {

    public static Iterable<String> readWords(File f) {
        String text = new String(Files.readAllBytes(Paths.get(f)), "UTF-8");
        Set<String> words = new HashSet<>();
        for (String word : text.split(" ")) {
            words.add(word);
        }
        return words;
    }
}

// because the utility method readWords() is responsible for too many things, to test it
//   we need to prepare a file for it to read and debug the code if the result is not what we expect
//
// (good design: distribute the responsibilities to different objects)
//
// Step 1: turn the utility method into a class

// class Words is responsible for both reading a file into a string and iterating over words of that string
class Words implements Iterable<String> {

    private final File file;

    Words(File src) {
        this.file = src;
    }

    @Override
    public Iterator<String> iterator() { // iterator() provides an iterator for iterating the file's words
        String text = new String(Files.readAllBytes(Paths.get(this.file)), "UTF-8");
        Set<String> words = new HashSet<>();
        for (String word : text.split(" ")) {
            words.add(word);
        }
        return words.iterator();
    }
}
// the class is responsible for too many things

// Step 2: refactor the class and distribute its responsibilities to other objects

// class Text is responsibe for reading the file into a string
class Text {

    private final File file;

    Text(File src) {
        this.file = src;
    }

    @Override
    public String toString() {
        return new String(Files.readAllBytes(Paths.get(this.file)), "UTF-8");
    }
}

// class Word is responsibe for iterating the words of string
class Words implements Iterable<String> {

    private final String text;

    Words(String txt) {
        this.text = txt;
    }

    @Override
    public Iterator<String> iterator() {
        Set<String> words = new HashSet<>();
        for (String word : this.text.split(" ")) {
            words.add(word);
        }
        return words.iterator();
    }
}

// more testable and reusable: we don't need to prepare a file for it to read
// 
// the test code
import org.junit.Test;
import static org.hamcrest.MatcherAssert.*;
import static org.hamcrest.Matchers.*;

public class WordsTest {

    @Test
    public void parsesSimpleText() {
        assertThat(new Words("How are you?"), hasItems("How", "are", "you"));
    }
}

