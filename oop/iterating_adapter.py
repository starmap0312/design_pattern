# iterating adapter
#   iterate a stream of data coming from some other source
#
#  // a source of data
#  final class Data {
#    byte[] read();
#  }
#  
#  // the iterator interface has two methods
#  final class FluentData implements Iterator<Byte> {
#    boolean hasNext() { /* ... */ }
#    Byte next() { /* ... */ }
#  }
#  
#  // implementation of iterator
#  final class FluentData implements Iterator<Byte> {
#
#      private final Data data;
#      private final Queue<Byte> buffer = new LinkedList<>(); // a list to hold the data
#
#      public FluentData(final Data d) {
#          this.data = d;
#      }
#
#      public boolean hasNext() {
#          if (this.buffer.isEmpty()) {                       // if list is empty, read in more data elements
#              for (final byte item : this.data.read()) {
#                  this.buffer.add(item);
#              }
#          }
#          return !this.buffer.isEmpty();
#      }
#
#      public Byte next() {
#          if (!this.hasNext()) {                             // check out the next data element
#              throw new NoSuchElementException("Nothing left");
#          }
#          return this.buffer.poll();                         // returns the next data element
#      }
#
#  }
