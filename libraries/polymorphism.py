from abc import ABC, abstractmethod

# example 1: supplement adapter class
#
# (bad design: big interface)

class InputStream(ABC):

    @abstractmethod
    def read(self, offset, length):
        pass

    @abstractmethod
    def read(self):
        pass

# (good design: small interface)

class InputStream(ABC):

    @abstractmethod
    def read(self, offset, length): # interface with one single method
        pass

    class SingleByte(object):       # define an adapter

        def __init__(self, stream):
            this.origin = stream

        def read(self):
            return this.origin.read(0, 1);


# example 2: multiple specified implementations using one generic implementation

class Request(ABC):

    @abstractmethod
    def fetch(self):
        pass

class BaseRequest(Request):

    def __init__(self, wire, uri):      # a generic implementation with two parameters
        self.wire = wire
        self.uri = uri

    def fetch(self):
        return this.wire.send(self.uri)

class ApacheRequest(Request):           # a specified class implementing the same interface

    WIRE = ApacheWire()

    def __init__(self, uri):            # a specified implementation with one parameter determined
        self.base = BaseRequest(ApacheRequest.WIRE, uri)

    def fetch(self):                    # a specified implementation using the generic implementation
        return self.base.fetch()

class JdkRequest(Request):              # a specified class implementing the same interface

    WIRE = JdkWire()

    def __init__(self, uri):            # a specified implementation with one parameter determined
        self.base = BaseRequest(JdkRequest.WIRE, uri)

    def fetch(self):                    # a specified implementation using the generic implementation
        return self.base.fetch()


# example 3: a family of extensions that work like decorators

class Response(ABC):

    @abstractmethod
    def body(self):
        pass

class AbstractResponse(Response):     # an abstract decorator class

    def __init__(self, response):
        this.response = response

    def body(self):
        return this.response.body()

class JsonResponse(AbstractResponse): # all response decorators inherit the body() method

    def __init__(self, response):
        super(JsonResponse, self).__init__(response)

    def json(self):                   # an extension method
        return # json format

class XmlResponse(AbstractResponse): # all response decorators inherit the body() method

    def __init__(self, response):
        super(XmlResponse, self).__init__(response)

    def json(self):                   # an extenstion method
        return # xml format

