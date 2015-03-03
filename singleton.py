# Singleton Pattern
# object pattern: responsibilities between objects are establsihed at run time via composition
# creational pattern: decouple a client from the objects it creates

class SingletonException(Exception):
    pass

class Singleton(object):

    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def __call__(self, *args, **kwargs):
        # disable instance call
        raise SingletonException

a = Singleton.getInstance()
b = Singleton.getInstance()
print a is b
