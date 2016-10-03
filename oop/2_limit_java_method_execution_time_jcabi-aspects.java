// Limit Java Method Execution Time
//   time out a Java method and raise an exception if the time limit is exceeded
//   jcabi-aspects:
//     based on AspectJ
//   example: most I/O operations in JDK
//     they check the interruption status of their threads while waiting for I/O resources.

public class Resource {

    @Timeable(limit = 5, unit = TimeUnit.SECONDS) // time out the method after 5 seconds
    public String load(URL url) {
        return url.openConnection().getContent();
    }
}

// how AOP aspects work together with Java annotations
//   Due to @Timeable annotation and class weaving,
//     every call to a method load() is intercepted by an aspect from jcabi-aspects
//   that aspect starts a new thread that monitors the execution of a method every second,
//     checking whether it is still running (i.e. creating a monitoring thread)
//   if the method runs for over five seconds, the monitoring thread calls interrupt() on the method's thread
//     but the method thread is NOT terminated immediately on that call, instead:
//     1) interrupt() sets a marker in the method thread
//     2) the method thread checks interrupted() as often as it can
//     3) if the marker is set, the method thread stops and throws InterruptedException


// example: this work() method will not react to interrupt() call
//          it will work until JVM is killed (very bad design)
public void work() {
    while (true) {
        // do something
    }
}

// example: refactor it in order to make sensitive to interruption requests
public void work() {
    while (true) {
        if (Thread.interruped()) {
            throw new InterruptedException();
        }
        // do something
    }
}
// the method can only stop itself. Nothing else can do it
//   the monitoring thread can only send a "timeout message" through interrupt() method

// note: use @Timeable annotation, but keep in mind that there could be situations when a thread 
//   can't be interrupted
