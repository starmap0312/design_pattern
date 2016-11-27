# Single Responsibility Principle
# - "a class should have only one reason to change (one responsibility)"
# - if a class has two things that change for different at different times, then it is better
#   to separate them in different classes; otherwise, if they are coupled in one class, then 
#   changing one may require to change the other accordingly
# - how to avoid over design (when not to separate)?
#   if two responsibilites always change at the same time, there is no need to separate them
#   a good separation can be done only when the full picture of how the application should 
#   work is well understood
# - example:
#   1) an application that compiles and prints a report
#     1. the content of the report
#     2. the print format of the report
#     if two responsibilites are coupled in one class, then changing one might affect the other
#     it is better to separate the two responsibilities in two classes

class Content(object):
    ''' an interface '''

    def compile(self):
        # the compilation process of the content may change
        raise NotImplementedError

class Report(object):
    ''' an interface '''

    def setContent(self, content):
        raise NotImplementedError

    def printContent(self):
        # the print format of the report may change
        raise NotImplementedError

class HeartBeat(Content):

    def compile(self):
        return "heart beat statistics data"

class Body(Content):

    def compile(self):
        return "body statistics data"

class HTMLReport(Report):

    def setContent(self, content):
        self.data = content.compile()

    def printContent(self):
        print "html format of %s" % self.data

class XMLReport(Report):

    def setContent(self, content):
        self.data = content.compile()

    def printContent(self):
        print "xml format of %s" % self.data

report = HTMLReport()
report.setContent(HeartBeat())
report.printContent()

report = XMLReport()
report.setContent(Body())
report.printContent()

#   b) dependency injection pattern: the construction and use of a service object are separated
#      there may be more service objects to be added, and there may be different uses of
#      the service objects to be defined in the future
