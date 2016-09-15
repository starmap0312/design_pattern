# vertical vs. horizontal decomposition of responsibility
  vertical decomposition is better
  ex.

    (before decomposition)

    // a class that is responsible for two things: formatting the text and writing the formated text to a file
    class Log

        def initialize(path)
            @file = IO.new(path, 'a')
        end

        def put(text)
            line = Time.now.strftime("%d/%m/%Y %H:%M ") + text
            @file.puts line
        end
    end

    (after horizontal decomposition)

    // the class is responsible for only writing the line to a file
    class Log

        def initialize(path)
            @file = IO.new(path, 'a')
        end

        def put(line)
            @file.puts line
        end
    end

    // an additional class that is responsible for formatting the text
    class Line

        def initialize(text)
            @line = text
        end

        def to_s
            Time.now.strftime("%d/%m/%Y %H:%M ") + text
        end
    end

    // the client class: need to know both classes Log and Line to provide its service
    class Script

        def write(text, filepath):
            log = Log.new(filepath)
            log.put(Line.new(text))

    // horizontally decomposition increases complexity as client has more dependencies and points of contact
    class Script --> class Log
                 --> class Line

    (after vertical decomposition)

    // the class is responsible for only writing the line to a file
    class Log

        def initialize(path)
            @file = IO.new(path, 'a')
        end

        def put(line)
            @file.puts line
        end
    end

    // a decorator class which responsible for providing formatting docoration to the text
    class TimedLog

        def initialize(log)
            @origin = log
        end

        def put(text)
            @origin.put(Time.now.strftime("%d/%m/%Y %H:%M ") + text)
        end
    end

    // the client class only one entry point to Log object
    class Script

        def write(text, log):
            // the Log object "consists" of two objects, one wrapped into another
            log = TimedLog().new(log)
            log.put(text)

    log = Log.new('/tmp/log.txt')

    // vertical decomposition decreases complexity
    class Script --> class TimedLog --> class Log

