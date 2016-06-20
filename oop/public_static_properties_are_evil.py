# Public static properties are evil
#
# ex. Apache Commons defines a public static property: CharEncoding.UTF_8
#
#     (bad design)
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
#     // the client code
#     ex1. create a String from a byte array
#     import org.apache.commons.lang3.CharEncoding;
#     String text = new String(array, CharEncoding.UTF_8);
#
#     ex2. convert a String into a byte array
#     import org.apache.commons.lang3.CharEncoding;
#     byte[] array = text.getBytes(CharEncoding.UTF_8);
#
#     (good design)
#
#     // the client code
#     String text = new UTF8String(array);
#
#     a) encapsulate the "UTF-8" constant inside a new class UTF8String
#     b) this decouples the client from the constant string data
#        the client have no idea how exactly this "byte array to string" conversion is happening
#     c) this encapsulates the functionality inside a class and let everybody instantiate objects and use them
#        it resolves the problem of functionality duplication, not just data duplication
#
#  why it is a bad design:
#  1) once you use CharEncoding.UTF_8, your object starts to depend on this data, and the user of your object
#     can't break this dependency
#  2) placing data into one shared place (CharEncoding.UTF_8) doesn't really solve the duplication problem
#     it encourages everybody to duplicate functionality using/depending the same piece of shared (constant) data
#
#  rule of thumbs
#    1) every time seeing some data duplication in your application, start thinking about the functionality
#       you're duplicating (you will find the code that is repeated again and again)
#
#       ex. String text = new String(array, CharEncoding.UTF_8);
#
#    2) make a new class for this code and place the data there
#       as a private property or private static property (that's how you get rid of duplication)
#
#       ex. String text = new UTF8String(array);

