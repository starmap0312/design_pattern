// Paired Brackets
//
// example:

new Foo( // ends the line
    Math.max(10, 40), // open/close at the same line
    String.format(
        "hello, %s",
        new Name(
            Arrays.asList(
                "Jeff",
                "Lebowski"
            )
        )
    ) // starts the line
);

// example: formatting fluent method calls

public class Test {
    public static void main(String[] args) {
        new Foo(
            new Bar()
                .with(
                    new ImmutableMap.Builder<Integer, String>()
                        .put(10, "First")
                        .put(20, "Second")
                        .build()
                )
                .with("another component")
        );
    }
}

// example: JSON

[
    {
        "name": "Jeff",
        "address": "Los Angeles",
        "details": {
            "title": "CTO",
            "age": "43"
        }
    },
    {
        "files": ["a.txt", "b.txt"]
    }
]

// example: Javascript

$(document).ready(
    function() {
        $('.button').click(
            function() {
                $(this).addClass('light');
            }
        );
    }
);
