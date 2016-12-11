// try to extract the if-then condition to decorator
//   similarly, we use validating decorator to simplify object's responsibility
//   extract if-then condition to decorator, leaving object with only nominal path of code
// put common/normal case first and unusual/error cases later
//   make the nominal path of the code clear
// complexity of if-statements:
// 1) plain if-then statements
// 2) if-then-else statements
//    normal case in the if block, and unusual case in else block
// 3) if-then-else-if statements
//    check if using a case statement can improve readability
