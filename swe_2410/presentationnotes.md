# Presentation Notes

## Chain of responsibility
 
 * Chain of handlers, e.g. a IT dept where a ticket filters through layers depending on severity 
 * **Interface:**

![alt text](W3sDesign_Chain_of_Responsibility_Design_Pattern_UML.jpg)

## State

## Mediator

* Similar to observer but through a single class (that "mediates"). Seems like it turns into an anti-pattern really quickly
* **Interface:**

![alt text](W3sDesign_Mediator_Design_Pattern_UML.jpg)


## Flyweight

* A pattern for preventing the issue of large memory footprints when you have to create a bunch of objects from the same class. Flyweight pattern limits memory use by sharing parts, like images
* **Interface:**

![alt text](W3sDesign_Flyweight_Design_Pattern_UML.jpg)

## Builder

* A pattern for limiting complexity when building complex objects
* Allows you to create unique objects with a single constructor
* **Interface**

![alt text](W3sDesign_Builder_Design_Pattern_UML.jpg)

* This relates to the factory pattern;
  * The Factory pattern creates an entire object in a single method call, typically when the exact type is unknown until runtime, while the Builder pattern constructs a complex object step-by-step, providing more control over the configuration and composition process.