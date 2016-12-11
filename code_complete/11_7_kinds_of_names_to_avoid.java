// Kinds of Names to Avoid 
// 1) avoid misleading names or abbreviations
// 2) avoid names with similar meanings
//    ex. the code becomes confusing if you use names with similar meaning within a scope
//        input      vs. inputValue
//        recordNum  vs. numRecords
//        fileNumber vs. fileIndex
// 3) avoid similar names that represent objects with different meanings
//    ex. clientRecords + clientReports vs. records + reports
// 4) avoid numerals in names
//    ex. file1 and file2, or total1 and total2
//
// Good Naming Principles: the goal is to improve program readability
// 1) fully and accurately describe what object represents
//    i.e. express what more than how
// 2) refer to real-world problem rather than to programming-language solution
//    i.e. use domain/problem driven names, not solution driven names
//         use meaningful names, not computerish names
//    ex. 
//    (good) count/index  vs. (bad) num
//      a named constant describing the entity it represents, not the number it refers to
//    (good) employeeData vs. (bad) inputData
//    (good) printerReady vs. (bad) readyFlag
//    (good) calcVal      vs. (bad) sum
//
//    ex.
//    (bad design: solution-oriented naming)
if ( flag ) {...}
if ( statusFlag & 0x0F ) {...}
if ( printFlag == 16 ) {...}
if ( computeFlag == 0 ) {...}
//    (good design: problem-oriented naming)
if ( dataReady ) {...}
if ( characterType & PRINTABLE_CHAR ) {...}
if ( reportType == ReportType_Annual ) {...}
if ( recalcNeeded == false ) {...}

// 3) use qualifiers on names to distinguish objects
//    use namepace (C++) or package (Java) or module (Python)
//    ex.
namespace UserInterfaceSubsystem {
    // declarations of objects
}

namespace DatabaseSubsystem {
    // declarations of objects
}
UserInterfaceSubsystem::Employee employee; 
DatabaseSubsystem::Employee employee;

// 4) use naming convention to distinguish objects 
//    a) use prefix or suffix that indicates the category
//       standardized prefixes allow you understand the object accurately
//    ex. Color_Red, Color_Green, Color_Blue, etc.
//    ex.
//        class RtGithub, RtRepos, RtRepo, etc. (Rt stands for Restful)
//        class StSender, StSubject, StReceient, etc. (St stands for Stamp) 
//        class EnPlain, EnHTML, EnBinary, etc. (En stands for Enclosure)
//
//    b) distinguish among local and global data: increase code readability
//    ex. my_local
//        MY_GLOBAL
//    c) distinguish among type names, enumerated types, named constants, and variables
//    ex. ClassName/TypeName: MyClass
//        EnumeratedTypes:    Color_Red, Color_Green, Color_Blue, etc.
//        NAMED_CONSTANT:     RECS_MAX
//        local_variable:     my_var
//
//    ex. named constants (C++)
const int LETTER = 0x01;
const int DIGIT = 0x02;
const int PUNCTUATION = 0x04;
const int LINE_DRAW = 0x08;
//
//    ex. enumerated types (C++)
enum Color {
    Color_Red,
    Color_Green,
    Color_Blue
};

//        
// 5) use short Names to increase code readability
//    a) use short names
//    ex.
//    (good) numTeamMembers    vs. (bad) numberOfPeopleOnTheUsOlympicTeam
//    (good) numSeatsInStadium vs. (bad) numberOfSeatsInTheStadium
//    (good) teamPointsMax     vs. (bad) maximumNumberOfPointsInModernOlympics
//
//    b) avoid compound names
//       use short name as long as it conveys enough meaning within the "scope"
//       similar to the idea of programming to interface (generic class) not implementation (descriptive)
//    ex:
//    (bad design: compound name does not increase readability)

class CSV(object):

    def __init__(self, csvFileName):
        self.filename = csvFileName

    def readRecords(self):
        records= []
        for csv_line in open(self.filename, 'rb').readlines():
            records.append(csv_line.split(','))
        return records

// (good design: single name improves the code readability)
class CSV(object):

    def __init__(self, file):
        self.file = file

    def records(self):
        records= []
        for line in open(self.file, 'rb').readlines():
            records.append(line.split(','))
        return records
//  one exception is that you want to emphasize relationships among related items
//  ex.
//    address vs. employeeAddress
//    phone   vs. employeePhone
//    name    vs. employeeName
//
//    b) all words abbreviated consistently
//       ex.
//        class RtGithub, RtRepos,   RtRepo,     etc. (Rt stands for Restful)
//        class StSender, StSubject, StReceient, etc. (St stands for Stamp) 
//        class EnPlain,  EnHTML,    EnBinary,   etc. (En stands for Enclosure)
//
// 6) use common opposite variable names
// ex.
//   begin/end
//   first/last
//   min/max
//   next/previous
//   source/target
//   source/destination
