# Notes from review

One Cheat sheet, both sides like last time

All material up through week 9

More code writing, no javadoc headers, just code.

- probably no multithreading
- As always, focus on verbs and nouns 

- cohesion, coupling. Recall the specific pyramids?
  - RIBS again (responsibility, identity, behavior, state)
    - single responsibility at the domain level
    - Coupling and cohesion at the domain level
  - maybe not as much on the specifics?


- Design patterns
  - Understand things at the interface level
  - Maybe draw out each interface on the note sheet?
  - how do each of these interfaces effect cohesion and coupling?
  - Study up on composite pattern
    - parts of a whole, used to represent hierarchies
    - you have components (internal nodes), and leafs. both implement the component interface
  - Study up on visitor interface
    - The strategy pattern is like a 1:many relationship, while the visitor pattern is many:many
  - Study on on facade pattern, adapter vs facade vs decorator
    - Facade pattern: consider the name: "something that wraps on object to make it pretty/simple
      - consider, a receptionist interface for all the functions of an office

Patterns that need to be covered:
    - Singleton
      - when you only want one unique item
    - Null
      - when you really need to make sure nothing happens
    - MVC
      - 


    - Strategy
      - allows for changing class behavior at run time
    - Adapter
      - applies a wrapper at compile time that allows a class to work with a previously incompatible interface
    - Observer
      - Observer interface
      - subject interface
    - Command
      - command has execute, unexecuted methods
    - Decorator
      - provides new functionality at runtime by wrapping a class
    - Composite
    - Visitor
      - The strategy pattern is like a 1:many relationship, while the visitor pattern is many:many
    - Facade
      - Facade pattern: consider the name: "something that wraps on object to make it pretty/simple
      - consider, a receptionist interface for all the functions of an office