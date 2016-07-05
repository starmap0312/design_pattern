# Iterator Pattern (a BAD design pattern)
# - it is bad because the iterator object is mutable (use an immutable cursor instead)
#   alternatives:
#     a) for-each loop
#        declares explicitly that all of elements from container should be processed
#     b) selectors:
#        when for-each is not appropriate because not all of objects from container should be processed
#        unlike iterators, selectors allow to manifest in one place what kind objects is to be processed
#        iterators are low level objects, whereas selectors allow programmers to express explicitly what
#          they want to process and so that they are high level objects
# - provide a way to access the elements of an aggregate object (container) sequentially, 
#   without exposing its internal data structure (representation)
#   a) decouple iteration of a collection from its data structure
#   b) provide a uniform interface for traversal: next() and hasNext() methods
#   c) take the responsibility of traversal out of the aggregate object
#
#                             (HAS_A)
#          Iterator ...........................> Aggregate
#             ^                uses                  ^
#             |                                      |
#             |                  (HAS_A)             |
#       ConcreteIterator <.................... ConcreteAggregate
#                        creates via injection
#
#   (the iterator pattern applies dependency injection pattern, where the iterator object
#    takes the aggregate object when constructed and uses it to iterate its elements)
#
# - iterator pattern vs. visitor pattern:
#   a) iterator can traverse a composite
#   b) visitor can apply an operation over a composite
# - examples of similar frameworks that separate algorithms from the data structure:
#   ex. support four data structures (array, binary tree, linked list, and hash table), and 
#       support three algorithms (sort, find, and merge)
#   a) the naive approach requires 4 x 3 developments
#   b) generic programming requires 4 + 3 configuration items

class Aggregate(object):
    ''' the aggregate interface with a createIterator() method
        i.e. the interface of the data structure (different types implemented in subclasses)
    '''
    def createIterator(self):
        raise NotImplementedError

class ConcreteAggregate(Aggregate):
    ''' an implementation of the aggregate having a group of items to be iterated
        the data structure and a concrete iterator is specified
    '''

    def __init__(self):
        self.items = []

    def createIterator(self):
        # create a concrete iterator by injection 
        return ConcreteIterator(self)

    @property
    def count(self):
        return len(self.items)

    def get(self, index):
        return self.items[index]

    def add(self, value):
        self.items.append(value)

class Iterator(object):
    ''' the iterator interface defining how to use an aggregate object
        in the case of iterator, this is a uniform interface with next() and hasNext() methods
    '''

    def first(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def hasNext(self):
        raise NotImplementedError

    def current(self):
        raise NotImplementedError

class ConcreteIterator(Iterator):
    ''' a concrete iterator implementing how to use an aggregate object '''

    def __init__(self, aggregate):
        # dependency injection: an aggregate object is injected via constructor
        # i.e. the construction of the aggregate object is delegated to external code
        #      the iterator object can be constructed only if the aggregate object is specified
        self.current = 0
        self.aggregate = aggregate

    def first(self):
        return self.aggregate.get(0)

    def next(self):
        # use of the aggregate object, giving the next element of the aggregate object
        if self.current < self.aggregate.count - 1:
            self.current += 1
            return self.aggregate.get(self.current)
        return None

    def hasNext(self):
        # use of the aggregate object, returning if there exists more element
        return True if self.current <= self.aggregate.count else False

    def current(self):
        return self.aggregate.get(self.current)

# construct the aggregate object
aggregate = ConcreteAggregate()
aggregate.add('Item A')
aggregate.add('Item B')
aggregate.add('Item C')
aggregate.add('Item D')
# two ways to construct the iterator object
# a) inject the aggregate object when constructing the iterator object
iterator = ConcreteIterator(aggregate)
# b) use the createIterator() of the iterator object
iterator = aggregate.createIterator()

# use of the iterator object
item = iterator.first()
while item is not None:
    print item
    item = iterator.next()

