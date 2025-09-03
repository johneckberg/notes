# A Quick UML Diagram review 

[Hasker's UML Standards](https://faculty-web.msoe.edu/hasker/swe2410/UML-standards.html)

[UML specifications](https://www.omg.org/spec/UML/2.5.1/About-UML)

## Classes:

A class is represented by a rectangle having three sections:

the top section containing the name of the class
the middle section containing class attributes
the bottom section representing operations of the class

## Class Attributes & Methods:

The visibility of the attributes and Methods can be represented in the following ways −

Public − A public member is visible from anywhere in the system. In class diagram, it is prefixed by the symbol +.

Private − A private member is visible only from within the class. It cannot be accessed from outside the class. A private member is prefixed by the symbol .

Protected − A protected member is visible from within the class and from the subclasses inherited from this class, but not from outside. It is prefixed by the symbol #.

## Interfaces & Abstract Classes:

The name of an abstract Class is shown in italics, where permitted by the font in use. Alternatively or in addition, an abstract Class may be shown using the textual annotation {abstract} after or below its name. In addition, abstract methods are also italicized.

The name of an interface is italicized and «interface» is placed above the interface name.
A dashed line going from a class to an interface, terminating with an open arrow signifies that the class implements the interface.

## Associations:

- Aggregation: Some associations imply a "whole-part" relationship.
An unfilled (open) diamond on the side that is the "whole" is used to denote this. For Example, students belong to/make up a section object.
- Composition: Some "whole-part" relationships represent an even stronger link.
A filled (closed) diamond on the side of the "whole" is used to denote this. For example, sections belong to/make up a course object.
- Dependency: one class may make use of another class
A dotted line is used to denote this, with an arrow that points to the class that is depended upon
- Inheritance: The relationship between a subclass and a superclass
A non dotted line with an open arrow pointing to parent class is used to denote this.