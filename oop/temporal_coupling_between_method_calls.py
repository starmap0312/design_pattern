# temporal coupling between method calls
#
#   sequential method calls must stay in a particular order
#
# ex.
#   (bad design)
#
#   class Foo {
#
#       public List<String> names() {   // a method with multiple statements, which are coupled together
#           List<String> list = new LinkedList();
#           Foo.append(list, "Jeff");
#           Foo.append(list, "Walter");
#           return list;
#       }
#
#       // a static append() method to avoid code duplication
#       private static void append(List<String> list, String item) {
#           list.add(item.toLowerCase());
#       }
#   }
#   
#   what is the problem?
#
#     ex. 10 months later, we may put more code around them
#
#     List<String> list = new LinkedList();
#     // 10 more lines here
#     Foo.append(list, "Jeff");   // not certain if the line can be removed, as the lines are coupled together
#     Foo.append(list, "Walter"); // the knowledge about the order are hidden inside the body of append method
#     // 10 more lines here
#     return list;
#
#     // if we want to remove the line Foo.append(list, "Jeff"), we need to check the body of append() method
#     // see if it will affect the result returned in the last line
#
#     ex. the code may be refactored by others as follows
#
#     List<String> list = new LinkedList();
#     if (/* something */) {      // not certain if the list can be returned before the two append method calls
#         return list;
#     }
#     // 10 more lines here
#     Foo.append(list, "Walter"); // not certain if the order of appending the two words can be changed 
#     Foo.append(list, "Jeff");
#     // 10 more lines here
#     return list;
#   
#     // if we want to return list before the two append() calls, we need to check the body of append() methods
#
# why is it bad?
#   temporal coupling: the lines are coupled together
#   they must stay in this particular order, but the knowledge about that order is hidden
#   it is easy to destroy the order, and our compiler won't be able to detect that 
#
#   (good design)
#
#   class Foo {
#
#       public List<String> names() {
#           // the method contains only one line, thus no line order dependency
#           return Foo.with(Foo.with(new LinkedList(), "Jeff"), "Walter");
#       }
#
#       private static List<String> with(List<String> list, String item) {
#           list.add(item.toLowerCase());
#           return list;
#       }
#   }
#   
# why is it good?
#   no temporal coupling: an ideal method in OOP havs one single statement, (a return statement)
#
# another example: validation
#
#   (bad design: the lines are coupled, the order is important)
#   
#   list.add("Jeff");                     // the lines are coupled together
#   Foo.checkIfListStillHasSpace(list);   // one needs to check the body of the methods to refactor the code
#   list.add("Walter");
#
#   (good design)
#
#   list.add("Jeff");
#   Foo.withEnoughSpace(list).add("Walter");  // the last two lines are combined together
#   // to further improve, we can replace static methods by composable decorators
#
# rule of thumbs:
#   a) an ideal method in OOP must has one single return statement
#   b) use composable decorators, not static methods
#      if we have to use static methods, don't make those static methods look like procedures 
#      make sure they always return results, which become arguments to further calls
#
