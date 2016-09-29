// Iterating Adapter
//   adapt a data source to have methods: hasNext() and next()
//   provide services that iterate a stream of data coming from some other source
//
// example:

// interface of the data source
final class Data {
    byte[] read();
}

// an adapter class that consumes the data source and let us iterate them
final class FluentData implements Iterator<Byte> {

    private final Data data;
    private final Queue<Byte> buffer = new LinkedList<>(); // a list/queue for buffering 

    public FluentData(final Data dat) {
        this.data = dat;
    }

    public boolean hasNext() {
        if (this.buffer.isEmpty()) { // try to read more data if nothing left in the buffer queue
            for (final byte item : this.data.read()) {
                this.buffer.add(item);
            }
        }
        return !this.buffer.isEmpty();
    }

    public Byte next() {
        if (!this.hasNext()) {
            throw new NoSuchElementException("Nothing left");
        }
        return this.buffer.poll();   // pop one element out of the queue
    }
}

// it's not thread-safe:  two threads may conflict if they both call hasNext() and next()
