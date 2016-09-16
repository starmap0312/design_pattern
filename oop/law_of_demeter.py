# Law of Demeter (LoD): principle of least knowledge
#
# 1) method chaining is OK: it does not go against the principle
#    but we should still limit the use of method chain
#      (ex.all methods except last one return the same type object)
#
#   ex.
#     def method():
#         book.pages().last().text()  ==> this is OK (but both pages() and last() returns a Page object)
#         book.textOfLastPage()       ==> no need to change to this
#
#    arguments of a method and objects created within the method are all considered as its knowledge
#      therefore, the Page object is the knowledge that the method needs to know
#
# 2) direct access to object's attributes or use its getters in a method chain is NOT OK
#   ex.
#     def method():
#         a.x.hello()                 ==> NOT OK
#         a.getX().hello()            ==> NOT OK
