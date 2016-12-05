// - Reasons to create a class
//   1) model real-world objects
//   2) model abstract objects
//   3) reduce complexity: classes are primary tool for managing complexity
//   4) isolate complexity
//   5) hide implementation details
//   6) limit effects of changes
//   7) hide global data
//   8) avoid streamline parameter passing
//
// - Streamline parameter passing
//   passing a parameter among several routines indicates a need to factor those routines into a class that
//   share the parameter as object data
//   (passing parameters between objects creates coupling between objects)
//   (share common object data in related member methods creates coupling between methods)
//
// - Classes to avoid
//   avoid creating god classes (classes with too many responsibilities)
//   eliminate irrelevant classes (DTO: data transfer object, data place holder)
