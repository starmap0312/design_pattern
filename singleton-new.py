
class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(
                                  cls, *args, **kwargs)
        return cls._instance

a = Singleton()
b = Singleton()
print a is b
