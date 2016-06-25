# testing methods must share nothing
#
#  example:
#
#  (bad design)
#
#  class FooTest {
#
#      private static final String MSG = "something"; // MSG: a static private literal
#
#      @Before
#      public final void setUp() throws Exception {
#          this.foo = new Foo(FooTest.MSG);           // the testing object depends on the static field MSG
#      }
#
#      @Test
#      public void simplyWorks() throws IOException {
#          assertThat(
#              foo.doSomething(),
#              containsString(FooTest.MSG)            // both test methods depend on the same static field MSG
#          );
#      }
#
#      @Test
#      public void simplyWorksAgain() throws IOException {
#          assertThat(
#              foo.doSomethingElse(),
#              containsString(FooTest.MSG)            // both test methods depend on the same static field MSG
#          );
#      }
#  }
#
#  what is wrong?
#   the shared literal MSG introduced an unnatural coupling between the two test methods
#   but they have nothing in common, because they test different behaviors of class Foo
#   this private constant ties them together (they are somehow related)
#     i.e. you cannot change the content of MSG for one method, because you will affect the other method
#
#  (partial solution)
#
#  class FooTest {
#
#      @Test
#      public void simplyWorks() throws IOException {
#          assertThat(
#              new Foo("something").doSomething(),          // instantiate a new object for each test method
#              containsString("something")
#          );
#      }
#
#      @Test
#      public void simplyWorksAgain() throws IOException {
#          assertThat(
#              new Foo("something").doSomethingElse(),      // instantiate a new object for each test method
#              containsString("something")
#          );
#      }
#  }
#
#  what is wrong?
#    we have decoupled the two testing methods (they have their own test object and strings: "something"
#    but the code is duplicated, as "something" appear four times
#
#  (complete solution)
#
#  class FooTest {
#
#      @Test
#      public void simplyWorks() throws IOException {
#          final String msg = "something";                  // the test method has its own set of data and objects
#          assertThat(
#              new Foo(msg).doSomething(),
#              containsString(msg)
#          );
#      }
#
#      @Test
#      public void simplyWorksAgain() throws IOException {
#          final String msg = "something else";             // the test method has its own set of data and objects
#          assertThat(
#              new Foo(msg).doSomethingElse(),
#              containsString(msg)
#          );
#      }
#  }
#
#  rule of thumbs:
#    a) don't share data and objects between test methods, as it creates coupling
#    b) test methods must always be independent, having nothing in common
#    c) don't use methods like setUp() or any shared variables in test classes

