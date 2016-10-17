import datetime
# vertical vs. horizontal decomposition of responsibility
#
#   vertical decomposition is better
#
# example:
#
# (bad design: before decomposition)
#
# a class responsible for two things: formatting the text and writing the formated text to a file
class Log(object):

    def __init__(self, path):
        self.file = open(path, 'a')

    def put(self, text):
        line = datetime.datetime.now().strftime("%B %d, %Y: ") + text
        self.file.write(line)

# (good design: after horizontal decomposition)
#
# the class is responsible for only writing the line to a file
class Log(object):

    def __init__(self, path):
        self.file = open(path, 'a')

    def put(self, line):
        self.file.write(str(line))

# an additional class that is responsible for formatting the text
class Line(object):

    def __init__(self, text):
        self.line = text

    def __str__(self):
        return datetime.datetime.now().strftime("%B %d, %Y: ") + self.line

# the client class: need to know both classes Log and Line to provide its service
class Script(object):

    def write(self, text, filepath):
        log = Log(filepath)
        log.put(Line(text))

script = Script().write('Message\n', '/tmp/log.txt')

# horizontally decomposition increases complexity as client has more dependencies and points of contact
#
#   class Script --> class Log
#                --> class Line
#
# (better design: after vertical decomposition)
#
# the class is responsible for only writing the line to a file (no change)
class Log(object):

    def __init__(self, path):
        self.file = open(path, 'a')

    def put(self, line):
        self.file.write(str(line))

# a decorator class responsible for decorating the Log put() method
class TimedLog(object):

    def __init__(self, log):
        self.origin = log

    def put(self, text):
        self.origin.put(datetime.datetime.now().strftime("%B %d, %Y: ") + text)

# the client class has only one entry point to Log object
class Script(object):

    def write(self, text, log):
        # the Log object "consists" of two objects, one wrapped into another
        log = TimedLog(log)
        log.put(text)

script = Script().write('Message\n', Log('/tmp/log.txt'))

# vertical decomposition decreases complexity
#
#   class Script --> class TimedLog --> class Log

