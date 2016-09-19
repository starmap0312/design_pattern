# JAVA check exceptions vs. unchecked exceptions
#   1) unchecked exceptions: exceptions that extend RuntimeException
#      compiler will never force you to catch unchecked exceptions
#      do not need to be declared it in the method with throws keyword
#   2) checked exceptions: all other exception types that do not extend RuntimeException
#      exceptions that need to be explicitly catched or rethrown
#
# why is unchecked exception bad?
#   hiding the fact that a method may fail is a mistake
#     a method is too complex and want to keep some exceptions "hidden" (i.e. unchecked)
#     refactor the method so that it is responsible for one thing, and will throw checked exception if fails
#
# why is checked exception good?
#   unlike unchecked exceptions, we can't ignore failures: need to try/catch somewhere
#   every method is either "safe" (throws nothing) or "unsafe" (throws Exception)
#     to be safe, the method needs to handle the excpetion by itself
#     otherwise, the method is not safe and the client have to worry about the safety
#
# rule of thumbs:
#   1) always use checked exceptions and never use unchecked exceptions
#      all methods are declared either as "safe" (throws nothing) or "unsafe" (throws Exception)
#   2) never use exceptions for flow control: use only Exception without any sub-types
#        we don't need multiple exception types, if we don't use exceptions to control flow
#
#        ex.
#
#        (bad design: use Exception subtypes to control flow)
#
#          use an Exception subtype, ex. OutOfMemoryException, for memory allocation errors
#
#        (good design: use methods to control flow)
#        
#          use a method, ex. bigEnough(), which tells us whether heap is big enough for the next operation
#
#   3) never recover from exceptions: never catch without rethrowing
#
#        ex.
#
#        (bad design)
#
#          try {
#              save(file, data);
#          } catch (Exception ex) {
#              // we can't save the file, but it's OK, let's move on and do something else
#          }
#
#        (good design)
#
#          App#run()
#            Data#update()
#              Data#write()
#                File#save()   // an exception is thrown
#                              // don't do anything in the catch block: only report the problem
#                              // if want to recover from exception, go up to the top and start the chain again
