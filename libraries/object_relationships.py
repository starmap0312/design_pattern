# different relationships of classes to complete a task()

class A(object):

    def func_a(self):
        return "A's func"

class B(object):

    def func_b(self):
        return "B's func"

# Scenario 1: class C has two collaborators (both are its characteristics) to complete a task()
class C(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def task(self):
        return "C's func: use {0} and {1} to complete a task".format(self.a.func_a(), self.b.func_b())

# client code: to test task(), we can substitute classes A and B with fake classes
print C(A(), B()).task()

# Scenario 2: class C has one collaborator as its characteristic and pass in another to complete a task()
class C(object):

    def __init__(self, a):
        self.a = a

    def task(self, b): # collaborator of class B is not a characteristic but a parameter of the method
        return "C's func: use {0} and {1} to complete a task".format(self.a.func_a(), b.func_b())

# client code: to test task(), we can substitute classes A and B with fake classes
print C(A()).task(B())

# real-world example:
#   postman = Postman(SMTP('example.relay.com'))
#   postman.send(DefaultEnvelope(EnHTML("<html><p>text</p></html>"))
# we can use a fake object, ex. FakeSMTP('localhost'), to test the send() method

# Scenario 3: class C preserves class A's functionality and adds an additional functionality task()
class C(object):

    def __init__(self, a):
        self.a = a

    def func_a(self):
        return self.a.func_a()

    def task(self, b):
        return "C's func: use {0} and {1} to complete a task".format(self.a.func_a(), b.func_b())

print C(A()).func_a()  # class C works as an extention of class A
print C(A()).task(B())

# real-world example: JsonResponse works as a subtype of DefaultResponse
#   response = JsonResponse(DefaultResponse())
#   response.body()                                // JsonResponse preserves body() functionality
#   response.json()                                // JsonResponse adds a json() functionality
#
# note: inheritance of implementation creates coupling between classes
#
# (bad design)
class C(A):

    def task(self, b):
        return "C's func: use {0} and {1} to complete a task".format(self.func_a(), b.func_b())

print C().func_a()                 # class C inherits func_a() from class A
print C().task(B())                # classes A and C are tightly coupled

# Scenario 4: class C preserves class A's functionality and adds an additional functionality task()
class C(object):

    def __init__(self, a, b):      # both classes A and B are A's characteristic
        self.a = a
        self.b = b

    def func_a(self):
        return self.a.func_a()

    def task(self):
        return "C's func: use {0} and {1} to complete a task".format(self.a.func_a(), self.b.func_b())

print C(A(), B()).func_a()         # class C preserves func_a() of class A
print C(A(), B()).task()           # class C adds an additional functionality task()
