# iterator: a class implementing the following two public methods
#   has_next()
#   next()
# iterable: a class with a factory method of its iterator 
#   __iter__(): returns an iterator
# reader: a class with a factory method of a iterable
#   iterate(): returns an iterable

import subprocess
from abc import ABCMeta, abstractmethod

cmd = 'echo Line1; echo ----; echo Line2; echo ----; echo Line3'

# Method 1: decorating reader class
class Reader(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def iterate(self):
        pass

class CommandReader(Reader):
    # reader class

    def __init__(self, cmd):
        self.cmd = cmd

    def iterate(self):
        process = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
        return process.stdout.readlines()

class Stripped(Reader):
    # decorator class

    def __init__(self, source):
        self.source = source

    def iterate(self):
        return [line.strip() for line in self.source.iterate()] 

class NoDashLine(Reader):
    # decorator class

    def __init__(self, source):
        self.source = source

    def iterate(self):
        return [line for line in self.source.iterate() if not line.startswith('--')]

print('Method 1: decorating reader class')
reader = NoDashLine(Stripped(CommandReader(cmd)))
for line in reader.iterate():
    print(line)


# Method 2: decorating iterator class

class Iterator(object):
    __metaclass__ = ABCMeta

    def __iter__(self):
        return self

    @abstractmethod
    def next(self):
        pass

class CommandIterator(Iterator):
    # iterator class

    def __init__(self, cmd):
        self.process = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)

    def next(self):
        line = self.process.stdout.readline()
        if not line:
            raise StopIteration()
        return line

class Stripped(Iterator):
    # decorator class

    def __init__(self, iterator):
        self.iterator = iterator

    def next(self):
        return self.iterator.next().strip()

class NoDashLine(Iterator):
    # decorator class

    def __init__(self, iterator):
        self.iterator = iterator

    def next(self):
        line = self.iterator.next()
        while line.startswith('--'): 
            line = self.iterator.next()
        return line

print('Method 2: decorating iterator class')
for line in NoDashLine(Stripped(CommandIterator(cmd))):
    print(line)
