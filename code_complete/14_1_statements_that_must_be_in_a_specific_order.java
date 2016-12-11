// example: temporal coupling
revenue.ComputeMonthly();
revenue.ComputeQuarterly();
revenue.ComputeAnnual();

// 1) try to code in a way that order dependencies  become obvious
// ex. code that suggests an order dependency
expenseData = InitializeExpenseData( expenseData )
expenseData = ComputeMarketingExpense( expenseData )
expenseData = ComputeSalesExpense( expenseData )
expenseData = ComputeTravelExpense( expenseData )
expenseData = ComputePersonnelExpense( expenseData )
DisplayExpenseSummary( expenseData )

// 2) check for dependencies with assertions or error-handling code
//    but this technique creates additional complexity to the code
// ex.
//   each function that depends on expenseData checks whether isExpenseDataInitialized is true before
//   performing additional operations on expenseData
