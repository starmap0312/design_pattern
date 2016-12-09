// A Compound Name Is a Code Smell
//   ex.
//   (bad design)
//     textLength, table_name, or current-user-email, etc.
//   (good design)
//     name, length, or email, etc.
//
// why is it bad?
//   we give a variable a compound name because its scope is so big and complex that a simple noun
//     would sound ambiguous
//   solution: refactor the code into smaller scopes to resolve the problem, not use compound names
//
// example:
//
// (bad design: compound variable names: csvFileName, redaRecords, csvLine, etc.)

class CSV

    def initialize(csvFileName)
        @fileName = csvFileName
    end

    def readRecords()
        File.readLines(@fileName).map |csvLine|
            csvLine.split(',')
        end
    end
end

// (good design: simple variable names: file, records, line, etc.)

class CSV

    def initialize(file)
        @file = file
    end

    def records()
        File.readLines(@file).map |line|
            line.split(',')
        end
    end
end
// the code looks more clear and concise
