from abc import ABC, abstractmethod

# example 1: a family of specified implementations that uses one generic implementation

class Request(ABC):

    @abstractmethod
    def fetch(self):
        pass

class BaseRequest(Request):             # a concrete implementation with a generic constructor

    def __init__(self, wire, uri):      # a generic constructor with two parameters
        self.wire = wire
        self.uri = uri

    def fetch(self):                    # this generic implementation will do the work
        return this.wire.send(self.uri)

class ApacheRequest(Request):           # a concrete implementation with a specified constructor 

    WIRE = ApacheWire()

    def __init__(self, uri):            # a specified constructor with one parameter
        self.base = BaseRequest(ApacheRequest.WIRE, uri)

    def fetch(self):                    # delegate the work to the generic implementation
        return self.base.fetch()

class JdkRequest(Request):              # a concrete implementation with a specified constructor 

    WIRE = JdkWire()

    def __init__(self, uri):            # a specified implementation with one parameter determined
        self.base = BaseRequest(JdkRequest.WIRE, uri)

    def fetch(self):                    # delegate the work to the generic implementation
        return self.base.fetch()

# example 2: a supplement class that works like an adapter
#
# (bad design: a big interface)

class InputStream(ABC):

    @abstractmethod
    def read(self, offset, length):
        pass

    @abstractmethod
    def read(self):
        pass

# (good design: a small interface)

class InputStream(ABC):             # a generic interface

    @abstractmethod
    def read(self, offset, length): # a generic method with two parameters
        pass

    class SingleByte(object):       # a supplement class that works like an adapter 

        def __init__(self, stream):
            this.origin = stream

        def read(self):             # an adapted method with no parameter
            return this.origin.read(0, 1);

# example 3: a supplement decorator class that works like an extenstion

class Response(ABC):

    @abstractmethod
    def body(self):
        pass

    class JsonResponse(AbstractResponse): # a supplement decorator class that adds one extention method 

        def __init__(self, response):
            self.response = response

        def body(self):                   # a direct delegation method
            return this.response.body()

        def json(self):                   # an extension method
            return # json format

# example 4: a family of decorator classes that work like extenstions

class Response(ABC):

    @abstractmethod
    def body(self):
        pass

class AbstractResponse(Response):     # an abstract class for the concrete decorators

    def __init__(self, response):
        this.response = response

    def body(self):                   # body() method to be inherited by concrete decorators
        return this.response.body()

class JsonResponse(AbstractResponse): # a concrete decorator class that adds one extention method 

    def __init__(self, response):
        super(JsonResponse, self).__init__(response)

    def json(self):                   # an extension method
        return # json format

class XmlResponse(AbstractResponse):  # a concrete decorator class that adds one extention method

    def __init__(self, response):
        super(XmlResponse, self).__init__(response)

    def json(self):                   # an extenstion method
        return # xml format

