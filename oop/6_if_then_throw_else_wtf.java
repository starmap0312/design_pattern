// example:
// (bad design)

if (x < 0) {
    throw new Exception("X can't be negative");
} else {
    System.out.println("X is positive or zero");
}

// (good design)
if (x < 0) { // you can later extract this if statement to a validating decorator
    throw new Exception("X can't be negative");
}
System.out.println("X is positive or zero");

// example:
// (bad design)
for (int x : numbers) {
    if (x < 0) {
        continue;
    } else {
        System.out.println("found positive number");
    }
}

// (good design)
for (int x : numbers) {
    if (x < 0) {
        continue;
    }
    System.out.println("found positive number");
}
