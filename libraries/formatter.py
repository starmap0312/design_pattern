print("%s %s" % ("one", "two"))
print("{} {}".format("one", "two"))

print("%s %s" % (1, 2))
print("{} {}".format(1, 2))

print("{1} {0}".format(1, 2))

class Data(object):

    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"

print("{0!s} {0!r}".format(Data()))

print("%10s" % "test")
print("{:>10}".format("test"))

print("%-10s" % "test")
print("{:10}".format("test"))
print("{:_<10}".format("test"))

print("%+d" % 42)
print("{:+d}".format(42))

print("%06.2f" % 3.141592653589793)
print("{:06.2f}".format(3.141592653589793))

print("{1} {0} {1}".format(10, 20))
print("{1} {var1} {0} {var2} {1}".format(10, 20, var2="variable2", var1="variable1"))
