# replace type code with classes
#
# example 1: use static method
class BloodType(object):

    def __init__(self, code):
        self.code = code

    def getCode(self):
        return self.code

    @staticmethod
    def A():
        return BloodType(0)

    @staticmethod
    def B():
        return BloodType(1)

    @staticmethod
    def AB():
        return BloodType(2)

    @staticmethod
    def O():
        return BloodType(3)

print(BloodType.A().getCode())
print(BloodType.B().getCode())
print(BloodType.AB().getCode())
print(BloodType.O().getCode())

# example 2: use static field
class BloodType(object):

    def __init__(self, code):
        self.code = code

    def getCode(self):
        return self.code

class BloodGroup(object):

    (A, B, AB, O) = (BloodType(0), BloodType(1), BloodType(2), BloodType(3))

print BloodGroup.A.getCode()
print BloodGroup.B.getCode()
print BloodGroup.AB.getCode()
print BloodGroup.O.getCode()

# replace type code with subclasses

class BloodType(object):

    (A, B, AB, O) = (0, 1, 2, 3)

    def getCode(self):
        raise NotImplementedError

class A(BloodType):

    def getCode(self):
        return BloodType.A

class B(BloodType):

    def getCode(self):
        return BloodType.B

class AB(BloodType):

    def getCode(self):
        return BloodType.AB

class O(BloodType):

    def getCode(self):
        return BloodType.O

print A().getCode()
print B().getCode()
print AB().getCode()
print O().getCode()

# replace type code with state/strategy
class Person(object):

    def __init__(self, bloodType):
        self.bloodType = bloodType

    def getCode(self):
        return self.bloodType.getCode()

print Person(A()).getCode()
print Person(B()).getCode()
print Person(AB()).getCode()
print Person(O()).getCode()


# static method vs. classmethod
class MyClass(object):

    def member_method(self, x):
        print "executing member_method(%s, %s)" % (self, x)
        MyClass.class_method(1.1)
        MyClass.static_method(1.2)

    @classmethod
    def class_method(cls, x):
        print "executing class_method(%s, %s)" % (cls, x)
        MyClass.static_method(2.1)

    @staticmethod
    def static_method(x):
        print "executing static_method(%s)" % x    

obj = MyClass()
obj.member_method(1)
obj.class_method(2)
MyClass.class_method(3)
obj.static_method(4)
MyClass.static_method(5)

