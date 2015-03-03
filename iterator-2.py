# Iterator Pattern
# - provide a way to access the elements of an aggregate object sequentially, without
#   exposing its underlying representation
# - decouple algorithms of a collection from its data structure
# - gives you a way to access the elements of an aggregate object without exposing its
#   internal structure
# - providing a uniform interface for traversing many types of aggregate objects
# - to traverse the elements of an aggregate object in different ways without bloat its interface
# - take the responsibility for traversal out of an aggregate object, put into a standard protocol
# - generic programming: separate the notion of "algorithm" from that of "data structure"
# - support 4 data structures(array/binary tree/linked list/hash table), and 3 algorithms(sort/
#   find/merg), the naive approach requires 4x3 developments, whereas generic programming
#   requires 4+3 configuration items
# - iterator can traverse a composite, and visitor can apply an operation over a composite

class Aggregate(object):
    # aggregate abstraction

    def createIterator(self):
        raise NotImplementedError

class ConcreteAggregate(Aggregate):

    def __init__(self):
        self.items = []

    def createIterator(self):
        return ConcreteIterator(self)

    @property
    def count(self):
        return len(self.items)

    def get(self, index):
        return self.items[index]

    def set(self, value):
        self.items.append(value)

class Iterator(object):
    # iterator abstraction

    def first(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def hasNext(self):
        raise NotImplementedError

    def current(self):
        raise NotImplementedError

class ConcreteIterator(Iterator):

    def __init__(self, aggregate):
        self.current = 0
        self.aggregate = aggregate

    def first(self):
        return self.aggregate.get(0)

    def next(self):
        if self.current < self.aggregate.count-1:
            self.current += 1
            return self.aggregate.get(self.current)
        return None

    def hasNext(self):
        return True if self.current <= self.aggregate.count else False

    def current(self):
        return self.aggregate.get(self.current)

aggregate = ConcreteAggregate()
aggregate.set('Item A')
aggregate.set('Item B')
aggregate.set('Item C')
aggregate.set('Item D')
iterator = ConcreteIterator(aggregate)
item = iterator.first()
while item is not None:
    print item
    item = iterator.next()


