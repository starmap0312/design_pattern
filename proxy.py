# Proxy Pattern
# object pattern: relationships between objects are established at run time via composition
# structural pattern: composes classes or objects into larger structures

class Image(object):
    # both proxy and real objects implement the same interface

    def displayImage(self):
        raise NotImplementedError

class RealImage(Image):

    def __init__(self, filename):
        self.filename = filename
        self.loadImageFromDisk()

    def loadImageFromDisk(self):
        print 'Loading %s' % self.filename

    def displayImage(self):
        print 'Displaying %s' % self.filename

class ProxyImage(Image):
    # virtual proxy, in place of expensive objects

    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def displayImage(self):
        if self.image is None:
            self.image = RealImage(self.filename)
        self.image.displayImage()

image1 = ProxyImage('Photo1')
image2 = ProxyImage('Photo2')
image1.displayImage()
image1.displayImage()
image2.displayImage()
image2.displayImage()
image1.displayImage()
