def func(arg):
    return arg

for i in map(func, [1, 2, 3]):
    print(i)

print(list(map(func, [4, 5, 6])))

print(list(map(lambda x: x * 2, [7, 8, 9])))
