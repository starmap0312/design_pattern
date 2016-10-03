// Cache Java Method Results
//   jcabi-aspects:
//     based on AOP aspects and Java6 annotations
//     cache method results for some time in memory
//   other libraries:
//     ex. Apache Commons JCS, Ehcache, JSR 107, Guava Caching
//
// example:

import com.jcabi.aspects.Cacheable;

public class Page {

    @Cacheable(lifetime = 5, unit = TimeUnit.MINUTES) // cache the method result for 5 minutes
    String load() {
        return new URL("http://google.com").getContent().toString();
    }
}

// how caching works: a static hash map with (key, value) pairs
//   key: method coordinates, i.e. the object, an owner of method, method name with parameter types
//   value: method result
//
//   right after the above method load() finishes, the hash map gets a new entry
//     key: [page, "load()"]
//     value: "<html>...</html>"
//   every consecutive call to load() will be intercepted by the aspect from jcabi-aspects and
//     resolved immediately with a value from the hash map
//   the method has no control until the end of its lifetime, i.e. 5 minutes
//
//
// What About Cache Flushing

import com.jcabi.aspects.Cacheable;

public class Employees {

    @Cacheable(lifetime = 1, unit = TimeUnit.HOURS)
    int size() {
        // calculate their amount in MySQL
    }

    @Cacheable.FlushBefore
    void add(Employee employee) { // flush cached results of all the class methods before the method executes
        // add a new one to MySQL
    }
}

// note: use @Cacheable.FlushAfter will flush all cached results after method add() finishes
