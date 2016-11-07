# unlike Java, python cannot override methods with different arguments

# Method 1: overriding methods with default argument value
class MyClass(object):

    def func(self, arg='x'):
        return 'use argument: {0} to do something'.format(arg)

obj = MyClass()
print obj.func()

# Method 2: defining separate methods
class MyClass(object):

    def func(self):
        return self.func_with_argument('x')

    def func_with_argument(self, arg):
        return 'use argument: {0} to do something'.format(arg)

obj = MyClass()
print obj.func()

# Method 2 is more flexsible, as the method logic are not mixed together
# use overriding/separate methods for unit testing: i.e. dependency injection via method argument

# for overriding constructors, we can only use method 1 in python
