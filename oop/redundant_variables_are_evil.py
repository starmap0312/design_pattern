# redundant variables
#   make the code more verbose and difficult to understand: use values instead
#   in perfectly designed methods, you won't need any variables aside from method arguments
#
#   
# example:
#
# (bad design)
#
#   String fileName = "test.txt";
#   print("Length is " + new File(fileName).length());
#
# (good design)
#
#   print("Length is " + new File("test.txt").length());
#
# // an increasing length of code degrades readability
# //   declare at most four variables in a method
# // refactor the code using new objects or methods but not variables
# //   make the code shorter by moving pieces of it into new classes or private methods
