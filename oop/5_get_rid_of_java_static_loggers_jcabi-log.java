// Get Rid of Java Static Loggers
//
// example:
//
// (bad design: code duplication)

import org.slf4j.LoggerFactory;

public class Foo {

    private static final Logger LOGGER = LoggerFactory.getLogger(Foo.class);

    public void save(String file) { // save the file
        if (Foo.LOGGER.isInfoEnabled()) {
            Foo.LOGGER.info("file {} saved successfuly", file);
        }
    }
}

// why is it bad?
//   the static LOGGER property has to be declared in every class where logging is required

// (good design: jcabi-log, a convenient utility class Logger)

import com.jcabi.log.Logger; // import my utility class for logging

public class Foo {

    public void save(String file) {
        // save the file
        Logger.info(this, "file %s saved successfuly", file); // calls the static method info() for logging
    }
}
// the info() method checks automatically whether a given logging level is enabled
//
// why is it good?
//   the code is simplified and more readable

// note: utility classes are evil, but this example is one of the very few exceptions that uses utility class
