// CONTAINMENT ("HAS A" RELATIONSHIPS)

// INHERITANCE ("IS A" RELATIONSHIPS)
// 1) define a base class that specifies common elements of multiple derived classes
//    facilitate code reuse and centralize data within a base class
// 2) deep inheritance trees increase complexity
// 3) prefer polymorphism to extensive type checking (i.e. recurring switch statement)
//
// example: a swith statement that should be replaced by polymorphism
//          (same type of behaviors, i.e. implement same interface)
//
// (bad design: adding a new shapes needs to modify the switch statement)
switch ( shape.type ) {
    case Shape_Circle:
        shape.DrawCircle();
        break;
    case Shape_Square:
        shape.DrawSquare();
        break;
}

// (good design: polymorphism)
shape.Draw();             // got called regardless of whether the shape is a circle or a square

// example: a swith statement that should NOT be replaced by polymorphism
//          (different types of behaviors, i.e. implement different interfaces)
//
// (good design: more descripitve and understandable)
switch ( ui.Command() ) {
    case Command_OpenFile:
        OpenFile();
        break;
    case Command_Print:
        Print();
        break;
    case Command_Save:
        Save();
        break;
    case Command_Exit:
        ShutDown();
        break;
}

// (bad design)
ui.DoCommand();          // meaningless and not understandable

//
// Why Are There So Many Rules for Inheritance?
// rules that reduces complexity:
// 1) if multiple classes share common data but not behavior, create a common object that those classes can contain
// 2) if multiple classes share common behavior but not data, derive them from a common base class that defines the common routines
// 3) if multiple classes share common data and behavior, inherit from a common base class that defines the common data and routines
// 4) inherit (IS_A) when you want the base class to control your interface
//    contain (HAS_A) when you want to control your interface
//

