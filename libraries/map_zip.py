def func(arg):
    return arg

for i in map(func, [1, 2, 3]):
    print(i)

print("basic use: map()")
print(list(map(func, [4, 5, 6])))

print(list(map(lambda x: x * 2, [7, 8, 9])))

print("basic use: enumerate()")
for index, value in enumerate(["one", "two", "three"]):
    print("{}: {}".format(index, value))

print("basic use: zip(), iterating multiple lists simultaneously")
alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]
clist = ["c1", "c2", "c3"]
for a, b, c in zip(alist, blist, clist):
    print("({}, {}, {})".format(a, b, c))

print("advanced use: zip() with unpacking")
multilists = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"]]
for a, b, c in zip(*multilists):
    print("({}, {}, {})".format(a, b, c))
