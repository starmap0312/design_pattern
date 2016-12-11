// principles of writing code with sequential dependencies (temporal coupling)
// 1) make the dependencies among statements obvious
//    use good routine names, parameter lists, comments, and housekeeping variables
//    ex. name routines in a way that makes dependencies obvious
//    ex. design parameters to routines in a way that makes dependencies obvious
//    ex. add comments to describe the dependencies
// 2) check/assert for sequential dependencies with the help of housekeeping variables
// 3) if statements do not have order dependencies, try to increase readability by 
//    a) grouping related statements together, making code easily read from top to bottom
//    b) moving independent groups of statements into its own routine
