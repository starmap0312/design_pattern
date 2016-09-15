# inherience/extends is evil 
  1) no concrete base classes, use interfaces instead
  2) programming to interfaces, not implementations
  3) create tight coupling between derived classes and base class 
     (modifying base class may affect derived classes)
  4) most of the code should be written entirely in terms of interfaces, ex. not HashMap but Map interface

# inheritence/subtyping itself is not evil, it enables polymorphism
  inheritance/subtyping: deriving a characteristic from another object
  ex.
    Article inherits all characteristics of objects in class Manuscript and adds its own

    interface Manuscript {

        void print(Console console);

    }

    interface Article extends Manuscript {
        // a derived interface, which inherits the print() characteristic of the parent interface
        // object of derived interface should behave just like the advertised behaviors of parent interface
        // but it can have its own characteristic

        void submit(Conference cnf);

    }

    whenever a manuscript is required, we can provide an article and nobody will notice anything
      because type Article is a subtype of type Manuscript
      i.e. Liskov Substitution Principle: derived classes must be completely substitutable for base classes

# what is evil is implementation inheritance
  an object is dead and it allows other objects to inherit its encapsulated code and data
    copying methods and attributes from a parent class: not deriving characteristics
  ex.
    class Manuscript {

        protected String body;

        void print(Console console) {
            System.out.println(this.body);
        }

    }

    class Article extends Manuscript {
        // body attribute and print() is inherited and can be used by the derived class

        void submit(Conference cnf) {
            cnf.send(this.body);
        }

    }

    Class Article copies method print() and attribute body from class Manuscript

# implementation inheritance is a procedural technique for code reuse
  implementation inheritance turns objects into containers with data and procedures

