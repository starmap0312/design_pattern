import subprocess
from abc import ABCMeta, abstractmethod

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
        return [line for line in self.source.iterate() if '----' not in line]

cmd = 'echo Title Line; echo sep ---- sep; echo Body line'
reader = NoDashLine(Stripped(CommandReader(cmd)))
for line in reader.iterate():
    print(line)

