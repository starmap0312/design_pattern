// Simple Java SSH Client
//
// the interface 
interface Shell {

    int exec(
        String cmd,
        InputStream stdin,
        OutputStream stdout,
        OutputStream stderr
    );
}

// example 1: upload a file via SSH and then read back its grepped content
Shell shell = new SSH(
    "ssh.example.com", 22,
    "yegor", "-----BEGIN RSA PRIVATE KEY-----..."
);
// class SSH, which implements interface Shell, has only one method with four arguments

File file = new File("/tmp/data.txt");
new Shell.Safe(shell).exec(
    "cat > d.txt && grep 'some text' d.txt",
    new FileInputStream(file),
    Logger.stream(Level.INFO, this),
    Logger.stream(Level.WARNING, this)
);
// Shell.Safe decorates a Shell object and throws an exception if exit code is not equal to zero
//   used when you want to make sure that your command executed successfully, but don't want to
//   duplicate if/throw in many places of your code
//
// example 2: execute a shell command via SSH
String hello = new Shell.Plain(
    new SSH(
        "ssh.example.com", 22,
        "yegor", "-----BEGIN RSA PRIVATE KEY-----..."
    )
).exec("echo 'Hello, world!'");
// a wrapper/adapter of a Shell object that introduces a new exec method with one argument, a command to execute

String login = new Shell.Plain(new Shell.Safe(ssh)).exec("whoami");

//
// example 3: copies stdout and stderr to the slf4j logging facility
Shell ssh = new Shell.Verbose(
    new Shell.Safe(
        new SSH(
            "ssh.example.com", 22,
            "yegor", "-----BEGIN RSA PRIVATE KEY-----..."
        )
    )
);
// shell.Verbose decorates a Shell object and copies stdout and stderr to logging facility (using jcabi-log)

