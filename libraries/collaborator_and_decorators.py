# relationships of classes to complete a task()
#
print "example 1: one collaborator"

class A(object):

    def func_a(self):
        return "A's func"

# Scenario 1: class C has one collaborator as its characteristics to complete a task()
class C(object):

    def __init__(self, a):  # the collaborator object can be substituted
        self.a = a

    def task(self):         # works like a decorator if class C also implements interface class A
        return "C's func: use {0} to complete a task".format(self.a.func_a())

# client code: to test task(), we can substitute class A with a fake class when constructing class C
print C(A()).task()

# Scenario 2: class C has one collaborator as its method parameter to complete a task()
class C(object):

    def task(self, a): # collaborator is not a characteristic but a parameter of the method
        return "C's func: use {0} to complete a task".format(a.func_a())

# client code: to test task(), we can substitute parameter of class A with a fake class
print C().task(A())

# Scenario 3: class C preserves class A's functionality and adds an additional functionality task()
class C(object):

    def __init__(self, a):
        self.a = a

    def func_a(self):            # class C works as an extention of class A
        return self.a.func_a()

    def task(self):
        return "C's func: use {0} to complete a task".format(self.a.func_a())

# client code: to test task(), we can substitute class A with a fake class when constructing A wrapped with C
c = C(A())
print c.func_a()
print c.task()

# real-world example: JsonResponse works as a subtype of DefaultResponse
#   response = JsonResponse(DefaultResponse())
#   response.body()                                // JsonResponse preserves body() functionality
#   response.json()                                // JsonResponse adds a json() functionality
#
# (bad design: inheritance of implementation creates coupling between classes)
class C(A):

    def task(self):
        return "C's func: use {0} to complete a task".format(self.func_a())

c = C()
print c.func_a()                 # class C inherits func_a() from class A
print c.task()                   # classes A and C are tightly coupled

#############################################################

print "example 2: two collaborators"

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

# Scenario 2: class C has one collaborator as its characteristic and another one as its method parameter
class C(object):

    def __init__(self, a):
        self.a = a

    def task(self):
        return "C's func: use {0} to complete a task".format(self.a.func_a())

# client code: to test task(), we can substitute classes A with a fake class
print C(A()).task()
# real-world example:
#   session = Session('example.db.com')
#   session.query('SELECT * FROM posts')

# Scenario 3: class C preserves class A's functionality and adds an additional functionality task()
class C(object):

    def __init__(self, a):
        self.a = a

    def task(self, b):
        return "C's func: use {0} and {1} to complete a task".format(self.a.func_a(), b.func_b())

c = C(A())
print c.func_a()
print c.task(B())
# real-world example:
#   postman = Postman(SMTP('example.relay.com'))
#   postman.send(DefaultEnvelope(EnHTML("<html><p>text</p></html>"))

# Scenario 4: class C preserves class A's functionality and adds an additional functionality task()
class C(object):

    def __init__(self, a, b):      # both classes A and B are A's characteristic
        self.a = a
        self.b = b

    def func_a(self):              # works like decorator: class C works as an extention of class A
        return self.a.func_a()

    def task(self):
        return "C's func: use {0} and {1} to complete a task".format(self.a.func_a(), self.b.func_b())

c = C(A(), B())
print c.func_a()         # class C preserves func_a() of class A
print c.task()           # class C adds an additional functionality task()
