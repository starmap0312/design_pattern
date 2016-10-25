// making an instance of an object with overloading methods, without having to actually subclass a class
//
// example 1: register event listener

button.addActionListener(
    new ActionListener() { // an anonymous subclass of class ActionListener
        @Override
        public void actionPerformed(ActionEvent e) {
            // override the class's method 
        }
    }
);
// instantiate an anonymous inner class without actually making a separate class
// the anonymous subclass is instantiated once and should not be known by others
// the instantiated object serves as a callback object
//
// example 2:

public interface Calculator {
    int calculate(int a, int b);
}

public static void main(String[] args) {

    Calculator adder = new Calculator() {      // instantiate an anonymous class
        public int calculate(int a, int b) {
            return a + b;
        }
    };

    Calculator multiplier = new Calculator() { // instantiate an anonymous class
        public int calculate(int a, int b) {
            return a*b;
    }

    System.out.println(adder.calculate(10, 20));
    System.out.println(multiplier.calculate(10, 20));
}
// we don't really name the subclass, but instantiate its object once and use
//
// example3: instantiate an anonymous subclass of an interface

interface HelloWorld {
    public void greet();
    public void greetSomeone(String someone);
}

HelloWorld frenchGreeting = new HelloWorld() {

    public void greet() {
        greetSomeone("world");
    }

    public void greetSomeone(String name {
        System.out.println("Hello " + name);
    }
};
