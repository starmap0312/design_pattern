# public static literals are evil
#   similarly, utility classes with public static methods are also evil
#
# ex. Apache Commons defines a public static property: CharEncoding.UTF_8
#
#     (bad design: use public static literals to avoid code duplicaiton)
#
#     package org.apache.commons.lang3;
#
#     public class CharEncoding {
#
#         public static final String UTF_8 = "UTF-8";  // a public static constant property
#
#         // some other methods and properties
#     }
#
#     // ex1. the client code: to convert a byte array into a String
#     import org.apache.commons.lang3.CharEncoding;
#     String text = new String(array, CharEncoding.UTF_8);
#
#     // ex2. the client code: to convert a String into a byte array
#     import org.apache.commons.lang3.CharEncoding;
#     byte[] array = text.getBytes(CharEncoding.UTF_8);
#
#     why is it bad?
#     1) once you use CharEncoding.UTF_8, your object starts to depend on this data
#        the user of your object can't break this dependency
#     2) placing data into one shared place (CharEncoding.UTF_8) doesn't really solve the duplication problem
#        it encourages everyone to duplicate functionality using the piece of constant data
#
#     (good design: encapsulate the public constant inside a new class that provides the same service)
#
#     // ex1. the client code: to convert a byte array into a String
#     String text = new UTF8String(array);  ==> create a new class/object that provides the service
#                                               encapsulate the "UTF-8" constant inside that class
#     // as Java makes class String final, in reality we will have to write this:
#     String text = new UTF8String(array).toString();
#
#     why is it good?
#     a) encapsulate the "UTF-8" constant inside the new class UTF8String
#     b) this decouples the client from the constant string data
#        the client have no idea how exactly this "byte array to string" conversion is happening
#     c) this encapsulates the functionality inside a class 
#        let everybody instantiate objects and use them independently
#        resolves the problem of functionality duplication, not just data duplication
#
#  rule of thumbs
#    every time seeing some data duplication in your application
#      instead of thinking about the data duplication, thinking about the functionality duplication
#      you will find the code that is repeated again and again
#
#       ex. String text1 = new String(array1, CharEncoding.UTF_8);
#           String text2 = new String(array2, CharEncoding.UTF_8);
#
#    make a new class/object for this code and place the data there
#      declare it as a private (static) property (that's how you get rid of duplication)
#
#       ex. String text1 = new UTF8String(array1);
#           String text2 = new UTF8String(array2);

