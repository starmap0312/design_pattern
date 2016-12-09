// common ways to handle errors
// 1) return a neutral/harmless value
//    ex. displaying incorrect data is better than shutdown the service 
// 2) substitute the next piece of valid data
//    ex. if encountering a corrupted record, then continue reading next valid record
// 3) return the same answer as the previous time
//    ex. if an invalid color, then return the same color used previously
// 4) substitute the closest legal value
//    ex. if negative speeds,then simply shows a speed of 0
// 5) log a warning message to a file
//    ex. log a warning message to a file and then continue on
// 6) return an error code
//    ex. report an error and let other routine higher in the calling hierarchy handles the error
//    ex. throw an exception
// 7) call an error-processing routine or object
//    ex. centralize error handling in a global error-handling routine or error-handling object
//    (make debugging easier, but creates coupling, as many parts of the program depend on it)
// 8) display an error message
//    ex. little overhead, but may reveal the interface information (security issues)
// 9) shut down
//    ex. safety-critical applications
//
// robustness (fail slow) vs. correctness (fail fast)
//
// high-level design of error processing
// 1) be careful to handle invalid parameters in consistent ways throughout the program
//    ex. high-level code handle errors and low-level code report errors
// 2) the whole point of defensive programming is guarding against errors you don't expect
//    if you don't expect the function ever to produce an error, check it anyway
