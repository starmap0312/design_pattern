# Resource Acquisition Is Initialization (RAII)
# 1) in RAII, holding a resource is a class invariant and is tied to object lifetime
# 2) resource allocation (acquisition) is done during object creation by the constructor
#    resource deallocation (release) is done by the destructor
#    ex. in C++, local variables allow easy management of multiple resources within a single function
#        local variables are destroyed in the reverse order of their construction
#        (an object is destroyed only if fully constructed, i.e. if no exception propagates from its constructor)
# 3) if there are no object leaks, then there will be no resource leaks
# 4) using RAII greatly simplifies resource management, reduces overall code size and helps ensure program correctness
# 5) RAII provides encapsulation
#      resource management logic is defined once in the class, not at each call site
#    RAII provides exception safety for stack resources
#      a) tying the resource to the lifetime of a stack variable
#      b) resources that are released in the same scope as they are acquired
#      c) if an exception is thrown and proper exception handling is in place
#         the only code that will be executed when exiting the current scope are the destructors of objects
#         declared in that scope
#      d) in C++, stack unwinding is only guaranteed to occur if the exception is caught somewhere
#         if no matching handler is found in a program, the function terminate() is called
#         this behavior is usually acceptable, since OS releases remaining resources like memory, files, sockets, etc.
#         at program termination
#    RAII provides locality
#      acquisition and release logic are written next to each other in the class definition
# 6) comparing RAII with the finally construct in Java
#      RAII technique leads to less code than use of a finally construct
# 7) typical uses 
#    a) controlling mutex locks in multi-threaded applications
#       the object releases the lock when destroyed
#       the code that locks the mutex essentially includes the logic that the lock will be released
#       when execution leaves the scope of the RAII object
#    b) interacting with files
#       have an object that represents a file that is open for writing
#       the file is opened in the constructor and closed when execution leaves the object's scope
#       care must be taken to maintain exception safety
# 8) ownership of dynamically allocated objects (memory allocated with new in C++) can be controlled with RAII
#    ex.  C++11 standard library: smart pointer classes std::unique_ptr for single-owned objects
#                                                       std::shared_ptr for objects with shared ownership
#         C++98 standard library: std::auto_ptr
#         Boost libraries: boost::shared_ptr
# 9) limitations
#    a) RAII only works for resources acquired and released (directly or indirectly) by stack-allocated objects
#       for Heap-allocated objects RAII needs smart pointers and weak-pointers for cyclically referenced objects
#
# Python manage object lifetime by reference counting, which makes it not possible to use RAII
#   a) deterministic object destruction tied to scope is impossible in a garbage collected language
#      RAII does not work in Python
#      there is no guarantee that __del__() will be called: it’s just for memory manager use not for resource handling
#   b) objects that are no longer referenced are destroyed and released, so a destructor can
#      release the resource at that time
#   c) however, object lifetimes are not necessarily bound to any scope
#      objects may be destroyed non-deterministically or not at all
#   d) it's possible to accidentally leak resources that should have been released at the end of some scope
#      ex. objects stored in a static variable (a global variable) may not be finalized when program terminates
#   e) objects with circular references will not be collected by a simple reference counter
#      they will live indeterminately long; even if collected (by garbage collection), destruction time and order
#      will be non-deterministic
#   f) context manager (i.e. with statement) has nothing to do with scoping
#      it is deterministic cleanup: so it overlaps with RAII in the ends, but not in the means
#
# Scope-based Resource Management (SBRM)
# 1) special case of automatic variables
# 2) RAII ties resources to object lifetime, which may not coincide with entry and exit of a scope
#    however, using RAII for automatic variables (SBRM) is the most common use case

