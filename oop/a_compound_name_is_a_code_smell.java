// A Compound Name Is a Code Smell
//   ex. variable names like textLength, table_name, or current-user-email are bad
//       use variable names like name, length, or email instead
//
// why is it bad?
//   we give a variable a compound name because its scope is so big and complex that a simple noun
//     would sound ambiguous
//   refactor the code into smaller scopes
//
// example:
//
// (bad design: compound variable names)

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

// (good design: simple variable names)

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
// the code looks clear and concise
