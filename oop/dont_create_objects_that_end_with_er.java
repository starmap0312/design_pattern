// Don't Create Objects That End With -ER
//   ex. Manager. Controller. Helper. Handler. Writer. Reader. Converter. Validator
//       Router. Dispatcher. Observer. Listener. Sorter. Encoder. Decoder
//
// why is it bad?
//   they are not classes / objects; they are collections of procedures pretending to be classes
//   ex. when you need a manager, the managed are just plain old data structures and the manager is
//       the smart procedure doing the real work
//   a good object name is not a job title; it should be a representative of real-world entities
//   they encourage imperative programming, not declarative programming
//
// example:
//
// (bad design: imperative programming)

List<Apple> sorted = new Sorter().sort(apples); // get them sorted immediately and never interact again
Apple biggest = sorted.get(0);
// sorter is a dumb imperative executor of your will

// (good design: declarative programming)

List<Apple> sorted = new Sorted(apples);        // a real object that will behave like a sorted list of apples
Apple biggest = sorted.get(0);                  // consider them sorted; do what you want to do next
// sorted apples are a living organism with its own will and behaviors

// the "-er" suffix is a sign of disrespect toward the poor object
