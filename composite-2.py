# Composite Pattern

# 1. create the same interface (lowest common denominator) that makes classes interchangeable
class Component(object):

    def traverse(self):
        raise NotImplementedError

# 2. all concrete classes IS_A interface
class Primitive(Component):

    def __init__(self, value):
        self.value = value

    def traverse(self):
        print '%s  ' % self.value

class Composite(Component):

    def __init__(self, value):
        self.value = value
        self.children = []
        self.total = 0

    # child management operation is not defined in interface, which benefits safety
    def add(self, component):
        self.children.append(component)
        self.total += 1

    def traverse(self):
        print '%s  ' % self.value
        for i in range(self.total):
            # 4. container classes use polymorphism as they delegate to their children
            self.children[i].traverse()

# two different kinds of container classes.
class Row(Composite):

    def traverse(self):
        print 'Row',
        super(Row, self).traverse()

class Column(Composite):

    def traverse(self):
        print 'Col',
        super(Column, self).traverse()

first = Row(1)
second = Column(2)
third = Column(3)
fourth = Row(4)
fifth = Row(5)
first.add(second)
first.add(third)
third.add(fourth)
third.add(fifth)
first.add(Primitive(6))
second.add(Primitive(7))
third.add(Primitive(8))
fourth.add(Primitive(9))
fifth.add(Primitive(10))
first.traverse()
