# patterns

- patterns of patterns

- null object, singleton pattern, strategy pattern, adapter pattern

## Design Patterns:

| Pattern | Goal | Effect on Cohesion | Effect on Coupling |
| :--- | :--- | :--- | :--- |
| **Null Object** | Provide a default, do-nothing behavior to avoid explicit null checks. | **Increases Cohesion** of client classes. The client class maintains its **Single Responsibility** by delegating the "no-op" logic, preventing core functionality from mixing with error-handling logic. | **Reduces Coupling**. The client is coupled to an **abstract interface** and treats the Null Object identically to a Real Object, eliminating **control coupling** (i.e., the need for `if (object == null)` statements). |
| **Singleton** | Ensure a class has only one instance and provide a global access point. | **Decreases Cohesion**. The class takes on the *secondary responsibility* of managing its own instance and lifecycle, often violating the **Single Responsibility Principle**. | **Increases Coupling**. It introduces **Common Coupling** (coupling through shared global state). Any client class is coupled to the Singleton's implementation details. Changes to the Singleton's internal state can cause non-obvious side effects throughout the system, leading to tight, brittle coupling. |
| **Strategy** | Define a family of algorithms, encapsulate each one, and make them interchangeable. | **Increases Cohesion**. It separates the *policy* (the Context class, which uses the algorithm) from the *implementation* (the Strategy classes). Each Concrete Strategy class achieves **functional cohesion** by focusing on a single algorithm. | **Reduces Coupling**. The client (Context) is coupled only to the **Strategy interface** (loose **abstract coupling**), not to any specific concrete implementation. This makes the system flexible and allows algorithms to be changed independently. |
| **Adapter** | Convert the interface of a class (the Adaptee) into another interface the client expects (the Target). | **Maintains Cohesion**. The Adapter class has the *single responsibility* of performing the translation. Critically, it helps **maintain the cohesion** of the client and the Adaptee by preventing them from needing to modify their own interfaces for compatibility. | **Reduces Coupling**. It decouples the client from the incompatible Adaptee's interface. The client only sees and interacts with the simple **Target interface**, establishing a looser form of **abstract coupling** between the main components. |


- decorator pattern: Not an is a relationship. dont use the strategy, decorate the strategy 
- observer pattern