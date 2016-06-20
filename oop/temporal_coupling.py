# temporal coupling between method calls
#
#   if sequential method calls must stay in a particular order
#
# ex.
#   (bad design)
#
#   class Foo {
#
#       public List<String> names() {
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
#   what is wrong?
#
#     ex1. 10 months later, the code may look like this
#
#     List<String> list = new LinkedList();
#     // 10 more lines here
#     Foo.append(list, "Jeff");   // not certain if the line can be removed
#     Foo.append(list, "Walter");
#     // 10 more lines here
#     return list;
#
#     // there may be temporal coupling, so we have to check the body of append() method 
#
#     ex2. the code may be refactored like this 
#
#     List<String> list = new LinkedList();
#     if (/* something */) {      // not certain if the list can be returned before appending the two words
#         return list;
#     }
#     // 10 more lines here
#     Foo.append(list, "Walter"); // not certain if the order of appending the two words can be changed 
#     Foo.append(list, "Jeff");
#     // 10 more lines here
#     return list;
#   
#     // the lines are coupled together
#     // they must stay in this particular order, but the knowledge about that order is hidden
#     // easy to destroy the order, and our compiler won't be able to detect that 
#
#   (good design)
#
#   class Foo {
#
#       public List<String> names() {
#           // the method contains only one line, thus no line order dependency
#           // calls the with() method twice
#           return Foo.with(Foo.with(new LinkedList(), "Jeff"), "Walter");
#       }
#
#       private static List<String> with(List<String> list, String item) {
#           list.add(item.toLowerCase());
#           return list;
#       }
#   }
#   
# rule of thumbs:
#   an ideal method in OOP must have just a single statement, and this statement is return
#   
#
# another example: validation
#
#   (bad design)
#   
#   list.add("Jeff");
#   Foo.checkIfListStillHasSpace(list);
#   list.add("Walter");
#
#   // temporal coupling: the lines are coupled, the order is important
#   
#   (better design)
#
#   list.add("Jeff");
#   Foo.withEnoughSpace(list).add("Walter");  // the last two lines are combined together
#
# rule of thumbs:
#   a) an ideal method in OOP must have just a single statement, and this statement is return
#   b) use composable decorators, not static methods
#   c) if have to use static methods, don't make those static methods look like procedures 
#      make sure they always return results, which become arguments to further calls
#
