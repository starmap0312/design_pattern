import subprocess
from abc import ABCMeta, abstractmethod

cmd = 'echo Line1; echo ----; echo Line2; echo ----; echo Line3'

# Method 1: decorating readers
class Reader(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def iterate(self):
        pass

class CommandReader(Reader):

    def __init__(self, cmd):
        self.cmd = cmd

    def iterate(self):
        process = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
        return [line for line in process.stdout.readlines()]

class Stripped(Reader):

    def __init__(self, source):
        self.source = source

    def iterate(self):
        return [line.strip() for line in self.source.iterate()] 

class NoDashLine(Reader):

    def __init__(self, source):
        self.source = source

    def iterate(self):
        return [line for line in self.source.iterate() if not line.startswith('--')]

print('Method 1: decorating readers')
reader = NoDashLine(Stripped(CommandReader(cmd)))
for line in reader.iterate():
    print(line)

class Iterable(object):
    __metaclass__ = ABCMeta

    def __iter__(self):
        return self

    @abstractmethod
    def next(self):
        pass

class CommandIterable(Iterable):

    def __init__(self, cmd):
        self.process = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)

    def next(self):
        line = self.process.stdout.readline()
        if not line:
            raise StopIteration()
        return line

class Stripped(Iterable):

    def __init__(self, iterable):
        self.iterable = iterable

    def next(self):
        return self.iterable.next().strip()

class NoDashLine(Iterable):

    def __init__(self, iterable):
        self.iterable = iterable

    def next(self):
        line = self.iterable.next()
        while line.startswith('--'): 
            line = self.iterable.next()
        return line

print('Method 2: decorating iterables')
for line in NoDashLine(Stripped(CommandIterable(cmd))):
    print(line)
