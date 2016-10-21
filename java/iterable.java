
// an implementation of Iteratable<T>
public class MyIterable<T> implements Iterable<T>{

    public Iterator<T> iterator() {
        return new MyIterator<T>();
    }
}

// an implementation of Iterator<T>
public class MyIterator<T> implements Iterator<T> {

    public boolean hasNext() {
        // ...
    }

    public T next() {
        // ...
    }
}

// use the MyIterable with the for-loop

public static void main(String[] args) {

    MyIterable<String> iterable = new MyIterable<String>();

    for(String string : iterable){

    }
}
