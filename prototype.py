# Prototype Pattern
# creational pattern: provides a way to decouple a client from the objects it creates
# used when creating an instance is too expensive (use clone instead)

import copy

class Prototype(object):

    def clone(self):
        raise NotImplementedError

class WordOccurrences(Prototype):
    # the field list: occurrences contains the position of the keyword in the text
    # which makes the instance expensive to construct, therefore it provides a clone method
    # that directly clones the result from an existing instance if any

    def __init__(self, test, word):
        self.occurrences = []
        for index in range(len(test)):
            if test[index:].startswith(word):
                self.occurrences.append(index)

    def getOneOccurrence(self, n):
        if n < len(self.occurrences):
            return self.occurrences[n]

    def clone(self):
        # return the member-wise copy of the object itself
        return copy.copy(self)

searchEngine = WordOccurrences('This is a test.', 'is')
anotherSearchEngine = searchEngine.clone()
print anotherSearchEngine.getOneOccurrence(0)
print anotherSearchEngine.getOneOccurrence(1)
print anotherSearchEngine.getOneOccurrence(2)
yetanotherSearchEngine = searchEngine.clone()
print yetanotherSearchEngine.getOneOccurrence(0)
print yetanotherSearchEngine.getOneOccurrence(1)
print yetanotherSearchEngine.getOneOccurrence(2)
