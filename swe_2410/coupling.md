# Cohesion and Coupling

## Big idea is that we want to make our software as modular as possible.

better modularity means its faster for someone who didn't write the code to understand and debug code. 

Cohesion = what a method does, whats it's responsibility. More cohesion means that everything works together to do less responsibilities.
Coupling =  interactions though parameters, attributes, static data, etc.  the degree of interdependence between components. High coupling means that when one thing breaks, everything breaks
Coupling is usually contrasted with cohesion. Low coupling often correlates with high cohesion, and vice versa

- Adapter pattern lowers coupling, has no impact to cohesion
- strategy pattern has higher cohesion, but also possibly higher coupling

## Coupling & cohesion examples

- individual methods:
    - Cohesion: what a method does
    - Coupling: interactions with parameters
- subsystems:
    - Cohesion: 

- content coupling: using data, control encapsulated within the boundary of another module. bypassing protected (like for example calling __func() in python) makes stuff hard to fix in the future, but can provide short term speed benefits. THE WORST FORM OF COUPLING!
- common coupling: leaving data unrestricted. Theres no real encapsulation here. 