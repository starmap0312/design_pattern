print("1) map():")
# 1) map(function, iterable): return a iterable, i.e. map to another iterable
def func(arg):
    return int(arg)

# map() returns an iterator: with which you can iterate over the result of func applied with each of the iterable
# in Python2, map() returns a list, therefore, it is similar to executing the following statement
#     [ func(alist[i]) for i in alist ]  ==> map(func, alist)

for i in map(func, ["1", "2", "3"]):
    print(i)

print(list(map(func, ["1", "2", "3"])))

print("2) lambda:")
# 2) lambda arg1, arg2: return expression (defines an anonymous function object)
#
sum = lambda x, y: x + y
print("sum={}".format(sum(3, 4)))

# it is simliary to use the following traditional definition
def sum(x, y):
    return x + y

# 3) combination of map & lambda:
print("3) combination of map & lambda")
print(list(map(lambda x: x * 2, [7, 8, 9])))

alist = [1,2,3,4]
blist = [5,6,7,8]
print(list(map(lambda x, y: x + y, alist, blist)))

# 4) filter(function, iterable): return a iterable, i.e. filter out elements if passed-in function return False 
# filter out all the elements of a iterable, for which the function returns True
fibonacci = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print("4) filter()")
print(odd_numbers)

# 5) enumerate(iterable):
print("5) enumerate():")
for index, value in enumerate(["one", "two", "three"]):
    print("{}: {}".format(index, value))

# 6) zip(iterable1, iterable2):
print("6) zip(), iterating multiple lists simultaneously")
alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]
clist = ["c1", "c2", "c3"]
for a, b, c in zip(alist, blist, clist):
    print("({}, {}, {})".format(a, b, c))

print("zip() with unpacking")
multilists = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"]]
for a, b, c in zip(*multilists):
    print("({}, {}, {})".format(a, b, c))
