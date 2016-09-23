from abc import ABCMeta, abstractmethod
from abc import ABC, ABCMeta, abstractmethod


# (Python2)
# class Abstract(metaclass=ABCMeta):

# (Python3)
class Abstract(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

# can't instantiate abstract class Abstract with abstract methods read, write: TypeError
# ex. obj = Abstract()

class Concrete(Abstract):

    def read(self):
        print("read() method implemented")

    def write(self, data):
        print("write() method implemented: writing {}".format(data))

obj = Concrete()
obj.read()
obj.write("message")
