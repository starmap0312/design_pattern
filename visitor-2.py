# Visitor Pattern
# - visitor lets you define a new operation without changing the classes of the elements on
#   which it operates
# - the classic technique for recovering lost type information without resorting to
#   dynamic casts
# - suppose that many unrelated operations need to be performed on node objects in a
#   heterogeneous aggregate strcutre, and you want to avoid "poluuting" the node classses 
#   with these operations
# - abstract functionality that can be applied to an aggregate hierarchy of "element" objects
# - the approach encourages designing "lightweight element classes" (by removing processing
#   functionality from their responsibilities)
# - new functionality implies new visitor subclass
# - visitor implements "double dispatch": in single dispatch, the executed operation depends
#   on 1.the name of the request and 2.the type of the receiver; in double dispatch, 
#   the executed operation depends on 1.the name of the request and 2.the type of TWO receivers
#   (the type of the visitor and the type of the element it visits)
# - double dispatch = accept() dispatch + visit() dispatch
# - visitor makes adding new operations easy (simply add a new visitor derived class), but
#   the subclasses in the aggregate node hierarchy must be stable to keep the visitor subclasses
#   in sync
# - visitor's goal: separate the algorithms from the data structures, or promote non-traditional
#   behavior to full object status
# - requirements of applying visitor: 1.element hierarchy is fairly stable 2.the public interface
#   of element class is sufficient for the visitor to perform the new operation
# - the element hierarchy is coupled only to visitor base class, the visitor hierarchy is 
#   coupled to each element derived class
# - iterator can traverse a composite. visitor can apply an operation over a composite
# - every time a new composite hierarchy derived class is added, every visitor derived class
#   must be amended
