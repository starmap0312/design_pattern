class Iterable(object):

    def __init__(self, last=1, size=5):
        self.last = last
        self.size = size  #cutoff

    def __iter__(self):
        return self    # because the object is both the iterable and the itorator

    def next(self):
        num = self.last
        if num > self.size:
            raise StopIteration()
        self.last = num + 1
        return num

print('use for-loop to traverse items of the iterable')
for item in Iterable():
    print(item)

print('use iterator to traverse items of the iterable')
iterator = Iterable().__iter__()
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
