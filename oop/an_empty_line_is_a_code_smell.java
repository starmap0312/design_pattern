// An Empty Line is a Code Smell
//   an empty line in a method is used for separation of concerns, but a method should always do one thing
//   refactor the code, so that there is no empty line in a method
//
// example:
//
// (bad design)

final class TextFile {

    private final File file;

    TextFile(File src) {
        this.file = src;
    }

    public int grep(Pattern regex) throws IOException {
        Collection<String> lines = new LinkedList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(this.file))) {
            while (true) {
                String line = reader.readLine();
                if (line == null) {
                    break;
                }
                lines.add(line);
            }
        } // we need an empty line, because the method try to do another thing

        int total = 0;
        for (String line : lines) {
            if (regex.matcher(line).matches()) {
                ++total;
            }
        }
        return total;
    }
}
// the grep() method first loads the content of the file
//   it next counts how many lines match the regular expression provided
//
// (good design)

final class TextFile {
    private final File file;

    TextFile(File src) {
        this.file = src;
    }

    public int grep(Pattern regex) throws IOException { // combining the two things
        return this.count(this.lines(), regex);
    }

    private int count(Iterable<String> lines, Pattern regex) { // count the number of lines matching the pattern
        int total = 0;
        for (String line : lines) {
            if (regex.matcher(line).matches()) {
                ++total;
            }
        }
        return total;
    }

    private Iterable<String> lines() throws IOException { // loads the content of the file to lines[]
        Collection<String> lines = new LinkedList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(this.file))) {
            while (true) {
                String line = reader.readLine();
                if (line == null) {
                    break;
                }
                lines.add(line);
            }
            return lines;
        }
    }
}

// CSS example:
//
// (bad design)

.container {
    width: 80%;
    margin-left: auto;
    margin-right: auto; // there is an empty line following

    font-size: 2em;
    font-weight: bold;
}
// .container class is too complex and has to be decomposed into two classes

// (good design)

.wide {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
}

.important {
    font-size: 2em;
    font-weight: bold;
}
