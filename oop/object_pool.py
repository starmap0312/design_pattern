# Object pool
# 1) a creational design pattern that keeps a set of initialized objects ready to use, i.e. a pool
#    rather than allocating and destroying them on demand
# 2) the client pool requests an object from the pool and perform operations on the returned object
#    when the client has finished, it returns the object to the pool rather than destroying it
# 3) object pools significantly improve performance
# 4) object pools complicate object lifetime, as objects obtained from and returned to a pool are not
#    actually created or destroyed at this time, and thus require care in implementation
#    ex. database connections, socket connections, threads, large graphic objects like fonts/bitmaps
# 5) used when working with a large number of objects that are expensive to instantiate and each object
#    is only needed for a short period of time
# 6) if no objects are present in the pool, a new item is created and returned
# 7) if resources are limited, a maximum number of objects is specified
# 8) object pooling may require resources, ex. memory or network sockets, and thus it is preferable that
#    the number of instances in the pool is low (not required)
#
# implementations
# 1) C++: smart pointers
#    in the constructor of the smart pointer, an object can be requested from the pool
#    in the destructor of the smart pointer, the object can be released back to the pool
# 2) garbage collected languages (no destructors)
#    do it manually: explicitly requesting an object from the factory and returning the object by
#    calling a dispose method
#    using a finalizer is not a good idea as there are no guarantees on when the finalizer will be run
#    use try/finally or context manager instead 
#
# handling of empty pools
# 1) fail to provide an object: return an error to the client
# 2) allocate a new object: this increases the size of the pool
# 3) in a multithreaded environment, a pool may block the client until another thread releases an object to
#    the pool

