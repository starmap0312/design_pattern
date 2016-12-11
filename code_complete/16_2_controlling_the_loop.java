// priciples
// 1) minimize the number of factors that affect the loop
//    simplify the loop by:
//    a) put initialization code directly before the loop
//    b) make entries and exits clear
//       a single and simple exit 
//       termination condition obvious
//    d) write short loops
//    e) keep housekeeping code in one place
//       i.e. put housekeeping code at the beginning or end of the loop
//    f) don't abuse loop index
//       name them clearly, and use them for only one purpose
//       ex. create additional variable rather than using the loop index outside the loop
//    
// 2) treat the inside of the loop as if it were a routine 
//    a) think of a loop as a black box
//    b) performs one and only one function
//    c) move part of the code inside long loops into routines
//
// 3) verify that the loop operates normally under each case and terminates under all possible conditions

while ( !inputFile.EndOfFile() && moreDataAvailable ) {
    // black box to the reader
}

// put housekeeping statements at the end of a loop
// ex.
nameCount = 0;
totalLength = 0;
while ( !inputFile.EndOfFile() ) {
   // do the work of the loop

   // housekeeping statements
   nameCount++;
   totalLength = totalLength + inputString.length();
}

// example: misuse loop index's terminal value
//          save important loop-index values rather than using the loop index outside the loop
// (bad design: recordCount is used outside of the loop)
for ( recordCount = 0; recordCount < MAX_RECORDS; recordCount++ ) {
    if ( entry[ recordCount ] == testValue ) {
        break;
    }
}
if ( recordCount < MAX_RECORDS ) {
    return true;
} else {
    return false;
}

// (good design: recordCount is more localized)
found = false;
for ( recordCount = 0; recordCount < MAX_RECORDS; recordCount++ ) {
    if ( entry[ recordCount ] == testValue ) {
        found = true;
        break;
    }
}
return found;

// example: meaningful variable names to make nested loops readable
// (bad design: meaningless names i, j, k)
for ( int i = 0; i < numPayCodes; i++ ) {
    for ( int j = 0; j < 12; j++ ) {
        for ( int k = 0; k < numDivisions; k++ ) {
            sum = sum + transaction[ j ][ i ][ k ];
        }
    }
}

// (good design: meaningful names)
for ( int payCodeIdx = 0; payCodeIdx < numPayCodes; payCodeIdx++ ) {
    for (int month = 0; month < 12; month++ ) {
        for ( int divisionIdx = 0; divisionIdx < numDivisions; divisionIdx++ ) {
            sum = sum + transaction[ month ][ payCodeIdx ][ divisionIdx ];
        }
    }
}

