# Mid-term review day

## is-a has-a, needs-a

## RIBS: cover identity again; find examples of each letter in the acronym 

## goal of domain driven design; the objects the customer is thinking of

## Coupling: best type of coupling = Data coupling; Worst case of coupling = content/do it class
    - find an example for each type of coupling.
    - common coupling; public visibility. If no visibility given java gives it package level visibility 
    - stamp coupling; passing in entire objects. The issue with this is you might not need all of the class attributes you're passing in 

    From worst to best: 
    - Content coupling: Do it class
    - Common Coupling: public attributes that should be private
    - external coupling:
    - control coupling
    - Stamp coupling: passing in entire objects including unnecessary fields
    - Data coupling: only passing exactly what you need
    - None: typically not possible


## Cohesion: worst type of coupling is still a do it class becuase it does too much
    you need to cover all examples of cohesion better
    Understand the difference between temporal procedural and sequential coupling
    specifically procedural vs temporal

    From worst to best:
    - Coincidental coupling: Do it class; everything is in there just because
    - Logical Coupling:
    - Temporal Coupling:
    - Procedural Coupling:
    - Communicational Coupling: 
    - Sequential Coupling: 
    - Functional coupling:

## review design patterns
- null object; exists in a place where theres an option to do something but the specific class cannot do it; like a sedan with a plow. it would have a null plow. 
- Singleton; only one of something can exist, and it must be Unique instance! 
- im confused on how this is different than a unique attribute? like couldn't you say an engine "has-a" serial number? (engine is wrong) Two cars might share the same type of engine, all engines have a unique serial number. employee id is also a good example of the singleton. Its just that the thing is has needs to be unique 
- strategy pattern; A list of specific types of algorithm/ behaviors that are interchangeable.
- get more comfortable with the difference between adapter vs decorator 
     decorator is dressing someone up as somebody else; adaptor is dressing someone up as a horse. Adapter changes the interface of an object to adapt it to another interface. A decorator has the same interface of the thing it decorates, it just adds new functionality. The adapter adapts a class to work with a new interface

## UML diagramming and sequence diagramming, ensure you know how the relationships and how they are represented