// maintenance vs. modifiability (flexibility)
//   the earlier the binding time, the lower the flexibility and the lower the complexity
//   minimize complexity but extend flexibility at the same time
// different binding times
// 1) Coding time (magic numbers)

// 0xFF is hex value for color blue
titleBar.color = 0xFF;                           // hard coding everywhere, not flexible at all

// 2) Compile time (use of a named constant)

private static final int TITLE_BAR_COLOR = 0xFF; // more flexiable, easiler to change once and at a place

titleBar.color = TITLE_BAR_COLOR;

// 3) Load time (from an external source, ex. reading a value from a file)

// 4) Run time (object instantiation time, ex. reading the value each time a window is created)

titleBar.color = ReadTitleBarColor();            // more readable and flexible, but increase code complexity

// 5)Just in time (ex. reading the value each time the window is drawn)
